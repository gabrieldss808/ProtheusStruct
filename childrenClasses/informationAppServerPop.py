from tkinter import BOTH
from tkinter import StringVar
from tkinter import Text
from tkinter import Tk
from tkinter.ttk import Frame
from childrenClasses.classChildrens import appserver,RPO

class InformationAppServerPop(Tk):

    contentScreen = Text
    textContent = StringVar

    def ConfigPop(self):

        self.title("Conteudo do Appserver")
        self["bg"] = "#616161"

        # self.Positioninthecenter()

        self.contentScreen = Text(self)
        self.contentScreen["bg"] = "#616161"
        self.contentScreen["fg"] = "white"
        self.contentScreen["font"] = ("Roboto Black","10")
        self.contentScreen.pack(padx=10,pady=10,fill=BOTH,expand=True)

    def inputContent(self,AppserverInput=appserver):

        cContentText = "Conteudo filtrado do Appserver\nLocalizado na: " + AppserverInput.cdir + "\n"
        
        cContentText += "Principais Chaves: \n"
        cContentText += AppserverInput.cContent
        
        if(len(AppserverInput.listRpo)>1):
            cContentText += "Informações dos RPOs: \n"
        else:
            cContentText += "Informação do RPO: \n"

        
        for RPO in AppserverInput.listRpo:

            cContentText += "# " + str(AppserverInput.listRpo.index(RPO)) + "\n"

            if(RPO.lEncontrado):

                cContentText += "Foi Localizado em: " + str(RPO.cDir) + "\n"
                cContentText += "Com a ultima alteração feita em: " + RPO.cDataAlteracao + "\n"
                cContentText += "Na seção do Ini: " + RPO.cSection + "\n"
            else:
                cContentText += "Local no ini: " + RPO.cDir + "\n"
                cContentText += "Na seção: " + RPO.cSection + "\n"

        self.contentScreen.insert(1.0,cContentText)
        self.contentScreen.config(state='disabled', relief='flat')

    def Positioninthecenter(self):

        largura = 400
        altura = 200

        largura_tela = self.winfo_screenwidth()
        altura_tela = self.winfo_screenheight()

        posx = largura_tela/2 - largura/2
        posy = altura_tela/2 - altura/2

        self.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))
