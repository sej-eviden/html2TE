# README

```ps
$path = pwd
Get-ChildItem -Path $path.path -Include *.jpg,*.png -Recurse | Copy-Item -Destination ./img/
```

```ps
pipenv shell
mkdir <cert name>
py .\main.py -file ".\path\to\exam.html"
```

## Roadmap

- [x] Get the first question too
- [x] Fix the answer to allow multiple answers (`<div class="voting-summary`)
