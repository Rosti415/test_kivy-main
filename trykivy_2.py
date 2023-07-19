# додаток з одним віджетом.

from kivy.app import App
# всі віджети знаходяться в окремих модулях усередині kivy.uix:
from kivy.uix.button import Button # кнопка

class MyApp(App):
   # якщо в об'єкті класу App є метод build(),
   # run() виконає цей метод
   # і виведе на екран те, що повертає build
   def build(self):
      btn = Button(text='Це кнопка')
      return btn # повертається завжди віджет!

app = MyApp()
app.run() # буде показано віджет класу Button