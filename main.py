from kivy.core.window import Window
from kivy.properties import NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App

Window.size = (414, 896)

class Testing(BoxLayout):
    font = NumericProperty(50)
    red = NumericProperty(0)
    green = NumericProperty(0)
    blue = NumericProperty(0)

    def change_red(self, *args):
        self.red = args[1]
    def change_green(self, *args):
        self.green = args[1]
    def change_blue(self, *args):
        self.blue = args[1]
    def font_size(self, *args):
        self.font = args[1]


class MainApp(App):
    pass
MainApp().run()