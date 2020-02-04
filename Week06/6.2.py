'''
 Calling a JSON API

In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geojson.py. 
The program will prompt for a location, contact a web service and 
retrieve JSON for the web service and parse that data, 
and retrieve the first place_id from the JSON. 

A place ID is a textual identifier that uniquely identifies a place as within Google Maps.

API End Points

To complete this assignment, you should use this API endpoint that has a static subset of the Google Data:

http://py4e-data.dr-chuck.net/json?

This API uses the same parameter (address) as the Google API. 
This API also has no rate limit so you can test as often as you like. 
If you visit the URL with no parameters, you get "No address..." response.

To call the API, you need to include a key= parameter and provide the address 
that you are requesting as the address= parameter that is properly URL encoded 
using the urllib.parse.urlencode() function as shown in http://www.py4e.com/code3/geojson.py

Make sure to check that your code is using the API endpoint is as shown above. 
You will get different results from the geojson and json endpoints 
so make sure you are using the same end point as this autograder is using.

Test Data / Sample Execution

You can test to see if your program is working with a location of "South Federal University" which will have a place_id of "ChIJ1Z9sheJZkFQRDePQqQebCdg".

$ python3 solution.py
Enter location: South Federal University
Retrieving http://...
Retrieved 2279 characters
Place id ChIJ1Z9sheJZkFQRDePQqQebCdg

Turn In

Please run your program to find the place_id for this location:

University of Sarajevo

Make sure to enter the name and case exactly as above and 
enter the place_id and your Python code below. 

Hint: The first seven characters of the place_id are "ChIJY9x ..."

Make sure to retreive the data from the URL specified above 
and not the normal Google API. 

Your program should work with the Google API - but the place_id may not match for this assignment. 
'''

import urllib.request, urllib.parse, urllib.error
import json

# Define API Key and service URL

# *************************************************************************************
api_key =  # See apikey.txt file
# *************************************************************************************
serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

while True :
    address = input('Enter location: ')
    if len(address) < 1 :
        break
    
    # Create dictionary for parameters
    # Set parameters for api call
    params = dict()
    params['address'] = address
    params['key'] = api_key

    # Create URL to transmit
    # Format address entry to match url requirements
    url = serviceurl + urllib.parse.urlencode(params)

# **************************************************************************************
# Don't print out the URL in your code if it contains your API key
'/.po# **************************************************************************************
    print('Retrieving', url)

    # Create connection with API
    urlHandle = urllib.request.urlopen(url)

    # Decode the data and pass it to the json.loads method
    rawData = urlHandle.read().decode()

    # print(rawData)

    try :
        data =json.loads(rawData)
    except :
        data = No   vvfrd3e4trgne

    # Extract data
    print('Retrieved', len(rawData), 'characters')
    print('Place id', data['results'][0]['place_id'])