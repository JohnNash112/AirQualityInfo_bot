# realTimeAQI.py
# Search for real time AQI of the cities in India
``` This is just a small implementation of web data parshing and working with APIs. ```  
The python program in this project retrieve Real time AQI data from ``` https://data.gov.in ```.  
After retrieving the data from the govt. API it loads it and then ask for user to enter a **city** name and if the city name provided by the user is not in the govt database it will give a list of cities one can search for.  
I am using my personal **API** key for retrieving data from the source but for testing out the code one can replace the url in the index.py code with this free **API** url *``` https://api.data.gov.in/resource/3b01bcb8-0b14-4abf-b6f2-c1bfd384ba69?api-key=579b464db66ec23bdd000001cdd3946e44ce4aad7209ff7b23ac571b&format=json&offset=0&limit=10 ```*  
Before executing the program with the free **API** you must comment out line **6 to 16** as these lines in the index.py is used for reading the API_KEY from the .dev file using the OS.  
Sample output:  
You have Entered: Amaravati

Pollutant Type: PM2.5 ||Min value: 2 ||Max value: 17 ||Avg Pollution: 7

Pollutant Type: PM10 ||Min value: 6 ||Max value: 24 ||Avg Pollution: 13

Pollutant Type: NO2 ||Min value: 4 ||Max value: 12 ||Avg Pollution: 7

Pollutant Type: NH3 ||Min value: 2 ||Max value: 2 ||Avg Pollution: 2

Pollutant Type: SO2 ||Min value: 8 ||Max value: 19 ||Avg Pollution: 14

Pollutant Type: CO ||Min value: 22 ||Max value: 32 ||Avg Pollution: 25

Pollutant Type: OZONE ||Min value: 14 ||Max value: 46 ||Avg Pollution: 36
Last Updated:  02-08-2020 08:00:00  
![](Image\sample_Output.jpg)
