from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout

class Reminder(BoxLayout):
  def __init__(self, **kwargs):
    super(Reminder, self).__init__(**kwargs)
    self.name = 'test'
    self.time = 'test'    
  

class ReminderGrid(BoxLayout):
  def __init__(self, **kwargs):
    super(ReminderGrid, self).__init__(**kwargs)
    self.reminders = [{'text': 'test', 'value': 1}, {'text': 'test2', 'value': 1}]
    self.recycle.data = self.reminders

class ReminderApp(App):
  def build(self):
    return ReminderGrid()

ReminderApp().run()