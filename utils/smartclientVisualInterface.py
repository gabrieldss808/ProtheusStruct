import kivy
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from utils.classChildrens import appserver, smartclient, RPO

class SmartclientVisual(BoxLayout):

    smartclientInput = smartclient
    NumberPositionView = 0

    def __init__(self, Smart=smartclient,NumberPosition=0, **kwargs):
        super().__init__(**kwargs)

        self.smartclientInput = Smart
        self.NumberPositionView = NumberPosition

        self.injectData()
    
    def injectData(self):
        pass



