# Lineage Service

[![License: AGPL v3](https://img.shields.io/badge/License-AGPL_v3-blue.svg?style=for-the-badge)](https://www.gnu.org/licenses/agpl-3.0)
[![Python 3.7](https://img.shields.io/badge/python-3.7-green?style=for-the-badge)](https://www.python.org/)

using Apache Atlas as metadata store to proxy the authorization

The service will running at `<host>:5064`

## Installation

follow the step below to setup the service

### Clone

- Clone this repo to machine using `https://github.com/PilotDataPlatform/lineage.git`

### Setup:

> To run the service as dev mode

```
python3 -m pip install -r requirements.txt
python3 app.py
```

> To add new entity in atlas run the curl in the `type.txt` it will add two more entity in atlas:

 - nfs_file
 - nfs_file_processed

## Features:

the service uses the swagger to make the api documents: see the detailed [doc](localhost:6064/v1/api-doc)

### Entity Related API:

 - Add entity to atlas

 - Query entity by the input payload

 - Get entiy by the guid

### Audit Related API:

 - Get audit of entity by guid
