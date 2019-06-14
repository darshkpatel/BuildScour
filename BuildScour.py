#Developed by darshkpatel 

import os
import logging
import requests
import argparse

from sys import stdout

logger=logging.getLogger(__name__)
formatter=logging.Formatter('%(asctime)s [%(levelname)s]  %(message)s')

#Argument Parsing 
parser = argparse.ArgumentParser(description='Scour CI Build Logs')
parser.add_argument('-l', dest='link', type=str, help='organizations github handle')
parser.add_argument('-v', dest='verbose', help='Show verbose output', action='store_true')
parser.add_argument('-A', dest='all', help='Scan organizations peoples profile too', action='store_true')
parser.add_argument('--log', dest='log', help='store output in file', type=str)
parser.add_argument('-o', dest='output', help='stores retrived log files in folder', type=str)
args = parser.parse_args()

#Setup Logging 
if args.verbose:
    logger.setLevel(logging.DEBUG)
else:
    logger.setLevel(logging.INFO)
    
if args.log:
    file_handler=logging.FileHandler(args.log)
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.DEBUG)
    logger.addHandler(file_handler)

stream_handler=logging.StreamHandler(stdout)
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.INFO)
logger.addHandler(stream_handler)

#Check Github link and token
if not args.link:
    logging.error("Github profile Not Provided")
    parser.print_usage()
    exit(1)

try:
    if  os.environ['GITHUB_TOKEN']:
        logger.info("Found github token")
        token = os.environ['GITHUB_TOKEN']
except KeyError:
    logger.error("Please save your github oauth token in environment variable 'GITHUB_TOKEN'")
    logger.error("use: export GITHUB_TOKEN=[oauth token]")
    exit(1)

# Check Output Directory
if not args.output:
    logging.error("Output directory Not Provided")
    parser.print_usage()
    exit(1)

if str(args.output)[-1]=='/':
    output_path = args.output
else:
    output_path = args.output + '/'

#Making Log Dirs 
if not os.path.exists(args.output):
    os.makedirs(args.output)


logger.info(f"Scouring {args.link} profile")


# Find all Repos on github using Github REST API v3
org_repositories = requests.get(f"https://api.github.com/orgs/{args.link}/repos", headers={'Authorization': f'token {token}'})
user_repositories = requests.get(f"https://api.github.com/users/{args.link}/repos", headers={'Authorization': f'token {token}'})

try:
    if 'message' not in org_repositories.json():
        to_check = [repo['full_name'] for repo in org_repositories.json()] 
        logger.info(f"Found {len(to_check)} repos in the Organization")
        if args.all:
            logger.info("Finding users associated with the organization")
            org_members = requests.get(f"https://api.github.com/orgs/{args.link}/members", headers={'Authorization': f'token {token}'})
            usernames = [member['login'] for member in org_members.json()]
            logger.info(f"Found {len(usernames)} users in organization")
            for user in usernames:
                user_repositories = requests.get(f"https://api.github.com/users/{user}/repos", headers={'Authorization': f'token {token}'})
                user_repo_list = [repo['full_name'] for repo in user_repositories.json()]
                to_check = to_check + user_repo_list

    else:
        to_check = [repo['full_name'] for repo in user_repositories.json()]

    logger.info(f'Found {len(to_check)} Repos')



    #Find github repos on Travis
    logger.info("Scouring Travis-CI")
    for repo in to_check:
        builds = requests.get(f'http://api.travis-ci.org/repos/{repo}/builds').json()
        if not builds:
            logger.debug(f"NO Builds exist for {repo} on Travis-CI")
        else:
            logger.info(f"Found {len(builds)} builds for {repo} on Travis CI")
            logger.debug(f"----------------------------------------------------\n\n\n{builds}\n\n\n")
            logger.info(f"Downloading build logs for {repo} in {output_path+repo}")
            for build in builds:
                logger.debug(f"Saving build {build['id']}")
                if not os.path.exists(output_path+repo):
                    logger.debug(f"Making Directory {output_path+repo}")
                    os.makedirs(output_path+repo)
                with open(output_path+repo+'/'+str(build['id'])+'-travis.txt',"w+") as f:
                    try:
                        f.write(str(requests.get(f"https://api.travis-ci.org/v3/job/{str(int(build['id'])+1)}/log.txt").text))
                    except Exception:
                        logger.error(f"Error Fetching Build Logs got {str(int(build['id'])+1)}")


    # Find github repos on circle-ci
    logger.info("Scouring Circle-CI")
    for repo in to_check:
        try:
            builds = requests.get(f'https://circleci.com/api/v1.1/project/github/{repo}').json()
            if builds == {'message': 'Project not found'}:
                logger.debug(f"NO Builds exist for {repo} on Circle-CI")
            else:
                logger.info(f"Found {len(builds)} builds for {repo} on Circle CI")
                logger.debug(f"----------------------------------------------------\n\n\n{builds}\n\n\n")
                logger.info(f"Downloading build logs for {repo} in {output_path+repo}")
                for build in builds:
                    logger.debug(f"Saving build {build['build_num']}")    
                    if not os.path.exists(output_path+repo):
                        logger.debug(f"Making Directory {output_path+repo}")
                        os.makedirs(output_path+repo)
                    build_details = requests.get(f"https://circleci.com/api/v1.1/project/github/{repo}/{str(build['build_num'])}").json()
                    for step in build_details['steps']:
                        for action in step['actions']:
                            if 'output_url' in action:
                                with open(output_path+repo+'/'+str(build['build_num'])+'-circle.txt',"a+") as f:
                                    f.write(str(requests.get(action['output_url']).json()[0]['message']))
        except Exception:
            logger.error("Error fetching repo details")
except KeyboardInterrupt:
    logger.error("Keyboard Interrupt Stopping")