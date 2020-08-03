import json
import urllib.request
import urllib.parse
import urllib.error
import dotenv
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Accessing variables.
api_key = os.getenv('API_KEY')
print("Retrieving data pls wait................")

url = "https://api.data.gov.in/resource/3b01bcb8-0b14-4abf-b6f2-c1bfd384ba69?api-key="+str(api_key)+"&format=json&offset=0&limit=10000"

jso = urllib.request.urlopen(url).read()
print("\nRetrieved", len(jso), "characters")

info = json.loads(jso)
#print(info)
count = len(info["records"])
print("Number of records available right now:", count)
city_list = []
for i in range(count):
    if(info["records"][i]["city"] not in city_list):
        city_list.append(info["records"][i]["city"])
#print(city_list)

while(True):
    city_in = input("Enter the name of city or press enter key to end: ")
    city_in = str(city_in.title())
    #print("You have Entered:",city_in)
    if(len(city_in)<1):
        print("Thanks for the search. Good Bye, have a nice day :)")
        break
    elif(city_in not in city_list):
        print("We don't have data for your choice city or There is no station as per Govt data")
        print("\nBut you can try out any of the below listed city for real time AQI:\n")
        print(sorted(city_list))
        continue
    elif(city_in in city_list):
        for j in range(count):
            if(info["records"][j]["city"]==city_in):
                save = j
                print("Pollution Station:",info["records"][j]["station"])
                print("Pollutant Type:", info["records"][j]["pollutant_id"], "||Min value:", info["records"][j]["pollutant_min"], "||Max value:", info["records"][j]["pollutant_max"], "||Avg Pollution:",info["records"][j]["pollutant_avg"],"\n")
        print("\nLast Updated: ", info["records"][save]["last_update"])
        print("Data from:",info["org"][0])
        continue
