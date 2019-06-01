# Build Scour 
Scours CI Build logs for github Organizations/Users
[![PyPI
version](https://badge.fury.io/py/BuildScour.svg)](https://badge.fury.io/py/BuildScour)


# Usage

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
