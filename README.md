# scup-python
Unnofficial Python library for the Scup API v1.1. http://www.scup.com/docs/api

## Installation
```bash
pip install scup-python
```

## Requires
* requests
* simplejson
* six

## Usage
```python
from scup import ScupAPI

api = ScupAPI(public_key, private_key)

monitorings = api.monitorings()
```
