import kivy
import subprocess
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from utils.classChildrens import appserver, smartclient, RPO

class AppserverVisual(BoxLayout):
    
    appserverInput = appserver
    NumberPositionView = 0

    def __init__(self, app=appserver, NumberPosition=0 ,**kwargs):
        super().__init__(**kwargs)

        self.appserverInput = app
        
        self.NumberPositionView = NumberPosition

        self.injectData()
    
    def injectData(self):
        
        self.ids.lbPositionView.text = '# ' + str(self.NumberPositionView)
        self.ids.DirAppServer.text = self.appserverInput.cdir


    def BtOpenDir(self):

        subprocess.Popen('explorer ' + self.appserverInput.cdir.rstrip('appserver.ini'))

class ScreenDataAppServerVisual(ScreenManager):
    pass
