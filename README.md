![BuildScour](https://socialify.git.ci/darshkpatel/BuildScour/image?description=1&descriptionEditable=Scour%20popular%20CI%20tools%20build%20logs%20for%20sensitive%20information&language=1&owner=1&theme=Light)


<p align="center">
<a href="https://pypi.org/project/BuildScour/"><img alt="PyPI" src="https://img.shields.io/pypi/v/BuildScour?label=PyPi%20Package%20&style=for-the-badge"></a>
<img alt="PyPI - License" src="https://img.shields.io/pypi/l/BuildScour?style=for-the-badge">
<a href="https://ssh.cloud.google.com/cloudshell/editor?cloudshell_git_repo=https%3A%2F%2Fgithub.com%2Fdarshkpatel%2FBuildScour&cloudshell_git_branch=master&cloudshell_tutorial=README.md"><img src="https://img.shields.io/badge/Google%20Cloud-Open%20in%20Goole%20Cloud%20Shell-blue?style=for-the-badge&logo=google-cloud" /></a>
</p>

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
