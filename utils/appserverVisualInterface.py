import kivy
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from utils.classChildrens import appserver, smartclient, RPO

class AppserverVisual(BoxLayout):
    
    appserverInput = appserver

    def __init__(self, app=appserver ,**kwargs):
        super().__init__(**kwargs)

        self.appserverInput = app

        self.injectData()
    
    def injectData(self):
        pass


