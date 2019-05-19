import requests

api_address = 'http://api.openweathermap.org/data/2.5/weather?appid=d16e105a8c04388c73b5429744f161d8&q='#New%20York
city = input("City Name: ")

url = api_address + city

json_data = requests.get(url).json()

print(json_data)
