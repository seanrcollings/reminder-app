from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.recycleview import RecycleView
import time

class Reminder(GridLayout):
  def __init__(self, name, deadline, **kwargs):
    super(Reminder, self).__init__(**kwargs)
    self.name = name
    self.deadline = deadline + time.time()

  def past_time(self):
    if time.time() >= self.deadline:
      return True
    else:
      return False

class RemindersGrid(RecycleView):
  pass

class ReminderApp(Screen):
  def __init__(self, **kwargs):
    super(ReminderApp, self).__init__(**kwargs)
    self.reminders = [Reminder('Reminder 1', 2331), Reminder('Reminder 2', 1231)]

  def render_reminders(self):
    self.recycle.data = []
    for reminder in self.reminders:
      self.recycle.data.append({'text': reminder.name, 'value': reminder.deadline - time.time()})

  def remove_reminder(self):
    print('hello')
    

  def add_reminder(self, name, time):
    self.reminders.append(Reminder(name, time))

class MyApp(App):
  def build(self):
    return ReminderApp()

if __name__ == '__main__':
    MyApp().run()