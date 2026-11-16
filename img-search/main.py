from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

import wikipedia
import requests

# load kivy file
Builder.load_file('loadscreen.kv')

class LoadScreen(Screen):
    def search_image(self):
        # get user text
        user = self.ids.input.text
        # wikipedia page matching user text
        page = wikipedia.page(user)
        # url of 1st image found in [age]
        image_link = page.images[0]
        # download image
        req = requests.get(image_link)
        # save the image
        img_dir = "image.png"
        with open(img_dir, 'wb') as f:
            f.write(req.content)
        # point to saved image
        self.ids.img.source = img_dir
        # image display on screen
        self.ids.img.reload()

class RootWidget(ScreenManager):
    pass

class ImageSearch(App):
    # return root widget
    def build(self):
        return RootWidget()
        
# initialize kivy app
ImageSearch().run()