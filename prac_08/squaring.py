"""
CP1404Practica l
Kivy GUI program to square a number
Started 10/18/2024
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

__created__ = 'Akram Kasozi'


class SquareNumberApp(App):
    """ SquareNumberApp is a Kivy App for squaring a number """
    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (200, 100)
        self.title = "Square Number"
        self.root = Builder.load_file('squaring.kv')
        return self.root

    def handle_calculate(self, value):
        """ handle calculation (could be button press or other call), output result to label widget """
        try:
            result = int(value) ** 2  # Perform conversion and calculation here
            self.root.ids.output_label.text = str(result)
        except ValueError:
            self.root.ids.output_label.text = "Invalid input"


SquareNumberApp().run()

