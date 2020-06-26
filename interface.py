import os
os.environ["KIVY_NO_CONSOLELOG"] = '1'

import kivy
import kivy.utils
import tkinter as tk
import pkg_resources.py2_warn
import threading

kivy.require('1.11.1')

from tkinter import filedialog
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock, mainthread
from kivy.uix.widget import Widget
from kivy.uix.popup import Popup
from time import time, sleep
from utils.processingScreen import ProcessingScreen
from utils.resultScreen import ResultScreen
from utils.resultScreen import MainDirVisualization



class MainInterface(ScreenManager):

    MainDir = ''
    
    def ProcessingCall(self):


        self.MainDir = self.children[1].getMainDir()

        if(self.children[1].getMainDir() != ''):

            if(os.path.exists(self.MainDir)):

                self.children[0].ScanStruct(self.children[1].getMainDir())
        else:

            popMen = PopMensageError()
            popMen.open()
            self.current = 'Home'

    @mainthread
    def AddWidgetsToResultScreen(self, Widgest):

        executeTask = threading.Thread(target=self.TaskAddWidgetsToResultScreen,args=[])
        executeTask.start()

    def TaskAddWidgetsToResultScreen(self,):

        self.children[0].children[0].ids.ResultScreenCorpo.clear_widgets()

        sleep(1)

        self.children[0].children[0].ids.ResultScreenCorpo.add_widget(MainDirVisualization(self.MainDir,len(self.children[1].getAppserversWidgets()),len(self.children[1].getSmartclientsWidgets())))

        sleep(1.5)

        for AppserversWidget in self.children[1].getAppserversWidgets():

            self.children[0].children[0].ids.ResultScreenCorpo.add_widget(AppserversWidget)
            sleep(1)
    
class PopMensageError(Popup):
    pass

class Home(Screen):
    
    mainDir = ''

    def btDirOpen(self):

        ConfigFileDialog = tk.Tk()
        ConfigFileDialog.withdraw()

        self.mainDir = filedialog.askdirectory()

        self.ids.inputDir.text = self.mainDir
    
    def getMainDir(self):

        return self.mainDir
