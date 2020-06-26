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

class MainInterface(ScreenManager):

    MainDir = ''
    appserversWidgets = list()
    smartclientsWidgets = list()

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
    def AddWidgetsToResultScreen(self):

        self.appserversWidgets =  self.children[1].getAppserversWidgets()
        self.smartclientsWidgets = self.children[1].getSmartclientsWidgets()

        self.children[0].children[0].ids.ScrollViewResult.clear_widgets()
        
        self.children[0].ConstructResults()

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
