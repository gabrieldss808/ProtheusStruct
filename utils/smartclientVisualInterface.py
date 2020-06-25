import kivy
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from utils.classChildrens import appserver, smartclient, RPO

class SmartclientVisual(BoxLayout):

    smartclientInput = smartclient

    def __init__(self, Smart=smartclient, **kwargs):
        super().__init__(**kwargs)

        self.smartclientInput = Smart

        self.injectData()
    
    def injectData(self):
        pass



