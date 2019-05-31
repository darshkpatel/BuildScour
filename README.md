# Build Scour
Scours CI Build logs for github Organizations/Users

# Usage

* NOTE: please Set github oauth token in environment variable `GITHUB_TOKEN` 

```
 export GITHUB_TOKEN=[oauth token]
```


```

usage: python -m BuildScour [-h] [-l LINK] [-v] [-A] [--log LOG] [-o OUTPUT]

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

```
python -m BuildScour -l RocketChat -A -o ./BuildLogs/ --log rocket.log
````