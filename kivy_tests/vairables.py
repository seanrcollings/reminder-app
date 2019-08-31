from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty


class StationTest(Screen):
    pass


class ScreenManagement(ScreenManager):
    pass


class TestApp(App):
    abcd = StringProperty('test')

    def build(self):
        return ScreenManagement()


TestApp().run()