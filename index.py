import json
import urllib.request
import urllib.parse
import urllib.error
url ="https://api.data.gov.in/resource/3b01bcb8-0b14-4abf-b6f2-c1bfd384ba69?api-key=579b464db66ec23bdd000001cdd3946e44ce4aad7209ff7b23ac571b&format=json&offset=0&limit=10"

jso = urllib.request.urlopen(url).read()

print("Retrieving data pls wait................")

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
    city_in = input("Enter the name of city: ")
    city_in = str(city_in.capitalize())
    print("You have Entered:",city_in)
    if(city_in not in city_list):
        print("We don't have data for your choice city or There is no station as per Govt data")
        print("\nBut you can try out any of the below listed city for real time AQI:\n")
        print(city_list)
        continue
    else:
        break

for j in range(count):
    if(info["records"][j]["city"]==city_in):
        save = j
        print("\nPollutant Type:", info["records"][j]["pollutant_id"], "||Min value:", info["records"][j]["pollutant_min"], "||Max value:", info["records"][j]["pollutant_max"], "||Avg Pollution:",info["records"][j]["pollutant_avg"])
print("Last Updated: ", info["records"][save]["last_update"])
