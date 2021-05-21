from django.shortcuts import render
from django.http import Http404, HttpResponse
from .models import Weather
from django.contrib import messages
# Create your views here.



def index(request):
    return render(request, "index2.html")

def weather(request):
    return render(request, "weather-ui.html")
    pass

def search(request):
    print(request.GET)
    return render(request, "weather-ui.html")
    pass

def fillweather(request):
    from geopy.geocoders import Nominatim
    
    from bs4 import BeautifulSoup
    import requests
    import re
    geolocator = Nominatim(user_agent="weathers")
    weath = Weather()
    try:
        location = geolocator.geocode(request.GET['city'])
        weath.city =  location.address
#        print(location.address)
#Flatiron Building, 175, 5th Avenue, Flatiron, New York, NYC, New York, ...
        lat = str(location.latitude)
        longi = str(location.longitude)
#        print(lat, longi)
        url = "https://weather.com/en-IN/weather/today/l/"+lat+","+longi+"?par=google"
        html = requests.get(url).content

# getting raw data
        soup = BeautifulSoup(html, 'html.parser')
        timest = soup.find('div', attrs={'class': 'CurrentConditions--timestamp--1SWy5'}).text
        weath.temp = soup.find('span', attrs={'class': 'CurrentConditions--tempValue--3KcTQ'}).text
        weath.weather = soup.find('div', attrs={'class': 'CurrentConditions--phraseValue--2xXSr'}).text
        #str = soup.find('span', attrs={'class': 'CurrentConditions--tempValue--3KcTQ'}).text
        weath.temp = re.findall('[1-9]+', str(weath.temp))
        weath.temp = weath.temp[0]
#        print("Temperature is", weath.temp)
#        print("Temperature is", timest)
#        print("Temperature is", weath.weather)
# print("Temperature is", temptime)

        table = soup.find('ul', attrs={'class': 'WeatherTable--columns--3q5Nx WeatherTable--wide--YogM9'})
        table_rows = table.find_all_next('li', attrs={'class': 'Column--column--2bRa6'})
        weath2 = Weather()
         
        tempe = []
        time = []
        weather_type_img = []
        for tr in table_rows:
            head = tr.find_all('h3')
            title = tr.find_all('title')
            temp_time = tr.find_all('span', attrs={'data-testid' : 'TemperatureValue'})
            preci = tr.find_all('span', attrs={'class': 'Column--precip--2H5Iw'})
            clean = re.compile('<.*?>')
#            print(re.sub(clean, '',  str(head[0])))
            w = re.sub(clean, '',  str(title[0]))
            weather_type_img.append(w.lower())
            t = re.sub(clean, '',  str(title[0]))
            t = re.findall('[1-9]+', str(temp_time[0]))
            tempe.append(re.sub(clean, '',  str(t[0])))
#            print(re.sub(clean, '',  str(preci[0])))
            tempotime = re.sub(clean, '',  str(head[0]))
            time.append(tempotime.lower())

    # reg = re.findall('[a-zA-Z]', str(td[0]))
    # print(reg)
            row = [i.text for i in head]
            if tempotime == 'Overnight':
                break
#        print(tempe)

        temperatures = weath2.temp2 = tempe
#        print(time)
        test_keys = ["Rash", "Kil", "Varsha"]
        test_values = [1, 4, 5]
  
# Printing original keys-value lists
#        print ("Original key list is : " + str(time))
#        print ("Original value list is : " + str(temperatures))
  
# using naive method
# to convert lists to dictionary
        res = {}
        for key in time:
            for value in temperatures:
                res[key] = value
                temperatures.remove(value)
                break  
        result = res.items()
# Printing resultant dictionary 
#        print ("Resultant dictionary is : " +  str(res))
        
#snippet for Celcius to Fahrenheit
        # Collect input from the user  
        celsius = int(weath.temp)
  
        # calculate temperature in Fahrenheit  
        fahrenheit = (celsius * 1.8) + 32  
        #
        celsius = str(celsius)
        print(weather_type_img)
        fahrenheit = str(fahrenheit)  
        ###################FOR#SVG#Dynamicity#############################
        def svg_founder(weathering):
            import re

            mylist = ['clear night','sunny', 'day rain', 'rain', 'fog moon', 'cloudy', 'cloudy night', 'cloudy night haze', 'wind', 'tornado', 'thunder', 'thermameter', 'sunset', 'sun sandstorm', 'storm', 'snow', 'snow flake', 'snow cloud', 'shower', 'rainbow', 'partly sunny cloudy', 'night storm', 'night snow', 'night sandstorm', 'night rain', 'moon rised', 'moon light', 'heavy rain', 'foggy day', 'thunderstorm', 'showers', 'thunderstorms']
            #print(type(weath.weather))
            #f = "rain shower"
            #print(f)
            mat = weathering.lower()
            #mat = 'rain'
            mat_l =  mat.split(" ")
        #mat_l.append(mat.split(" "))
        #print(mat_l)
            m = []
            ray_final = ''
            for i in range(len(mat_l)):
                pattern = ".*"+mat_l[i]
                r = re.compile(pattern)
            #r = re.compile(".*cloudy")
                newlist = list(filter(r.match, mylist)) # Read Note
                m.append(newlist)
                if mat_l[i] in newlist:
                    ray_final = mat_l[i]
    #print(newlist)
            if len(m) > 2 and ray_final == '':
                for i in range(len(m)):
                    for j in range(len(m[i])):
                        if m[i] == m[-1]:
                            break
                        elif m[i][j] in m[i+1]:
                            ray_final = m[i][j]
                            break
                        pass
        
                    pass
            elif ray_final == '':
                for i in range(len(m)):
                #print(m[i][0])
                    if mat_l[0] in m:
                        ray_final = mat_l[0]
            
                    else:
                        ch = m[i][0].split(" ")
                        if mat_l[0] in ch:
                            ray_final = m[i][0]
                pass
