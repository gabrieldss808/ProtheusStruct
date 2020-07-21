from tkinter import X,BOTTOM,LEFT
from tkinter import Frame
from tkinter import Label
from tkinter import Button
from tkinter.ttk import Frame as FrameStyle
from childrenClasses.stylesBackGround import BackgroundsStyle
from childrenClasses.appserverResultCard import AppserverResultCard

class ResultScreen(Frame):

    btHome = Button
    linhaDeSeparacao = Frame
    appservers = list()
    smartclients = list()
    ResultPanel = FrameStyle
    style = BackgroundsStyle
    QtdAppServers = int()
    QtdSmartclients = int()

    def configScreen(self):

        self["bg"] = "#616161"

        self.btHome = Button(self)
        self.btHome["bg"] = "#4285F4"
        self.btHome["text"] = "Inicio"
        self.btHome["font"] = ("Roboto Black","15")
        self.btHome["fg"] = "white"
        self.btHome["relief"] = "flat"
        self.btHome["command"] = self.master.goToHome
        self.btHome.pack(fill=X,padx=40,pady=20)

        self.linhaDeSeparacao = Frame(self)
        self.linhaDeSeparacao["bg"] = "#9E9E9E"
        self.linhaDeSeparacao["height"] = 4
        self.linhaDeSeparacao.pack(fill=X)

        self.style = BackgroundsStyle(self)
        self.style.CreateStyleResultPanel()

        self.ResultPanel = FrameStyle(self,style="BackGroundGreen")
        self.ResultPanel.pack(fill=X,pady=10,padx=20)

    def ShowInformationResult(self):

        self.getData()

        self.createResultPanel()

        self.createAppServersResult()

    def createAppServersResult(self):

        pass

    def getData(self):

        self.appservers = self.master.appservers

        self.QtdAppServers = len(self.appservers)
        
        self.smartclients = self.master.smartclients

        self.QtdSmartclients = len(self.smartclients)

    def clear(self):

        for children in self.ResultPanel.winfo_children():

            children.destroy()
        
    def createResultPanel(self):

        lbPresentation = Label(self.ResultPanel)
        lbPresentation["font"] = ("Roboto Black","20")
        lbPresentation["fg"] = "white"
        lbPresentation["text"] = "Olha o que encontrei :)"
        lbPresentation["bg"] = "#34A853"
        lbPresentation.pack(fill=X,pady=5,padx=5)

        linhaResultPanel = Frame(self.ResultPanel)
        linhaResultPanel["bg"] = "white"
        linhaResultPanel["height"] = 2
        linhaResultPanel.pack(fill=X,pady=5,padx=10)

        StringResultInformation = "Local de busca: " + self.master.DirScanMain + "\n"

        if(self.QtdAppServers > 1 and self.QtdSmartclients > 1):
            StringResultInformation += 'Foram Encontrados: ' + str(self.QtdAppServers) + ' Appservers e ' + str(self.QtdSmartclients) + ' Smartclients\n'
        elif(self.QtdAppServers > 1):
            StringResultInformation += 'Foram Encontrados: ' + str(self.QtdAppServers) + ' Appservers e ' + str(self.QtdSmartclients) + ' Smartclient\n'
        elif(self.QtdSmartclients > 1):
            StringResultInformation += 'Foi Encontrado: ' + str(self.QtdAppServers) + ' Appserver e ' + str(self.QtdSmartclients) + ' Smartclients\n'
        elif(self.QtdAppServers == 0):
            StringResultInformation += 'Foi Encontrado: ' + str(self.QtdAppServers) + ' Appserver e ' + str(self.QtdSmartclients) + ' Smartclients\n'
        elif(self.QtdAppServers == 1):            
            StringResultInformation += 'Foi Encontrado: ' + str(self.QtdAppServers) + ' Appserver\n'

        lbResultInformation = Label(self.ResultPanel,justify=LEFT)
        lbResultInformation["font"] = ("Roboto Black","10")
        lbResultInformation["fg"] = "white"
        lbResultInformation["text"] = StringResultInformation
        lbResultInformation["bg"] = "#34A853"
        lbResultInformation.pack(pady=5,padx=10,side=LEFT)


