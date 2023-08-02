from kivy.lang import Builder#підключаємо  в 1 рядку
from kivymd.uix.card import MDCard
from kivy.properties import StringProperty
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRectangleFlatButton
import requests

from config import*
import datetime

API_URL = "https://api.openweathermap.org/data/2.5/weather?&units=metric&lang=ua" 
FORECAST_URL = "https://api.openweathermap.org/data/2.5/forecast?&cnt=7&units=metric&lang=ua"

class WeatherCard(MDCard):
    def __init__(self, date,temp, weather_text, wind_speed, rain, rain_pop = None):
            super().__init__()
            self.ids.date_text.text = str(date)
            self.ids.weather_text.text = weather_text.capitalize()
            self.ids.temp_text.text = "Dg: " + str(round(temp))+ '°C'
            if rain_pop:
                self.ids.rain_pop_text.text = f"Ймовірність опадів: {round(rain_pop)*100}%"
            self.ids.rain_text.text = f"Кількість опадів: {rain} mm"
            self.ids.wind_speed_text.text = f"Швидкість вітру: {wind_speed} м/c"


        


class HomeScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(name = 'homes_creen', **kwargs)

    def city_request(self):
        #print(self.ids.city.text)
        #отримуємо введення
        city = self.ids.city.text.lower().strip()
        api_args = {#формує словник аргумкетів для API запиту
            'q': city,
            'appid': API_KEY
        }
        #поточна погода
        data = requests.get(API_URL,api_args)#робимо запит
        response = data.json()#отримуємоп відповідь в JSON
        print(response)
        temp_data = response['main']['temp']
        weather_data = response['weather'][0]['main']
        desc_data = response['weather'][0]['description']
        wind_data = response['wind']['speed']
        if 'rain' in response:
            rain_data = response['rain']['1h']
        else:
            rain_data = 0
        new_card = WeatherCard("Зараз",temp_data,desc_data,wind_data,rain_data)
        self.ids.weather_carousel.add_widget(new_card)
      

        #прогноз погоди
        data = requests.get(FORECAST_URL,api_args)#робимо запит
        response = data.json()#отримуємоп відповідь в JSON
        for period in response['list']:
            date_data = period['dt']
            date_obj = datetime.datetime.fromtimestamp(date_data)
            date = date_obj.strftime('%H:%M\n%A,%d %b')#функція для перетворення в зручний формат дати
            temp_data = period['main']['temp']
            weather_data = period['weather'][0]['main']
            desc_data = period['weather'][0]['description']
            wind_data = period['wind']['speed']
            if 'rain' in period:
                rain_data = period['rain']['3h']
            else:
                rain_data = 0
            rain_pop = period['pop']
            new_card = WeatherCard(date,temp_data,desc_data,wind_data,rain_data,rain_pop)
            self.ids.weather_carousel.add_widget(new_card)





class MyWeatherApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"
        Builder.load_file('style.kv')
        return HomeScreen()


app = MyWeatherApp()
app.run()