from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
import time

class Reminder(BoxLayout):
  def __init__(self, name, deadline, **kwargs):
    super(Reminder, self).__init__(**kwargs)
    name = Property('test')
    # self.deadline = deadline + time.time()    
  

class ReminderGrid(BoxLayout):
  def __init__(self, **kwargs):
    super(ReminderGrid, self).__init__(**kwargs)
    self.reminders = [Reminder(name='Reminder 1', deadline=12), Reminder(name='Reminder 2', deadline=13)]

    
class ReminderApp(App):
  def build(self):
    return Reminder(name='Test', deadline=12)

ReminderApp().run()