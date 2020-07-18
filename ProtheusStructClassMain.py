import os
import sys

from tkinter import Tk
from tkinter import X,Y,BOTH
from tkinter.ttk import Frame
from childrenClasses.logController import logController
from childrenClasses.HomeScreen import HomeScreen
from childrenClasses.stylesBackGround import BackgroundsStyle

class ProtheusStruct(Tk):

    log =  logController
    homeScreen = HomeScreen
    stylesBackGround = BackgroundsStyle

    def ConfigAppComponents(self):

        self.title("Protheus Struct")

        self["bg"] = "#616161"

        self.iconbitmap(self.resource_path("icon.ico"))

        self.Positioninthecenter()

        self.log = logController()
        self.log.clearLog()

        self.stylesBackGround = BackgroundsStyle(self)

        self.configHomeScreen()
    
    def configHomeScreen(self):

        self.stylesBackGround.CreateStyleBackgroundGray()
        
        self.homeScreen = HomeScreen(self,style="backGroundGray")
        self.homeScreen.pack(fill=BOTH,padx=70,pady=70,expand=True)
        self.homeScreen.ConfigAppComponents()

    def resource_path(self,relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath("./icons")

        return os.path.join(base_path, relative_path)

    def Positioninthecenter(self):

        largura = 650
        altura = 600

        largura_tela = self.winfo_screenwidth()
        altura_tela = self.winfo_screenheight()

        posx = largura_tela/2 - largura/2
        posy = altura_tela/2 - altura/2

        self.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))
        self.minsize(650,600)

