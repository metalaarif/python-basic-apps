#!/usr/bin/python3

from kivy.app import App
#from kivy.uix.label import Label
from kivy.uix.button import Button


class TestApp(App):

    def build(self):
        return Button(text="Hello World!, \nAarif is here coding in python and using Kivy")


if __name__ == '__main__':
    TestApp().run()