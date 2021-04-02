import requests


open_api_key = "c0ddfd7d322622bad27a6236bcb3e793"
city = input("Enter the city you like to check the forecast: ")   #Ask the user what city he like to check the forecast
url = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+open_api_key+"&units=imperial" #will call the result from OpenWeather API with a Farenheight temperature 


request = requests.get(url)		#Calling the site to provide the information of the city
json = request.json()	#Will format the request to JSON

#I had to get format the json result to a JSON Formatter site so I can analyze the data properly as it's returning a hard to read data when printing the JSON result that we get from the API.

city = json.get("name")	
country = json.get("sys").get("country")
forecast = json.get("weather")[0].get("description")
print ("The weather forecast today in", city, "city,", country, "is:", forecast )

min_temp = json.get("main").get("temp_min")
max_temp = json.get("main").get("temp_max")
print ("The current temperature is", min_temp, "to", max_temp)

'''
The result will be like the one below:
Enter the city you like to check the forecast: manila
The weather forecast today in Manila city, PH is: few clouds
The current temperature is 82 to 82.99
'''