#['day rain', 'fog moon', 'cloudy', 'cloudy night', 'cloudy night haze', 'wind', 'tornado', 'thunder', 'thermameter', 'sunset', 'sun sandstorm', 'storm', 'snow', 'snow flake', 'snow cloud', 'shower', 'rainbow', 'partly sunny cloudy', 'night storm', 'night snow', 'night sandstorm', 'night rain', 'moon rised', 'moon light', 'heavy rain', 'foggy day', ]
            return ray_final+".svg"
        weath_path = []
        weath_path.append(svg_founder(weath.weather))
        for m in weather_type_img:
            weath_path.append(svg_founder(m))
            print(weath_path, m)
            pass
        print(weath_path)
        a = 100
    except:
        return render(request, '404.html')
    return render(request, "weather-ui.html",{'weath':weath,'result':result, 'celsius':celsius, 'fahrenheit':fahrenheit, 'weath_path': weath_path, 'a':a})
    pass
#['day rain.svg', 'fog moon.svg', 'cloudy.svg', 'cloudy night.svg', 'cloudy night haze.svg', 'wind.svg', 'tornado.svg', 'thunder.svg', 'thermameter.svg', 'sunset.svg', 'sun sandstorm.svg', 'storm.svg', 'snow.svg', 'snow flake.svg', 'snow cloud.svg', 'shower.svg', 'rainbow.svg', 'partly sunny cloudy.svg', 'night storm.svg', 'night snow.svg', 'night sandstorm.svg', 'night rain.svg', 'moon rised.svg', 'moon light.svg', 'heavy rain', 'foggy day']



'''
from geopy.geocoders import Nominatim
from bs4 import BeautifulSoup
import requests
import re
geolocator = Nominatim(user_agent="weather")
location = geolocator.geocode("474003")
print(location.address)
#Flatiron Building, 175, 5th Avenue, Flatiron, New York, NYC, New York, ...
lat = str(location.latitude)
longi = str(location.longitude)
print(type(lat), longi)


#extraction Link --->>   https://weather.com/en-IN/weather/today/l/26.22,78.18?par=google
''''''
extraction tags
<div class="CurrentConditions--timestamp--1SWy5">As of 22:14 IST</div>
<span data-testid="TemperatureValue" class="CurrentConditions--tempValue--3KcTQ">28°</span>
<div data-testid="wxPhrase" class="CurrentConditions--phraseValue--2xXSr">Clear</div>
<title>Clear Night</title>
<span data-testid="TemperatureValue">33°</span>
<title>Partly Cloudy</title>
<span class="Column--precip--2H5Iw">--</span>
<span class="Ellipsis--ellipsis--lfjoB" style="-webkit-line-clamp:2">Morning</span>
<span class="Ellipsis--ellipsis--lfjoB" style="-webkit-line-clamp:2">Afternoon</span>

''''''

# creating url and requests instance
url = "https://weather.com/en-IN/weather/today/l/26.22,78.18?par=google"
html = requests.get(url).content

# getting raw data
soup = BeautifulSoup(html, 'html.parser')
timest = soup.find('div', attrs={'class': 'CurrentConditions--timestamp--1SWy5'}).text
temp = soup.find('span', attrs={'class': 'CurrentConditions--tempValue--3KcTQ'}).text
weahter = soup.find('div', attrs={'class': 'CurrentConditions--phraseValue--2xXSr'}).text

##########################################3

temptime = soup.find('span', attrs={'data-testid': 'TemperatureValue'}).text
# temp = soup.find('span', attrs={'class': 'CurrentConditions--tempValue--3KcTQ'}).text
# temp = soup.find('span', attrs={'class': 'CurrentConditions--tempValue--3KcTQ'}).text
# str = soup.find('span', attrs={'class': 'CurrentConditions--tempValue--3KcTQ'}).text

print("Temperature is", temp)
print("Temperature is", timest)
print("Temperature is", weahter)
# print("Temperature is", temptime)

table = soup.find('ul', attrs={'class': 'WeatherTable--columns--3q5Nx WeatherTable--wide--YogM9'})
table_rows = table.find_all_next('li', attrs={'class': 'Column--column--2bRa6'})
# print(table_rows)
for tr in table_rows:
    head = tr.find_all('h3')
    title = tr.find_all('title')
    temp_time = tr.find_all('span', attrs={'data-testid' : 'TemperatureValue'})
    preci = tr.find_all('span', attrs={'class': 'Column--precip--2H5Iw'})
    clean = re.compile('<.*?>')
    print(re.sub(clean, '',  str(head[0])))
    print(re.sub(clean, '',  str(title[0])))
    print(re.sub(clean, '',  str(temp_time[0])))
    print(re.sub(clean, '',  str(preci[0])))
    # reg = re.findall('[a-zA-Z]', str(td[0]))
    # print(reg)
    row = [i.text for i in head]
    
'''