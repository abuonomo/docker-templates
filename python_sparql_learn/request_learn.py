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


def main(url, dictionary, username, password, cafile, outfile):
    LOG.info(f'Extractin from url {url}.')
    dictionary_query = f'{dictionary}/query'
    sparql = SPARQLWrapper(f"{url}/{dictionary_query}",  cafile=cafile)
    sparql.setCredentials('admin', 'password')
    query_str = """
        SELECT ?subject ?predicate ?object
        WHERE {
          ?subject ?predicate ?object
        }
        LIMIT 25
    """
    LOG.info(f'Sending query: \n {query_str}')
    sparql.setQuery(query_str)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    LOG.info(f'Writing results to {outfile}.')
    with open(outfile, 'w') as f0:
        json.dump(results, f0)
    LOG.info('Done.')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = 'Extracts info from SPARQL endpoint using example query.')
    parser.add_argument('u', help='endpoint for api', default='https://learn.analytics.nasa.gov')
    parser.add_argument('d', help='the dictionary to query', default='STI')
    parser.add_argument('n', help='username for endpoint',)
    parser.add_argument('p', help='password for endpoint',)
    parser.add_argument('c', help='pem cert location for this url', default='noca_fullpath.pem')
    parser.add_argument('o', help='output file for query')
    args = parser.parse_args()
    main(args.u, args.d, args.n, args.p, args.c, args.o)

