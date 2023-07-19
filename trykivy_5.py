# програма з двома екранами
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
# Екран (об'єкт класу Screen) – це віджет типу "макет" (Screen – спадкоємець класу RelativeLayout).
# ScreenManager - це особливий віджет, який робить видимим один із прописаних у ньому екранів.

class FirstScr(Screen):
    def __init__(self, name='first'):
        super().__init__(name=name) # ім'я екрана має передаватися конструктору класу Screen
        btn = Button(text="Перейти на інший екран")
        btn.on_press = self.next
        self.add_widget(btn) # екран - це віджет, на якому можуть створюватись всі інші (нащадки)
    def next(self):
        self.manager.transition.direction = 'left' # об'єкт класу Screen має властивість manager 
        # - це посилання на батьківський клас
        self.manager.current = 'second'

class SecondScr(Screen):
    def __init__(self, name='second'):
        super().__init__(name=name)
        btn = Button(text="Повернися, повернися!")
        btn.on_press = self.next
        self.add_widget(btn)
        
    def next(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'first'

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(FirstScr())
        sm.add_widget(SecondScr())
        # буде показано FirstScr, тому що він доданий першим. Це можна змінити ось так:
        # sm.current = 'second'
        return sm

app = MyApp()
app.run()