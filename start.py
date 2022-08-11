
from yelpapi import YelpAPI

import argparse
from pprint import pprint

import pandas as pd
import io
import requests
import operator

import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("api_key", default="OOPS, please set env var called 'SENDGRID_API_KEY'")

import tkinter

#
# INITIALIZE A NEW GUI WINDOW
#

window = tkinter.Tk()

#
# INITIALIZE SOME USER INTERFACE COMPONENTS
#

# MESSAGE

my_message = tkinter.Message(text="Hi, welcome to the 'Yelp Me Pick' restaurant chooser!\nPlease input your cuisine then your zipcode.", justify='center', width=1000)

# ENTRY (TEXT INPUT) WITH LABEL

my_cuisine = tkinter.Label(text="Input your desired cuisine:")
cuisine_value = tkinter.StringVar()
cuisine_entry = tkinter.Entry(textvariable=cuisine_value)
#
my_zip = tkinter.Label(text="Input your zip code:")
zip_value = tkinter.StringVar()
zip_code_entry = tkinter.Entry(textvariable=zip_value)
#

# BUTTON

def handle_button_click():
    print(zip_code_entry.get())
    print(cuisine_entry.get())
    zip_code = zip_code_entry.get()
    cuisine = cuisine_entry.get()
    with YelpAPI(api_key) as yelp_api:
        search_results = yelp_api.search_query(location = zip_code, term = cuisine, sort_by= 'rating', limit = 5, radius=2000)
    for business in search_results['businesses']:
        address_line1 = business['location']['display_address'][0]
        address_line2 = business['location']['display_address'][1]
        address = address_line1 + ", " + address_line2
        print("Name: " + str(business['name']),"\n" "Address: " + address + "\n" "Rating: " + str(business['rating']))


my_button = tkinter.Button(text="Submit", command=handle_button_click)

#
# BIND THE INDIVIDUAL COMPONENTS TO THE GUI WINDOW (PACK)
# ... THEN LAUNCH THE GUI WINDOW (MAINLOOP)
#

my_message.pack()

cuisine_entry.pack()
zip_code_entry.pack()

my_button.pack()

window.mainloop()
'''
#city = input("Please input your zip code: ")
#cuisine = input('Please input your cuisine: ')
with YelpAPI(api_key) as yelp_api:
    search_results = yelp_api.search_query(location = zip_code, term = cuisine, sort_by= 'rating', limit = 5, radius=2000)

#pprint(search_results)


for business in search_results['businesses']:
    address_line1 = business['location']['display_address'][0]
    address_line2 = business['location']['display_address'][1]
    address = address_line1 + ", " + address_line2
    print("Name: " + str(business['name']),"\n" "Address: " + address + "\n" "Rating: " + str(business['rating']))
'''

















#request_url = "https://api.yelp.com/v3/businesses/matches"
#response = requests.get(request_url)
#print(response.status_code)
#print(response.text)

#client_id = os.getenv("client_id", default="OOPS, please set env var called 'SENDER_ADDRESS'")

#argparser = argparse.ArgumentParser(description='Example Yelp queries using yelpapi. '
#                                                'Visit https://www.yelp.com/developers/v3/manage_app to get the '
#                                                'necessary API keys.')
#argparser.add_argument('api_key', type=str, help='Yelp Fusion API Key')
#args = argparser.parse_args()
#with YelpAPI(api_key) as yelp_api:
#search_results = yelp_api.search_query(location="Austin")
#print(search_results)
#=======
#city = input("Please input your zip code: ")
#cuisine = input("Please input your cuisine: ")
#with YelpAPI(api_key) as yelp_api:
#    search_results = yelp_api.search_query(location=city, term = cuisine, sort_by='rating', limit = 5, radius=1000)

