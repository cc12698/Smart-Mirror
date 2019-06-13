import requests
import json
import objectpath
import clothingRecommendation

class main(): 
    def tempName(z):
        tempScale = ["really damn cold", "damn cold", "really cold", "quite cold", "freezing", "cold", "chilly", "cool", "nice", "warm", "quite hot", "damn hot", "clothing on fire"]
        clothType = "warm"
        
        if z in range(-999, -4):
            print(tempScale[0])
            clothType = "cold"
        elif z in range(-3, 5):
            print(tempScale[1])
            clothType = "cold"
        elif z in range(6, 14):
            print(tempScale[2])
            clothType = "cold"
        elif z in range(15, 23):
            print(tempScale[3])
            clothType = "cold"
        elif z in range(24, 32):
            print(tempScale[4])
            clothType = "cold"
        elif z in range(33, 41):
            print(tempScale[5])
            clothType = "cold"
        elif z in range(42, 50):
            print(tempScale[6])
            clothType = "cold"
        elif z in range(51, 59):
            print(tempScale[7])
            clothType = "warm"
            #print(clothType)
        elif z in range(60, 68):
            print(tempScale[8])
            clothType = "warm"
        elif z in range(69, 77):
            print(tempScale[9])
            clothType = "warm"
        elif z in range(78, 86):
            print(tempScale[10])
            clothType = "warm"
        elif z in range(87, 95):
            print(tempScale[11])
            clothType = "warm"
        elif z in range(96, 999):
            print(tempScale[12])
            clothType = "warm"

        return clothType

    def currentForcast():
        api_address = 'http://api.openweathermap.org/data/2.5/weather?appid=d16e105a8c04388c73b5429744f161d8&q='#New%20York
        #city = input("City Name: ")
        city = "new york"
        url_current = api_address + city + "&units=imperial"
        json_data = requests.get(url_current).json()
        clothType = ""
        
        print("")
        print('current forecast starts')
        print("")
        c = json_data['weather'][0]['main']
        print("the weather today is currently " + c)
        print("")

        z = json_data['main']['temp']
        print("the temp is " + str(z) + " degrees fahrenheit")
        print("")
        
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
        #return clothType

        return z
        
   
    
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
        
    #def main():
    e = currentForcast()
    z = tempName(e)
    clothingRecommendation.main.clothRec(z)
    fiveDayForcast()

    #main()
        #<div id="openweathermap-widget-15"></div>
        #<script>window.myWidgetParam ? window.myWidgetParam : window.myWidgetParam = [];
        #window.myWidgetParam.push({id: 15,cityid: '5128581',appid: 'd16e105a8c04388c73b5429744f161d8',units: 'metric',containerid: 'openweathermap-widget-15',  });
        #(function() {var script = document.createElement('script');
        #script.async = true;script.charset = "utf-8";
        #script.src = "//openweathermap.org/themes/openweathermap/assets/vendor/owm/js/weather-widget-generator.js";
        #var s = document.getElementsByTagName('script')[0];s.parentNode.insertBefore(script, s);  })();</scrip


