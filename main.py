from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.animation import Animation
from kivy.clock import Clock
import socket as s


class MyPage(BoxLayout):
    def __init__(self):
        super().__init__()
        self.orientation = 'vertical'
        self.padding = 50
        self.spacing = 20
        self.label = Label(text="{Mr.X}")
        self.textinput = TextInput(multiline=False,hint_text="Enter Domain...")
        
        
        self.button = Button(text="Find",background_color=(0,0,1,1),on_press=self.find_domain)

        self.add_widget(self.label)
        self.add_widget(self.textinput)
        self.add_widget(self.button)
    
    def find_domain(self,instance):
        #self.label.text = "IP"
        #self.textinput.text = "This is IP"
        a = self.textinput.text
        try:
            self.textinput.text = s.gethostbyname(a)
        except Exception:
            self.textinput.text = ""
            self.textinput.hint_text = "Invalid Domain...! Please try another..."
        


class IPxFOUND(App):
    def build(self):
        Window.clearcolor = (0,0,255,1)
        self.icon = 'icon.png'
        #self.presplash = 'icon.png'
        
        return MyPage()
        
if __name__ == '__main__':
    IPxFOUND().run()