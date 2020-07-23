from tkinter import Toplevel
from tkinter import Text
from tkinter import Frame
from tkinter import Label
from tkinter import StringVar
from tkinter import BOTH,X,LEFT
from childrenClasses.classChildrens import smartclient,RPO
from childrenClasses.panelScroll import PanelInterior

class InformationSmartclientPop(Toplevel):

    contentScreen = Text
    contentScreenRPO = Text
    textContent = StringVar
    lbInfoPresentation = Label
    interiorContent = PanelInterior

    def ConfigPop(self):

        self.title("Conteudo do Smartclient")
        self["bg"] = "#616161"

        self.Positioninthecenter()

        self.minsize(500,400)

        self.bind("<Configure>",self.configureLength)

        self.interiorContent = PanelInterior(self)
        self.interiorContent.pack(fill=BOTH, expand=True)

        self.lbInfoPresentation = Label(self.interiorContent.interior)
        self.lbInfoPresentation["bg"] = "#616161"
        self.lbInfoPresentation["font"] = ("Roboto Black","15")
        self.lbInfoPresentation["fg"] = "white"
        self.lbInfoPresentation["wraplength"] = 400
        self.lbInfoPresentation.pack(fill=X,padx=10,pady=5)

        self.contentScreen = Text(self.interiorContent.interior)
        self.contentScreen["bg"] = "#9E9E9E"
        self.contentScreen["fg"] = "white"
        self.contentScreen["font"] = ("Roboto Black","10")
        self.contentScreen.pack(padx=10,pady=5,fill=BOTH,expand=True)

    def inputContent(self,SmartclientInput=smartclient):

        cContentText = ""

        self.lbInfoPresentation["text"] = "Conteudo filtrado do Smartclient\nLocalizado na: " + SmartclientInput.cdir + "\n"
        
        cContentText += "Principais Chaves: \n\n"
        cContentText += SmartclientInput.cContent

        self.contentScreen.insert(1.0,cContentText)
        self.contentScreen.config(state='disabled')

    def Positioninthecenter(self):

        largura = 500
        altura = 520

        largura_tela = self.winfo_screenwidth()
        altura_tela = self.winfo_screenheight()

        posx = largura_tela/2 - largura/2
        posy = altura_tela/2 - altura/2

        self.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))

    def configureLength(self,event):

        self.lbInfoPresentation["wraplength"] = event.width - 100