from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.clipboard import Clipboard

import time
import webbrowser
import os

# load from kivy file
Builder.load_file('loadscreen.kv')

class RootWidget(ScreenManager):
    pass

# class to handle web cam
class CamScreen(Screen):
    # turn on camera
    def start(self):
        self.ids.camera.play = True
        # stop camera button toggle
        self.ids.btn.text = 'Stop Camera'
        # refresh
        self.ids.camera.texture = self.ids.camera.texture
    # capture and save the web camera picture
    def capture(self):
        # directory to save image
        os.makedirs("webcam-capture/img", exist_ok=True)
        # create a time stamp and export picture as png
        curr_time = time.strftime("%d%m%Y_%H%M%S")
        self.file_path = f'webcam-capture/img/{curr_time}.png'
        # see image screen
        self.ids.camera.export_to_png(self.file_path)
        self.manager.current = 'img_screen'
        # assign file path to widget
        self.manager.current_screen.ids.img.source = self.file_path
    # stop camera
    def stop(self):
        self.ids.camera.play = False
        # start camera button toggle
        self.ids.btn.text = 'Start Camera'
        self.ids.camera.texture = None

# class to view captured image
class CapturedImgScreen(Screen):
    url = ""
    # create link to view image
    def create_link(self):
        # get saved image path
        path = App.get_running_app().root.ids.cam_screen.file_path
        # convert to absolute path
        abs_path = os.path.abs_path.replace("\\", "/")
        # create URI
        self.url = "file:///" + abs_path
        # show inside a kivy widget
        self.ids.lbl.text = self.url
    # copy link to clipboard
    def copy_link(self):
        try:
            Clipboard.copy(self.url)
        # error message
        except AttributeError as err:
            self.ids.lbl.text = 'No link was created!'
    # open link on the web browser
    def open_link(self):
        try:
            webbrowser.open(self.url)
        # error message
        except:
            self.ids.lbl.text = 'Image link not found!'

# inherit from kivy
class CaptureApp(App):
    # initialize UI
    def build(self):
        return RootWidget()

# start application
CaptureApp().run()