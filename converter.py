# програма з двома екранами
# імпортування всіх бібліотек
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen

# клас конвертер для операцій зміну валют
class Converter():
    def __init__(self, usd):
        self.usd = usd

    def hrn_to_usd(self, hrn_value):
        return round(hrn_value/self.usd, 2)

    def usd_to_hrn(self, usd_value):
        return round(usd_value*self.usd, 2)
        
# створення домашнього вікна
class HomeScreen(Screen):
    def __init__(self):
        super().__init__(name="home") #задаємо ім'я
        text = Label(text="Конвертер валют") 
        btn1 = Button(text="Гривні у долари", size_hint = (.9, .3), pos_hint={"center_x":0.5})#створення і розташування кнопок
        btn2 = Button(text="Долари в гривні", size_hint = (.9, .3), pos_hint={"center_x":0.5})
        btn1.on_press = self.next# при натискані зміна екрану
        btn2.on_press = self.next
        layout = BoxLayout(orientation="vertical", spacing=15, padding=30) # уявна вертикальна сітка для розташування об'єктів
        layout.add_widget(text)
        layout.add_widget(btn1)
        layout.add_widget(btn2)
        self.add_widget(layout)#розміщення об'єктів по черзі

    def next(self):
        self.manager.transition.direction = 'left' # об'єкт класу Screen має властивість manager 
        # - це посилання на батьківський клас
        self.manager.current = 'convert_1'
    def next(self):
        self.manager.transition.direction = 'left' # об'єкт класу Screen має властивість manager 
        # - це посилання на батьківський клас
        self.manager.current = 'convert_2'

# клас для створення вікна для конвертації
class ConvertScreen(Screen):
    def __init__(self, name,convert_func):
        super().__init__(name= name)
        self.convert_func = convert_func
        self.amount_input = TextInput(size_hint = (.9 ,None),height = '30 sp', halign = "center", pos_hint = {"center_x":0.5},multiline = False)# створення поля для введення
        self.result_text = Label(text="Результат: 0.0") 
        back_btn = Button(text="Назад", size_hint = (0.9, .3), pos_hint={"center_x":0.5})#кнопка
        back_btn.on_press = self.back#повернення на початковий екран
        self.amount_input.bind(text =self.convert )#привязу'єм дію до кнопки
        layout = BoxLayout(orientation="vertical", spacing=15, padding=30)
        layout.add_widget(self.amount_input)
        layout.add_widget(self.result_text)
        layout.add_widget(back_btn)
        self.add_widget(layout)
# *args-зміння кількість аргументів
    def convert(self,*args):
        try:
            amount = float(self.amount_input.text) #введене число
            result = self.convert_func(amount) #конвертуємо  суму в долари
            self.result_text.text = "Результат: $" + str(result)
        except:
            self.result_text.text = "Введіть число" 
    def back(self):
        self.manager.transition.direction = 'right' # об'єкт класу Screen має властивість manager 
        # - це посилання на батьківський клас
        self.manager.current = 'home'

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(HomeScreen())
        sm.add_widget(ConvertScreen("convert_1", converter.hrn_to_usd))
        sm.add_widget(ConvertScreen("convert_2" , converter.usd_to_hrn))
        
        # буде показано FirstScr, тому що він доданий першим. Це можна змінити ось так:
        # sm.current = 'second'
        return sm

converter = Converter(36.56)
app = MyApp()
app.run()#запуск нашого додатку
