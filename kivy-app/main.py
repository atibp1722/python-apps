from kivymd.app import MDApp
from kivymd.uix.boxlayout import BoxLayout, MDBoxLayout
from kivymd.uix.widget import Widget
from kivymd.uix.slider import MDSlider
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen

Window.size = (300, 500)

class Home(Screen):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        slider = MDSlider(min=0, max=10, value=5)
        self.add_widget(slider)

    def left_button(self):
        print("Cancel pressed")

    def right_button(self):
        print("Close pressed")

# class Home(MDBoxLayout):
#     pass

# class Home(MDBoxLayout):
#     pass

# class Home(Widget):
#     pass

# class HomePage(BoxLayout):
#     pass

class MainApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = 'Amber'
        self.theme_cls.theme_style = 'Dark'
        return Home()

MainApp().run()