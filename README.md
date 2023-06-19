# README

```ps
$destination = "..\..\results\prueba\img\"
$path = pwd
Get-ChildItem -Path $path.path -Include *.jpg,*.png -Recurse | Copy-Item -Destination $destination
```

```ps
pipenv shell
py .\main.py
```

## Ignore the following

```ps
Copy-Item $source -Destination (New-Item -Path (Split-Path -Path $destination) -Type Directory)
```

## Roadmap

- [x] Get the first question too
- [x] Fix the answer to allow multiple answers (`<div class="voting-summary`)
- [ ] crear ps1 que pase imágenes etc.
