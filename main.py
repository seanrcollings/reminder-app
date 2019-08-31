from kivy.app import App; from kivy.uix.boxlayout import BoxLayout; from kivy.uix.label import Label; from kivy.uix.gridlayout import GridLayout; from kivy.uix.button import Button
from kivy.uix.recycleview import RecycleView; from kivy.uix.recycleboxlayout import RecycleBoxLayout; from kivy.uix.textinput import TextInput; from kivy.properties import StringProperty
import time; import threading 

class Reminder(GridLayout):
  def __init__(self, name, deadline, controller, **kwargs):
    super(Reminder, self).__init__(**kwargs)
    self.rows = 1
    self.cols = 3
    self.size_hint_y = None
    self.height = 50
    self.name = name
    self.controller = controller
    self.deadline = str(float(deadline) + time.time())
    self.add_widget(Label(text=self.name))
    self.add_widget(Label(text=self.deadline))
    self.add_widget(Button(text='X', on_press = lambda *args: self.controller.delete_reminder(self)))

    # thread = threading.Thread(target=self.update_distance_to_deadline)
    # thread.start()
    
  def past_time(self):
    if time.time() >= self.deadline:
      return True
    else:
      return False

  def update_distance_to_deadline(self):
    while True:
      time.sleep(1)
      if not self.past_time():
        self.distance_to_deadline.set(str(round(self.deadline - time.time())))
      else:
        self.distance_to_deadline.set('0')

class RV(RecycleView):
  def __init__(self, **kwargs):
    super(RV, self).__init__(**kwargs)
    self.viewclass = 'Reminder'
    self.data = [{'text': 'text', 'value': 121}]

class RBL(RecycleBoxLayout):
  def __init__(self, **kwargs):
    super(RBL, self).__init__(**kwargs)
    self.default_size = None, dp(56)
    self.default_size_hint = 1, None
    self.size_hint_y = None
    self.height = self.minimum_height
    self.orientation = 'vertical'

class NewReminder(GridLayout):
  def __init__(self, controller, **kwargs):
    super(NewReminder, self).__init__(**kwargs)
    self.cols=3
    self.rows=2
    self.add_widget(Label(text='Reminder Name'))
    self.add_widget(Label(text='Time in seconds'))
    self.add_widget(Label(text=''))
    self.name = TextInput(multiline=False)
    self.time = TextInput(multiline=False)
    self.add_widget(self.name)
    self.add_widget(self.time)
    self.add_widget(Button(text='Add Reminder', on_press= lambda *args: controller.add_reminder(self.name.text, self.time.text)))


class ReminderBox(BoxLayout):
  def __init__(self, **kwargs):
    super(ReminderBox, self).__init__(**kwargs)
    self.orientation='vertical'
    self.reminders = [Reminder('test', 1, self)]
    self.add_widget(NewReminder(size_hint_y=None, height=70, controller=self))
    # self.render_reminders()
    self.add_widget(RV())

  def render_reminders(self): # Hacky way to render the reminders, change later (RecycleView?)
    for reminder in self.reminders:
      try:
        self.add_widget(reminder)
      except Exception:
        pass

  def add_reminder(self, name, time):
    self.reminders.append(Reminder(name, time, self))
    self.render_reminders()

  def delete_reminder(self, reminder, *args):
    self.reminders.remove(reminder)
    self.remove_widget(reminder)

class ReminderGrid(GridLayout):
  def __init__(self, **kwargs):
    super(ReminderGrid, self).__init__(**kwargs)
    self.rows = 2
    self.add_widget(Label(text='Reminder App', size_hint_y=None, height=100, font_size=35, color=(1,1,0,1)))
    self.add_widget(ReminderBox())
    

class RemindersApp(App):
  def build(self):
    return ReminderGrid()

if __name__ == '__main__':
  RemindersApp().run()