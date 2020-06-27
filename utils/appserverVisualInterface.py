import kivy
import subprocess
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from utils.classChildrens import appserver, smartclient, RPO

class AppserverVisual(BoxLayout):
    
    appserverInput = appserver
    NumberPositionView = 0
    ColorServiceStatus = ''

    def __init__(self, app=appserver, NumberPosition=0 ,**kwargs):
        super().__init__(**kwargs)

        self.appserverInput = app

        self.ColorServiceStatus = kivy.utils.get_color_from_hex("#34A853")
        
        self.NumberPositionView = NumberPosition

        self.injectData()
    
    def injectData(self):
        
        self.ids.lbPositionView.text = '# ' + str(self.NumberPositionView)
        self.ids.DirAppServer.text = self.appserverInput.cdir
        
        if(self.appserverInput.lServiceExists):
            self.ids.lbServiceStatus.text = 'Serviço encontrado e rodando ;)\nNome: ' + self.appserverInput.cDisplayNameService
            self.ids.lbServicePort.text = 'Porta: ' + self.appserverInput.cport
            self.ColorServiceStatus = kivy.utils.get_color_from_hex("#34A853")
        else:
            self.ids.lbServiceStatus.text = 'Tag de serviço do Appserver não está instalado :(\nNome: ' + self.appserverInput.cDisplayNameService 
            self.ColorServiceStatus = kivy.utils.get_color_from_hex("#DB4437")

    def ColorServiceStatus(self):
        
        return self.ColorServiceStatus
        
    def BtOpenDir(self):

        subprocess.Popen('explorer ' + self.appserverInput.cdir.rstrip('appserver.ini'))

class ScreenDataAppServerVisual(ScreenManager):
    pass
