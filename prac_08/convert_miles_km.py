from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.core.window import Window

# Define a constant for miles to kilometers conversion
MILES_TO_KM = 1.60934

class ConvertMilesKmApp(App):
    output_km = StringProperty("0.0 km")

    def build(self):
        Window.size = (300, 200)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_convert(self, miles_text):
        """Handle conversion from miles to kilometers."""
        try:
            miles = float(miles_text)
            kilometers = miles * MILES_TO_KM
            self.output_km = f"{kilometers:.2f} km"
        except ValueError:
            self.output_km = "0.0 km"

    def handle_increment(self, value):
        """Handle incrementing or decrementing the miles value."""
        try:
            miles = int(self.root.ids.input_miles.text)
        except ValueError:
            miles = 0
        miles += value
        self.root.ids.input_miles.text = str(miles)
        self.handle_convert(str(miles))

    def on_text_change(self, miles_text):
        """Handle text change event to update the conversion immediately."""
        self.handle_convert(miles_text)

ConvertMilesKmApp().run()
