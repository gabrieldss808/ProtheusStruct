from copy import copy
from tkinter import Frame
from tkinter import Label
from tkinter import Button
from tkinter import X,BOTTOM,LEFT,BOTH,NW,N
from tkinter.ttk import Frame as FrameStyle
from childrenClasses.stylesBackGround import BackgroundsStyle
from childrenClasses.appserverResultCard import AppserverResultCard
from childrenClasses.smartclientResultCard import SmartclientResultCard
from childrenClasses.appserverPanel import AppserverPanel
from childrenClasses.smartclientPanel import SmartclientPanel

class ResultScreen(Frame):

    btHome = Button
    linhaDeSeparacao = Frame
    appservers = list()
    smartclients = list()
    ResultPanel = FrameStyle
    style = BackgroundsStyle
    QtdAppServers = int()
    QtdSmartclients = int()
    btAppserverShowPanel = Button
    btSmartclientsShowPanel = Button
    isAppserversPanelShow = bool()
    isSmartclientsPanelShow = bool()
    appserverPanel = AppserverPanel
    smartclientPanel = SmartclientPanel
    numberOfStyles = int()
    organizationFrame = Frame

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

        self.numberOfStyles = 0

        self.ResultPanel = FrameStyle(self,style="BackGroundGreen")
        self.ResultPanel.pack(fill=X,pady=10,padx=20)

        #Feito para organizar os botões btAppserverShowPanel btSmartclientsShowPanel na esquerda da tela
        self.organizationFrame = Frame(self)
        self.organizationFrame["bg"] = "#616161"
        self.organizationFrame.pack(anchor=NW,fill=X)

        self.btAppserverShowPanel = Button(self.organizationFrame)
        self.btAppserverShowPanel["bg"] = "#4285F4"
        self.btAppserverShowPanel["font"] = ("Roboto Black","8")
        self.btAppserverShowPanel["fg"] = "white"
        self.btAppserverShowPanel["relief"] = "flat"
        self.btAppserverShowPanel["command"] = self.ShowAppServerPanel

        self.btSmartclientsShowPanel = Button(self.organizationFrame)
        self.btSmartclientsShowPanel["bg"] = "#4285F4"
        self.btSmartclientsShowPanel["font"] = ("Roboto Black","8")
        self.btSmartclientsShowPanel["fg"] = "white"
        self.btSmartclientsShowPanel["relief"] = "flat"
        self.btSmartclientsShowPanel["command"] = self.ShowSmartclientPanel

        self.appserverPanel = AppserverPanel(self)
        self.smartclientPanel = SmartclientPanel(self)

        self.isAppserversPanelShow = False
        self.isSmartclientsPanelShow = False

    def ShowInformationResult(self):

        self.getData()

        self.createResultPanel()

        self.createAppServersResult()

        self.createSmartclientResult()

    def createSmartclientResult(self):

        self.btSmartclientsShowPanel["text"] = "Smartclient("+ str(self.QtdSmartclients) +") >"
        self.btSmartclientsShowPanel.pack(padx=10,pady=5,side=LEFT)

        if(self.isSmartclientsPanelShow):

            self.smartclientPanel.pack_forget()
            self.isSmartclientsPanelShow = False
            self.btSmartclientsShowPanel["text"] = "Smartclient("+ str(self.QtdSmartclients) +") >"
        
        for smartclient in self.smartclients:

            self.style.CreateStyleCard(self.numberOfStyles)

            smartclientCard = copy(SmartclientResultCard(self.smartclientPanel.interior,style="backGroundGrayApp"+str(self.numberOfStyles)))
            smartclientCard.configureVisualization(smartclient,self.smartclients.index(smartclient)+1)
            smartclientCard.pack(fill=X,padx=10,pady=10)

            self.numberOfStyles += 1

    def createAppServersResult(self):

        
        self.btAppserverShowPanel["text"] = "Appservers("+ str(self.QtdAppServers) +") >"
        self.btAppserverShowPanel.pack(padx=10,pady=5,side=LEFT)
        
        if(self.isAppserversPanelShow):

            self.appserverPanel.pack_forget()
            self.isAppserversPanelShow = False
            self.btAppserverShowPanel["text"] = "Appservers("+ str(self.QtdAppServers) +") >"

        for appserver in self.appservers:
            
            self.style.CreateStyleCard(self.numberOfStyles)

            appserverCard = copy(AppserverResultCard(self.appserverPanel.interior,style="backGroundGrayApp"+str(self.numberOfStyles)))
            appserverCard.configureVisualization(appserver,self.appservers.index(appserver)+1)
            appserverCard.pack(fill=X,padx=10,pady=10)

            self.numberOfStyles += 1

    def ShowSmartclientPanel(self):

        if(self.isSmartclientsPanelShow):

            self.smartclientPanel.pack_forget()
            self.isSmartclientsPanelShow = False
            self.btSmartclientsShowPanel["text"] = "Smartclient("+ str(self.QtdSmartclients) +") >"
        else:
            
            if(self.isAppserversPanelShow):

                self.appserverPanel.pack_forget()
                self.isAppserversPanelShow = False
                self.btAppserverShowPanel["text"] = "Appservers("+ str(self.QtdAppServers) +") >"
                
            self.smartclientPanel.pack(fill=BOTH,expand=True)
            self.isSmartclientsPanelShow = True
            self.btSmartclientsShowPanel["text"] = "Smartclient("+ str(self.QtdSmartclients) +") <"


    def ShowAppServerPanel(self):

        if(self.isAppserversPanelShow):

            self.appserverPanel.pack_forget()
            self.isAppserversPanelShow = False
            self.btAppserverShowPanel["text"] = "Appservers("+ str(self.QtdAppServers) +") >"
        else:

            if(self.isSmartclientsPanelShow):

                self.smartclientPanel.pack_forget()
                self.isSmartclientsPanelShow = False
                self.btSmartclientsShowPanel["text"] = "Smartclient("+ str(self.QtdSmartclients) +") >"

            self.appserverPanel.pack(fill=BOTH,expand=True)
            self.isAppserversPanelShow = True
            self.btAppserverShowPanel["text"] = "Appservers("+ str(self.QtdAppServers) +") <"

        
    def getData(self):

        self.appservers = self.master.appservers

        self.QtdAppServers = len(self.appservers)
        
        self.smartclients = self.master.smartclients

        self.QtdSmartclients = len(self.smartclients)

    def clear(self):

        for children in self.ResultPanel.winfo_children():

            children.destroy()
        
        for children in self.appserverPanel.interior.winfo_children():

            children.destroy()
        
        for children in self.smartclientPanel.interior.winfo_children():

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


