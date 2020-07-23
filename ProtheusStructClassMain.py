import os
import sys

from tkinter import Tk
from tkinter import X,Y,BOTH
from tkinter.ttk import Frame
from childrenClasses.logController import logController
from childrenClasses.HomeScreen import HomeScreen
from childrenClasses.processScreen import ProcessScreen
from childrenClasses.resultScreen import ResultScreen
from childrenClasses.stylesBackGround import BackgroundsStyle

# Classe responsável por Controlar toda a interface e gestão de componentes do Protheus Struct
class ProtheusStruct(Tk):

    log =  logController
    homeScreen = HomeScreen
    processScreen = ProcessScreen
    resultScreen = ResultScreen
    stylesBackGround = BackgroundsStyle
    DirScanMain = ""
    appservers = list()
    smartclients = list()

    def ConfigAppComponents(self):

        self.title("Protheus Struct")

        self["bg"] = "#616161"

        self.iconbitmap(self.resource_path("icon.ico"))

        self.Positioninthecenter()

        self.log = logController()
        self.log.clearLog()
        self.log.consoleLogAdd(self.menssageInit())

        self.stylesBackGround = BackgroundsStyle(self)

        self.configHomeScreen()

        self.stylesBackGround.CreateStyleBackgroundGrayProcess()

        self.processScreen = ProcessScreen(self,style="backGroundGrayPro")
        self.processScreen.configureScreen()

        self.resultScreen = ResultScreen(self)
        self.resultScreen.configScreen()

        self.protocol("WM_DELETE_WINDOW", self.close_window)

    def close_window(self):

        self.destroy()

        sys.exit()

    def menssageInit(self):

        TextIni = ''

        TextIni+="##################################### Protheus Struct ######################################\n"
        TextIni+="### Autor: Gabriel Da Silva Souza                                                        ###\n"
        TextIni+="### Descrição: App que analisa arquivos para filtragem de dados de arquivos da           ###\n"
        TextIni+="### estrutura Protheus                                                                   ###\n"
        TextIni+="### Para detalhes: https://github.com/gabrieldss808/ProtheusStruct/blob/master/README.md ###\n"
        TextIni+="### Versão: 1.0 22/07/2020                                                               ###\n"
        TextIni+="############################################################################################"
        
        return TextIni
    
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

    def process(self,DirScanMain=''):

        self.DirScanMain = DirScanMain

        self.homeScreen.pack_forget()

        self.processScreen.pack(fill=BOTH,padx=100,pady=190,expand=True)
        
        self.processScreen.executeProcess(self.DirScanMain)

    def returnToHome(self):

        self.processScreen.pack_forget()
        self.processScreen.ClearComponent()

        self.homeScreen.pack(fill=BOTH,padx=70,pady=70,expand=True)

    def gotoResult(self):

        self.processScreen.pack_forget()
        self.processScreen.ClearComponent()

        self.resultScreen.pack(fill=BOTH,expand=True)

    def goToHome(self):

        self.resultScreen.pack_forget()

        self.homeScreen.pack(fill=BOTH,padx=70,pady=70,expand=True)
        