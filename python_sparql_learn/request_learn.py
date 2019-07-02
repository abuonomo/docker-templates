"""
author: Anthony Buonomo
contact: anthony.r.buonomo@nasa.gov

Example of how to send SPARQL requests to NASA dictionaries in python.
"""

import argparse
import logging
import json

from SPARQLWrapper import SPARQLWrapper, JSON

logging.basicConfig(level=logging.INFO)
LOG = logging.getLogger(__name__)
LOG.setLevel(logging.INFO)

QUERY_STR = """
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

    SELECT ?predicate ?ol
    WHERE {
      ?subject ?predicate ?object .
      ?subject skos:prefLabel "VAR" .
      ?object skos:prefLabel ?ol .
    }
"""

def main(url, username, password, cafile, keyword):
    LOG.info(f'Extractin from url {url}.')
    dictionary = 'subjects'
    dictionary_query = f'{dictionary}/query'
    sparql = SPARQLWrapper(f"{url}/{dictionary_query}",  cafile=cafile)
    sparql.setCredentials('admin', 'password')
    query_str = QUERY_STR.replace('VAR', keyword)
    LOG.info(f'Sending query: \n {query_str}')
    sparql.setQuery(query_str)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    try:
        pred = results["results"]["bindings"][0]["predicate"]["value"]
        obj_label = results["results"]["bindings"][0]["ol"]["value"]
    except IndexError as e:
        LOG.exception(f"""\"{keyword}\"" not in \"{dictionary}\". This query requires an exact string match.""")
    LOG.info(f'{keyword} -- {pred} -- {obj_label}.')
    LOG.info('Done.')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = 'Extracts info from SPARQL endpoint using example query.')
    parser.add_argument('u', help='endpoint for api', default='https://learn.analytics.nasa.gov')
    parser.add_argument('n', help='username for endpoint',)
    parser.add_argument('p', help='password for endpoint',)
    parser.add_argument('c', help='pem cert location for this url', default='noca_fullpath.pem')
    parser.add_argument('k', help='the keyword for which to find a broader category', default='STI')
    args = parser.parse_args()
    main(args.u, args.n, args.p, args.c, args.k)

