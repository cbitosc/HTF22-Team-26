from flask import Flask, render_template
from tkinter import *
import requests
import json
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/my-link/')
def my_link():
  """ {
    "coord": {
      "lon": 10.99,
      "lat": 44.34
    },
    "weather": [
      {
        "id": 501,
        "main": "Rain",
        "description": "moderate rain",
        "icon": "10d"
      }
    ],
    "base": "stations",
    "main": {
      "temp": 298.48,
      "feels_like": 298.74,
      "temp_min": 297.56,
      "temp_max": 300.05,
      "pressure": 1015,
      "humidity": 64,
      "sea_level": 1015,
      "grnd_level": 933
    },
    "visibility": 10000,
    "wind": {
      "speed": 0.62,
      "deg": 349,
      "gust": 1.18
    },
    "rain": {
      "1h": 3.16
    },
    "clouds": {
      "all": 100
    },
    "dt": 1661870592,
    "sys": {
      "type": 2,
      "id": 2075663,
      "country": "IT",
      "sunrise": 1661834187,
      "sunset": 1661882248
    },
    "timezone": 7200,
    "id": 3163858,
    "name": "Zocca",
    "cod": 200
  }           """


  #frontend
  root = Tk()
  root.geometry("400x400")
  root.title("The Desktop Weather Page! - PS2")
  city_value = StringVar()

  # api to time sensitive using datatime method
  # Universal Time Coordinate to specific time zone
  def time_format_for_location(utc_with_tz):
    local_time = datetime.utcfromtimestamp(utc_with_tz)
    return local_time.time()

  # backend
  def showWeather():
    api_key = "857db2e4eb97ddc8662293bba5812773"
    city_name = city_value.get()

    weather_url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city_name + '&appid=' + api_key
    response = requests.get(weather_url)

    weather_info = response.json()

    tfield.delete('0.0', 'end')  # re-initialize the text field
    if weather_info['cod'] == 200:  # cod has to be 200 to fetch place's details
      kelvin = 273
      temp = int(weather_info['main']['temp'] - kelvin)  # converting default kelvin value to Celsius
      feels_like_temp = int(weather_info['main']['feels_like'] - kelvin)
      pressure = weather_info['main']['pressure']
      humidity = weather_info['main']['humidity']
      wind_speed = weather_info['wind']['speed'] * 3.6
      sunrise = weather_info['sys']['sunrise']
      sunset = weather_info['sys']['sunset']
      timezone = weather_info['timezone']
      cloudy = weather_info['clouds']['all']
      description = weather_info['weather'][0]['description']

      sunrise_time = time_format_for_location(sunrise + timezone)
      sunset_time = time_format_for_location(sunset + timezone)
      weather = f"\nWeather of: {city_name}\nTemperature (Celsius): {temp}°\nFeels like in (Celsius): {feels_like_temp}°\nPressure: {pressure} hPa\nHumidity: {humidity}%\nSunrise at {sunrise_time} and Sunset at {sunset_time}\nCloud: {cloudy}%\nInfo: {description}"
    else:
      weather = f"\n\tWeather for '{city_name}' not found!\n\tKindly Enter valid City Name !!"
    tfield.insert(INSERT, weather)

  # Backend Label

  city_head = Label(root, text='Enter City Name', font='Arial 12 bold').pack(pady=10)  # to generate label heading
  inp_city = Entry(root, textvariable=city_value, width=24, font='Arial 14 bold').pack()
  Button(root, command=showWeather, text="Check Weather", font="Arial 10", bg='lightblue', fg='black',
         activebackground="teal", padx=5, pady=5).pack(pady=20)
  weather_now = Label(root, text="The Weather is:", font='arial 12 bold').pack(pady=10)
  tfield = Text(root, width=46, height=10)
  tfield.pack()
  root.mainloop()

  return "Successfully passed"

if __name__ == '__main__':
  app.run(debug=True)