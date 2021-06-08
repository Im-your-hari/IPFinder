from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class MyPage(BoxLayout):
    def __init__(self):
        super().__init__()
        BoxLayout().orientation = 'horizontal'
        self.label = Label(text="_Enter Domain_")
        self.textinput = TextInput(multiline=False)
        self.button = Button(text="Find",on_press=self.find_domain)

        self.add_widget(self.label)
        self.add_widget(self.textinput)
        self.add_widget(self.button)
    
    def find_domain(self,instance):
        self.label.text = "IP"
        self.textinput.text = "This is IP"


class Main(App):
    def build(self):
        return MyPage()
        
if __name__ == '__main__':
    Main().run()