import os
os.environ["KIVY_NO_CONSOLELOG"] = '1'

import kivy
import threading

from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from scanStruct import scanStruct
from kivy.clock import Clock, mainthread
from time import time, sleep
from utils.appserverVisualInterface import AppserverVisual
from utils.smartclientVisualInterface import SmartclientVisual

class ProcessingScreen(Screen):

    scanStructObject = scanStruct
    appserversWidgets = list()
    smartclientsWidgets = list()
    isCreatingWidgets = bool
    wasCreateWidgets = bool

    def __init__(self, **kw):
        super().__init__(**kw)

    @mainthread
    def ScanStruct(self,cPath=''):

        self.scanStructObject = scanStruct(cPath)

        self.ids.bodyProgress.clear_widgets()

        executeTask = threading.Thread(target=self.executeScanProcess,args=[])
        executeTask.start()

        runStatusProcessTaks = threading.Thread(target=self.runStatusProcess, args=[])
        runStatusProcessTaks.start()    

    def runStatusProcess(self):

        StatusText = ''

        self.ids.progressBarMain.value = 0

        self.ids.lbDescprogressMain.text =   'Procurando Arquivos da Estrutura Protheus...'

        while (self.scanStructObject.isExecuteProcess):
            
            self.ids.progressBarMain.value += 1
            sleep(.5)

            if(self.ids.progressBarMain.value == 10):
                self.ids.progressBarMain.value = 0

        self.ids.progressBarMain.value = 10

        self.ids.lbDescprogressMain.text =   'Criando os widgets...'

        while(self.isCreatingWidgets):

            self.ids.progressBarMain.value += 1
            sleep(.5)

            if(self.ids.progressBarMain.value == 10):
                self.ids.progressBarMain.value = 0

        self.ids.progressBarMain.value = 10

        if(self.wasCreateWidgets):

            self.ids.lbDescprogressMain.text =   'Pronto, agora é só ver os resultados!!'
            self.ids.bodyProgress.add_widget(BtNextScreen())
        else:

            self.ids.lbDescprogressMain.text = 'Sem Resultados!! Tente novamente.'
            self.ids.bodyProgress.add_widget(BtReturn())
        
            
    def executeScanProcess(self):
        
        self.scanStructObject.execute()

        if(self.scanStructObject.wasFoundSomething):
            self.createWidgetsResult()
        else:
            self.isCreatingWidgets = False
            self.wasCreateWidgets = False

    def createWidgetsResult(self):
        
        self.isCreatingWidgets = True

        for appserverObject in self.scanStructObject.getApperservers():

            appserverVisu = AppserverVisual(appserverObject)
            self.appserversWidgets.append(appserverVisu)
        
        for smartclientObject in self.scanStructObject.getSmartclients():

            smartclientVisu = SmartclientVisual(smartclientObject)
            self.smartclientsWidgets.append(smartclientVisu)
        
        self.isCreatingWidgets = False
        self.wasCreateWidgets = True
    
    def getAppserversWidgets(self):

        return self.appserversWidgets   
    
    def getSmartclientsWidgets(self):

        return self.smartclientsWidgets

class BtNextScreen(Button):
    pass

class BtReturn(Button):
    pass