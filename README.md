## Build Scour [![PyPI version](https://badge.fury.io/py/BuildScour.svg)](https://badge.fury.io/py/BuildScour)
Scours CI Build logs for github Organizations/Users

[![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.svg)](https://ssh.cloud.google.com/cloudshell/editor?cloudshell_git_repo=https%3A%2F%2Fgithub.com%2Fdarshkpatel%2FBuildScour&cloudshell_git_branch=master&cloudshell_tutorial=README.md)


## Usage

* NOTE: please Set github oauth token in environment variable `GITHUB_TOKEN` 

```
 export GITHUB_TOKEN=[oauth token]
```
### Use PyPi Package:
```
pip install BuildScour
```
```
python -m BuildScour [-h] [-l LINK] [-v] [-A] [--log LOG] [-o OUTPUT]
```
### Use from Source:
```
git clone https://github.com/darshkpatel/BuildScour && cd BuildScour
```
```
python BuildScour.py [-h] [-l LINK] [-v] [-A] [--log LOG] [-o OUTPUT]
```
### Detailed Usage
```
usage: BuildScour [-h] [-l LINK] [-v] [-A] [--log LOG] [-o OUTPUT]

Scour CI Build Logs

optional arguments:
  -h, --help  show this help message and exit
  -l LINK     organizations github handle
  -v          Show verbose output
  -A          Scan organizations peoples profile too
  --log LOG   store output in file
  -o OUTPUT   stores retrived log files in folder
  
  ```

#### Example Usage
To Scour `RocketChat`'s github repositories:

```
python BuildScour.py -l RocketChat -A -o ./BuildLogs/ --log rocket.log
```
```
python -m BuildScour.py RocketChat -A -o ./BuildLogs/ --log rocket.log
```


#### What next ?

After getting saving all the logs locally, you can analyze the logs manually or use grep to find sensitive information. 
There are a couple of word lists containing common environment variables containing API keys and passwords in the `Keywords` folder.  
