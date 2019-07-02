# About

Instructions on how to send SPARQL queries to https://learn.analytics.nasa.gov/ using python. 
This script shows how to use the "subjects" dictionary to find higher order categories for STI keywords.

## Installation

Get correct cert for https://learn.analytics.nasa.gov and covert to correct format:
```bash
curl https://pki.treas.gov/noca_fullpath.p7b > noca_fullpath.p7b
openssl pkcs7 -inform der -in noca_fullpath.p7b -out noca_fullpath.cer
openssl pkcs7 -print_certs -in noca_fullpath.cer -out noca_fullpath.pem
```
(You can also use the `noca_full.pem` provided, assuming it is not outdated.)

Install sparqlwrapper library with option to add custom cert:
```
pip install git+https://github.com/abuonomo/sparqlwrapper#egg=sparqlwrapper
```

Help here:
```
(.venv) ❯ python request_learn.py -h
usage: request_learn.py [-h] u n p c k

Extracts info from SPARQL endpoint using example query.

positional arguments:
  u           endpoint for api
  n           username for endpoint
  p           password for endpoint
  c           pem cert location for this url
  k           the keyword for which to find a broader category

optional arguments:
  -h, --help  show this help message and exit
```

Example usage:
```
python request_learn.py https://learn.analytics.nasa.gov admin password noca_fullpath.pem "Environmental Pollution"
```