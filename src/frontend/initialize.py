from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

print("HELLO WORLD...?")


class PyfyApp(App):
    def build(self):
        shortButton = Button(text="Find and order short positions",
                             size_hint=(.25, .18),
                             pos=(50,50))
        longButton = Button(text="Find and order short positions",
                            size_hint=(.25, .18),
                            pos=(100,50),
                            # on_press= self.helloWorld()
                            )
        longButton.bind(on_press=self.helloWorld)
        boxlayout = BoxLayout()
        boxlayout.add_widget(shortButton)
        boxlayout.add_widget(longButton)
        return boxlayout

    def helloWorld(self):
        print("Hello world")


# click this button to make some smart short trades

# click this button to make the long trades that make money when gaining...

# click this button to show current positions in alpaca ...


# todo: make this less whorish lol

# PyfyApp().run()
