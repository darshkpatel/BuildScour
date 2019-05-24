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
parser.add_argument('--org', dest='org', type=str, help='organizations github handle')
parser.add_argument('-v', dest='verbose', help='Show verbose output', action='store_false')
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
    file_handler.setLevel(logging.INFO)
    logger.addHandler(file_handler)

stream_handler=logging.StreamHandler(stdout)
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.INFO)
logger.addHandler(stream_handler)

#Check Github link and token

if not args.org:
    logging.error("Github profile Not Provided")
    parser.print_usage()
    exit(1)

if not os.environ['GITHUB_TOKEN']:
    logger.error("Please save your github oauth token in environment variable 'GITHUB_TOKEN'")
    logger.error("use: export GITHUB_TOKEN=[oauth token]")
    exit(1)
else:
    logger.info("Found github token")
    token = os.environ['GITHUB_TOKEN']

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


logger.info(f"Scouring {args.org} profile")

#members = requests.get(f"https://api.github.com/orgs/{args.org}/members", headers={'Authorization': f'token {token}'})
repositories = requests.get(f"https://api.github.com/orgs/{args.org}/repos", headers={'Authorization': f'token {token}'})
to_check = [repo['full_name'] for repo in repositories.json()]

logger.info(f'Found {len(to_check)} Repos')

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
            with open(output_path+repo+str(build['id'])+'.txt',"w+") as f:
                f.write(str(requests.get(f"https://api.travis-ci.org/v3/job/{str(int(build['id'])+1)}/log.txt").text))


                
        