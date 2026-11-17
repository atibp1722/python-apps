from kivymd.app import MDApp
from kivymd.uix.boxlayout import BoxLayout, MDBoxLayout
from kivymd.uix.widget import Widget
from kivymd.uix.slider import MDSlider
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen

# size of the app screen
Window.size = (300, 500)

# home class for <Home> in kivy file
class Home(Screen):
    # define constructtir and initiaite parent class
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # create slider with range 0-10
        slider = MDSlider(min=0, max=10, value=5)
        # add slider to screen
        self.add_widget(slider)
    # trigger when right button pressed
    def left_button(self):
        print("Cancel pressed")
    # trigger when left button pressed
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

# define main class and inherit from MDApp
class MainApp(MDApp):
    # method call when app starts
    def build(self):
        self.theme_cls.primary_palette = 'Amber'
        self.theme_cls.theme_style = 'Dark'
        return Home()

MainApp().run()