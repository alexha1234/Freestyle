
from yelpapi import YelpAPI

import argparse
from pprint import pprint

import pandas as pd
import io
import requests


import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("api_key", default="OOPS, please set env var called 'SENDGRID_API_KEY'")


#print(api_key)

city = input("Please input your zip code: ")
cuisine = input('Please input your cuisine: ')
with YelpAPI(api_key) as yelp_api:
    search_results = yelp_api.search_query(location = city, term = cuisine, sort_by='rating', limit = 5, radius=1000)

#pprint(search_results)


for business in search_results['businesses']:
        address_line1 = business['location']['display_address'][0]
        address_line2 = business['location']['display_address'][1]
        address = address_line1 + ", " + address_line2
        print("Name: " + str(business['name']),"\n" "Address: " + address + "\n" "rating: " + str(business['rating']))


