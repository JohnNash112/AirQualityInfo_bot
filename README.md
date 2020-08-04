# realTimeAQI.py
# Search for real time AQI of the cities in India
``` This is just a small implementation of web data parshing and working with APIs. ```  
The python program in this project retrieve Real time AQI data from (https://data.gov.in).  
After retrieving the data from the govt. API it loads it and then ask for user to enter a **city** name and if the city name provided by the user is not in the govt database it will give a list of cities one can search for.  
I am using my personal **API** key for retrieving data from the source but for testing out the code one can replace the url in the index.py code with this free **API** url (https://api.data.gov.in/resource/3b01bcb8-0b14-4abf-b6f2-c1bfd384ba69?api-key=579b464db66ec23bdd000001cdd3946e44ce4aad7209ff7b23ac571b&format=json&offset=0&limit=10)  
Before executing the program with the free **API** you must **Comment out line *6 to 16* as these lines in the index.py is used for reading the API_KEY from the .dev file using the OS.**  
## If you want to execute the program with your own API please follow the steps given below:  
1. Install ``` dotenv ``` on your system : execute ***``` pip install python-dotenv ```*** in cmd if you are using windows system.  
2. Create a ``` .env ``` file in your current workspace and in that file write ``` API_KEY = 'YOUR API KEY HERE' ``` and save it.  
3. Now you are all set to get data from (https://data.gov.in) using your own API.  

Sample output:  
Enter the name of city or enter to end: Varanasi  
Pollution Station: Ardhali Bazar, Varanasi - UPPCB  
Pollutant Type: PM2.5 ||Min value: 33 ||Max value: 117 ||Avg Pollution: 64  

Pollution Station: Ardhali Bazar, Varanasi - UPPCB  
Pollutant Type: NO2 ||Min value: 6 ||Max value: 29 ||Avg Pollution: 22  

Pollution Station: Ardhali Bazar, Varanasi - UPPCB  
Pollutant Type: OZONE ||Min value: 7 ||Max value: 17 ||Avg Pollution: 13  

Last Updated:  03-08-2020 03:00:00
Data from: Ministry of Environment and Forests  
## Tearminal Output Sample
![](/Image/sample_Output.jpg)
