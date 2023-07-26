from kivy.lang import Builder#підключаємо  в 1 рядку
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRectangleFlatButton
import requests

from config import*

API_URL = "https://api.openweathermap.org/data/2.5/weather?&units=metric&lang=ua" 

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
        data = requests.get(API_URL,api_args)#робимо запит
        response = data.json()#отримуємоп відповідь в JSON
        temp_data = response['main']['temp']
        weather_data = response['weather'][0]['main']
        desc_data = response['weather'][0]['description']
        wind_data = response['wind']['speed']
        self.ids.weather_text.text = desc_data.capitalize()
        self.ids.temp_text.text = "Dg: " + str(round(temp_data))+ '*'
        self.ids.wind_text.text = "Windy: " + str(round(wind_data)) + 'm/s'
        print(response)
        print(temp_data)






class MyWeatherApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"
        Builder.load_file('style.kv')
        return HomeScreen()


MyWeatherApp().run()