#for business in search_results['business']:
#    print(business['name'], business['rating'])
#>>>>>>> 4034dbf098bf64d80bb014cd00c765aed8431ba7
'''
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


    """
        Example search by centroid and category.
        
        all Yelp categories: https://www.yelp.com/developers/documentation/v3/all_category_list
        centroid: https://www.flickr.com/places/info/2487956
    """
    print('***** 5 bike rentals in San Francisco *****\n{}\n'.format("yelp_api.search_query(categories='bikerentals', "
                                                                     "longitude=-122.4392, latitude=37.7474, limit=5)"))
    response = yelp_api.search_query(categories='bikerentals', longitude=-122.4392, latitude=37.7474, limit=5)
    pprint(response)
    print('\n-------------------------------------------------------------------------\n')


    """
        Example phone search query.
        
        Phone Search API: https://www.yelp.com/developers/documentation/v3/business_search_phone
    """
    print('***** search for business by phone number *****\n{}\n'.format("yelp_api.phone_search_query("
                                                                         "phone='+13193375512')"))
    response = yelp_api.phone_search_query(phone='+13193375512')
    pprint(response)
    print('\n-------------------------------------------------------------------------\n')


    """
        Example business match query with the 'best' type.
        
        Business Match API: https://www.yelp.com/developers/documentation/v3/business_match
    """
    print('***** search for business best match *****\n{}\n'.format("yelp_api.business_match_query(name='Splash Cafe', "
                                                                    "address1='197 Pomeroy Ave', ",
                                                                    "city='Pismo Beach', state='CA', country='US')"))
    response = yelp_api.business_match_query(name='Splash Cafe',
                                             address1='197 Pomeroy Ave',
                                             city='Pismo Beach',
                                             state='CA',
                                             country='US')
    pprint(response)
    print('\n-------------------------------------------------------------------------\n')


    """
        Example business match query with the 'lookup' type.
        
        Business Match API: https://www.yelp.com/developers/documentation/v3/business_match
    """
    print('***** search for business best match *****\n{}\n'.format("yelp_api.business_match_query(name='Splash Cafe', "
                                                                    "address1='197 Pomeroy Ave', ",
                                                                    "city='Pismo Beach', state='CA', country='US')"))
    response = yelp_api.business_match_query(name='Splash Cafe',
                                             address1='197 Pomeroy Ave',
                                             city='Pismo Beach',
                                             state='CA',
                                             country='US')
    pprint(response)
    print('\n-------------------------------------------------------------------------\n')


    """
        Example transaction search query.
        
        Transaction Search API: https://www.yelp.com/developers/documentation/v3/transactions_search
    """
    print("***** businesses in Dallas supporting delivery transactions *****\n{}\n".format("yelp_api.transaction_search_"
                                                                                           "query(transaction_type="
                                                                                           "'delivery', location='dallas, "
                                                                                           "tx')"))
    response = yelp_api.transaction_search_query(transaction_type='delivery', location='dallas, tx')
    pprint(response)
    print('\n-------------------------------------------------------------------------\n')


    """
        Example business query.
        
        Business API: https://www.yelp.com/developers/documentation/v3/business
    """
    print("***** business information for Amy's on 6th St. *****\n{}\n".format("yelp_api.business_query(id='amys-ice-"
                                                                               "creams-austin-3')"))
    response = yelp_api.business_query(id='amys-ice-creams-austin-3')
    pprint(response)
    print('\n-------------------------------------------------------------------------\n')


    """
        Example reviews query.
        
        Reviews API: https://www.yelp.com/developers/documentation/v3/business_reviews
    """
    print("***** selected reviews for Amy's on 6th St. *****\n{}\n".format("yelp_api.reviews_query(id='amys-ice-"
                                                                           "creams-austin-3')"))
    response = yelp_api.reviews_query(id='amys-ice-creams-austin-3')
    pprint(response)
    print('\n-------------------------------------------------------------------------\n')


    """
        Example autocomplete query.
        
        Autocomplete API: https://www.yelp.com/developers/documentation/v3/autocomplete
        centroid: https://www.flickr.com/places/info/2427422
    """
    print("***** autocomplete results for 'Hambur' in Iowa City *****\n{}\n".format("yelp_api.autocomplete_query("
                                                                                    "text='Hambur', longitude=-91.5327, "
                                                                                    "latitude=41.6560)"))
    response = yelp_api.autocomplete_query(text='Hambur', longitude=-91.5327, latitude=41.6560)
    pprint(response)
    print('\n-------------------------------------------------------------------------\n')


    """
        Example event search query.
        
        Event Search API: https://www.yelp.com/developers/documentation/v3/event_search
    """
    print("***** event search result *****\n{}\n".format("yelp_api.event_search_query()"))
    response = yelp_api.event_search_query()
    pprint(response)
    print('\n-------------------------------------------------------------------------\n')


    """
        Example event lookup query.
        
        Event Lookup API: https://www.yelp.com/developers/documentation/v3/event
    """
    print("***** event lookup result using previous search's first event *****\n{}\n".format("yelp_api.event_lookup_"
                                                                                             "query(id=response['events']"
                                                                                             "[0]['id'])"))
    response = yelp_api.event_lookup_query(id=response['events'][0]['id'])
    pprint(response)
    print('\n-------------------------------------------------------------------------\n')


    """
        Example featured event query.
        
        Featured Event API: https://www.yelp.com/developers/documentation/v3/featured_event
    """
    print("***** featured event lookup result for New York City, NY *****\n{}\n".format("yelp_api.featured_event_"
                                                                                        "query(location='New York City, "
                                                                                        "NY')"))
    response = yelp_api.featured_event_query(location='New York City, NY')
    pprint(response)
    print('\n-------------------------------------------------------------------------\n')


    """
        Example erroneous search query.
    """
    print('***** sample erroneous search query *****\n{}\n'.format("yelp_api.search_query(term='ice cream', "
                                                                   "location='austin, tx', sort_by='BAD_SORT')"))
    try:
        # sort can only take on values "best_match", "rating", "review_count", or "distance"
        yelp_api.search_query(term='ice cream', location='austin, tx', sort_by='BAD_SORT')
    except YelpAPI.YelpAPIError as e:
        print(e)
    print('\n-------------------------------------------------------------------------\n')


    """
        Example erroneous business query.
    """
    print('***** sample erroneous business query *****\n{}\n'.format("yelp_api.business_query(id='fake-business')"))
    try:
        yelp_api.business_query(id='fake-business')
    except YelpAPI.YelpAPIError as e:
        print(e)
'''