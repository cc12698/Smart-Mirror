import requests
import json
import objectpath

class main():
    def currentForcast():
        api_address = 'http://api.openweathermap.org/data/2.5/weather?appid=d16e105a8c04388c73b5429744f161d8&q='#New%20York
        city = input("City Name: ")
        url_current = api_address + city + "&units=imperial"
        json_data = requests.get(url_current).json()

        print("")
        print('current forecast starts')
        print("")
        c = json_data['weather'][0]['main']
        print("the weather today is currently " + c)
        print("")

        z = json_data['main']['temp']
        print("the temp is " + str(z) + " degrees fahrenheit")
        print("")

        tempScale = ["really damn cold", "damn cold", "really cold", "quite cold", "freezing", "cold", "chilly", "cool", "nice", "warm", "quite hot", "damn hot", "clothing on fire"]

        
        if int(z) in range(-999, -4):
            print(tempScale[0])
        elif int(z) in range(-3, 5):
            print(tempScale[1])
        elif int(z) in range(6, 14):
            print(tempScale[2])
        elif int(z) in range(15, 23):
            print(tempScale[3])
        elif int(z) in range(24, 32):
            print(tempScale[4])
        elif int(z) in range(33, 41):
            print(tempScale[5])
        elif int(z) in range(42, 50):
            print(tempScale[6])
        elif int(z) in range(51, 59):
            print(tempScale[7])
        elif int(z) in range(60, 68):
            print(tempScale[8])
        elif int(z) in range(69, 77):
            print(tempScale[9])
        elif int(z) in range(78, 86):
            print(tempScale[10])
        elif int(z) in range(87, 95):
            print(tempScale[11])
        elif int(z) in range(96, 999):
            print(tempScale[12])
            
        print("")
        currWindInt = json_data['wind']['speed']
        print("the wind speed is " + str(currWindInt) + " MPH")
                
        if currWindInt >= 5:
            print("unrowable")
        else:
            print("possibly rowable")
        print("")
        print('curr forecast ends')
        print("")

        

        #<div id="openweathermap-widget-15"></div>
        #<script>window.myWidgetParam ? window.myWidgetParam : window.myWidgetParam = [];
        #window.myWidgetParam.push({id: 15,cityid: '5128581',appid: 'd16e105a8c04388c73b5429744f161d8',units: 'metric',containerid: 'openweathermap-widget-15',  });
        #(function() {var script = document.createElement('script');
        #script.async = true;script.charset = "utf-8";
        #script.src = "//openweathermap.org/themes/openweathermap/assets/vendor/owm/js/weather-widget-generator.js";
        #var s = document.getElementsByTagName('script')[0];s.parentNode.insertBefore(script, s);  })();</scrip

    def fiveDayForcast():
        five_day = 'http://api.openweathermap.org/data/2.5/forecast?appid=d16e105a8c04388c73b5429744f161d8&q=New%20York,%20US&units=imperial'
        five_day_json = requests.get(five_day).json()

        print("")
        print('5 day starts')
        print("")
        
        x = 0

        while x < len(five_day_json['list']):
            print(five_day_json['list'][x]['weather'][0]['main'])
            print(five_day_json['list'][x]['dt_txt'])
            x += 7

        print("")
        print('5 day ends')
        
    currentForcast()
    fiveDayForcast()
