from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.recycleview import RecycleView
import time

class ReminderGrid(BoxLayout):
  pass

class RemindersRecycle(RecycleView):
  def __init__(self, **kwargs):
    super(RemindersRecycle, self).__init__(**kwargs)
    self.data = [{'text': 'test', 'value': 1}]

class ReminderApp(App):
  
  def build(self):
    return ReminderGrid()

ReminderApp().run()