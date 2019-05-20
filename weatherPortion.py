import requests

api_address = 'http://api.openweathermap.org/data/2.5/weather?appid=d16e105a8c04388c73b5429744f161d8&q='#New%20York
city = input("City Name: ")

url_current = api_address + city

json_data = requests.get(url_current).json()

print(json_data)

five_day = 'http://api.openweathermap.org/data/2.5/forecast?appid=d16e105a8c04388c73b5429744f161d8&q=New%20York,%20US'

five_day_json = requests.get(five_day).json()

print(five_day_json)


