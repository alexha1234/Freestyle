from yelpapi import YelpAPI
import argparse
from pprint import pprint

from yelpapi import YelpAPI
try:
    yelp_api = YelpAPI(api_key)
    search_results = yelp_api.search_query(args)
finally:
    yelp_api.close()
    
argparser = argparse.ArgumentParser(description='Example Yelp queries using yelpapi')
argparser.add_argument('api_key', type=str, help='Yelp Fusion API Key')
args = argparser.parse_args()

with YelpAPI(args.api_key) as yelp_api:
    """
        Example search by location text and term. 
        
        Search API: https://www.yelp.com/developers/documentation/v3/business_search
    """
    print('***** 5 best rated ice cream places in Austin, TX *****\n{}\n'.format("yelp_api.search_query(term='ice cream', "
                                                                                 "location='austin, tx', sort_by='rating', "
                                                                                 "limit=5)"))
    response = yelp_api.search_query(term='ice cream', location='austin, tx', sort_by='rating', limit=5)
    pprint(response)
    print('\n-------------------------------------------------------------------------\n')