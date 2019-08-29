# from kivy.app import App
# from kivy.uix.button import Label
# from functools import partial
 

# class TestApp(App):

#   def build(self):
#     # mybtn = Button(text="Click me to disable", pos=(300,350), size_hint = (.25, .18))
#     # mybtn.bind(on_press=partial(self.disable, mybtn))
#     # mybtn.bind(on_press=partial(self.update, mybtn))
#     # return mybtn
#     return Label()
 
# TestApp().run()

import kivy

from kivy.app import App
from kivy.uix.button import Label

class HelloKivyApp(App):
    def build(self):
        return Label()

HelloKivyApp().run()