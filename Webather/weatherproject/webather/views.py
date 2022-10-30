from django.shortcuts import render

# Create your views here.

import urllib.request
import json
from datetime import datetime

def time_format_for_location(utc_with_tz):
    local_time = datetime.utcfromtimestamp(utc_with_tz)
    return local_time.time()


def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + 
                                        city +'&units=metric&appid=6c411c439c7aaa09347d49dfd145432f').read()
        list_of_data = json.loads(source)
        
        data = {
            "city_name" : str(list_of_data['name']),
            "country_code" : str(list_of_data['sys']['country']),
            "coordinate" : str(list_of_data['coord']['lon']) +' °N'+ ', ' + str(list_of_data['coord']['lat']) + ' °W',
            "temp" : str(list_of_data['main']['temp']) + ' °C',
            "pressure" : str(list_of_data['main']['pressure']) + ' kPa',
            "humidity" : str(list_of_data['main']['humidity']) + ' %',
            "wind_speed" : str(list_of_data['wind']['speed']) + 'KpH',
            "main" : str(list_of_data['weather'][0]['main']),
            "description" : str(list_of_data['weather'][0]['description']),
            "icon" : list_of_data['weather'][0]['icon'],
            "sunrise_time" : time_format_for_location((list_of_data['sys']['sunrise'])),
            "sunset_time" : time_format_for_location((list_of_data['sys']['sunset'])),
            }
        print(data)
    else:
        data = {}
    
    return render(request, "main/index.html", data)