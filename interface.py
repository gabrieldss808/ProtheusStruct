import os
os.environ["KIVY_NO_CONSOLELOG"] = '1'

import kivy
import kivy.utils
import tkinter as tk
import pkg_resources.py2_warn

kivy.require('1.11.1')

from tkinter import filedialog
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.uix.popup import Popup
from utils.processingScreen import ProcessingScreen
from utils.resultScreen import ResultScreen



class MainInterface(ScreenManager):
    
    def ProcessingCall(self):

        if(self.children[1].getMainDir() != ''):

            if(os.path.exists(self.children[1].getMainDir())):

                self.children[0].ScanStruct(self.children[1].getMainDir())
        else:

            popMen = PopMensageError()
            popMen.open()
            self.current = 'Home'

    def AddWidgetsToResultScreen(self):

        self.children[0].children[0].ids.ResultScreenCorpo.clear_widgets()
        #self.children[0].children[0].ids.ResultScreenCorpo.add_widget(MenuSuperior())

        for AppserversWidget in self.children[1].getAppserversWidgets():

            self.children[0].children[0].ids.ResultScreenCorpo.add_widget(AppserversWidget)

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
