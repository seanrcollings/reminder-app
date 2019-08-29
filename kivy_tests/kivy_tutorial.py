from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.properties import StringProperty
import random

class Widgets(Widget):
  random_number = StringProperty()
  def __init__(self, **kwargs):
    super(Widgets, self).__init__(**kwargs)
    self.random_number = str(random.randint(1, 100))

  def change_text(self):
    self.random_number = str(random.randint(1, 100))


class SimpleKivyApp(App):
  def build(self):
    return Widgets()

if __name__ == "__main__":
  SimpleKivyApp().run()
