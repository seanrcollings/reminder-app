import kivy
from kivy.app import App
from kivy.uix.button import Label

class HelloKivyApp(App):
    def build(self):
        return Label()

HelloKivyApp().run()