from tkinter import Toplevel
from tkinter import Text
from tkinter import Frame
from tkinter import Label
from tkinter import StringVar
from tkinter import BOTH,X,LEFT
from childrenClasses.classChildrens import appserver,RPO
from childrenClasses.panelScroll import PanelInterior

class InformationAppServerPop(Toplevel):

    contentScreen = Text
    contentScreenRPO = Text
    textContent = StringVar
    lbInfoPresentation = Label
    interiorContent = PanelInterior

    def ConfigPop(self):

        self.title("Conteudo do Appserver")
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
        self.lbInfoPresentation.pack(fill=X,padx=10,pady=5)

        self.contentScreen = Text(self.interiorContent.interior)
        self.contentScreen["bg"] = "#9E9E9E"
        self.contentScreen["fg"] = "white"
        self.contentScreen["font"] = ("Roboto Black","10")
        self.contentScreen.pack(padx=10,pady=5,fill=BOTH,expand=True)

        self.protocol("WM_DELETE_WINDOW", self.close_window)

    def close_window(self):

        self.destroy()


    def inputContent(self,AppserverInput=appserver):

        cContentText = ""

        self.lbInfoPresentation["text"] = "Conteudo filtrado do Appserver\nLocalizado na: " + AppserverInput.cdir + "\n"
        
        cContentText += "Principais Chaves: \n\n"
        cContentText += AppserverInput.cContent

        cContentText += "-----------------------------------------\n"
        
        if(len(AppserverInput.listRpo)>1):
            cContentText += "Informações dos RPOs: \n\n"
        else:
            cContentText += "Informações do RPO: \n\n"

        for RPO in AppserverInput.listRpo:

            cContentText += "# " + str(AppserverInput.listRpo.index(RPO)+1) + "\n"

            if(RPO.lEncontrado):

                cContentText += "Foi Localizado em: " + str(RPO.cDir) + "\n"
                cContentText += "Com a ultima alteração feita em: " + RPO.cDataAlteracao + "\n"
                cContentText += "Na seção do Ini: " + RPO.cSection + "\n\n"
            else:
                
                cContentText += "Local no ini: " + str(RPO.cDir) + "\n"
                cContentText += "Na seção: " + RPO.cSection + "\n\n"

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