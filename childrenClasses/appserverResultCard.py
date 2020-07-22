import subprocess

from copy import copy
from tkinter import Label
from tkinter import Button
from tkinter.ttk import Frame
from tkinter import Frame as FrameNoStyle
from tkinter import NW,S,W,X,Y,LEFT,RIGHT,BOTH
from childrenClasses.classChildrens import appserver
from childrenClasses.informationAppServerPop import InformationAppServerPop

class AppserverResultCard(Frame):

    appserverData = appserver
    lbMainInformation = Label
    numberOfAppserver = int()
    btOpenLocal = Button
    topInformationFrame = FrameNoStyle
    panelServiceAndPortApp = FrameNoStyle
    btShowContentAppserver = Button
    informatioContentScreen = InformationAppServerPop

    def configureVisualization(self,Appserver=appserver,numberOfAppserver=0):

        self.appserverData = Appserver
        self.numberOfAppserver = numberOfAppserver

        self.configEvents()

        self.createVisualComponents()
    
    def createVisualComponents(self):

        self.createTopInformation()

        linhaAppserverResultCard = FrameNoStyle(self)
        linhaAppserverResultCard["bg"] = "white"
        linhaAppserverResultCard["height"] = 2
        linhaAppserverResultCard.pack(fill=X,pady=5,padx=10)

        self.createServiceInformation()

        self.createPanelMainContent()

    def createPanelMainContent(self):

        self.btShowContentAppserver = Button(self)
        self.btShowContentAppserver["bg"] = "#4285F4"
        self.btShowContentAppserver["font"] = ("Roboto Black","15")
        self.btShowContentAppserver["fg"] = "white"
        self.btShowContentAppserver["text"] = "Abrir conteúdo"
        self.btShowContentAppserver["relief"] = "flat"
        self.btShowContentAppserver["command"] = self.ShowAppserverContentCommand
        self.btShowContentAppserver.pack(fill=X,padx=10,pady=10)

    def ShowAppserverContentCommand(self):

        informatioContentScreen = InformationAppServerPop()
        informatioContentScreen.ConfigPop()
        informatioContentScreen.inputContent(self.appserverData)
        informatioContentScreen.mainloop()


    def createServiceInformation(self):

        self.panelServiceAndPortApp = FrameNoStyle(self)
        if(self.appserverData.lServiceExists):

            self.panelServiceAndPortApp["bg"] = "#34A853"
        else:

            self.panelServiceAndPortApp["bg"] = "#EA4335"
        self.panelServiceAndPortApp.pack(fill=X,pady=10,padx=10)

        lbServiceInfo = Label(self.panelServiceAndPortApp,justify=LEFT)
        lbServiceInfo["font"] = ("Roboto","12")
        lbServiceInfo["fg"] = "white"
        if(self.appserverData.lServiceExists):
            
            lbServiceInfo["text"] = "Serviço encontrado :)\nEncontrado pelo Nome: " + self.appserverData.cNameService + "\nNome de Exibição no ini: " + self.appserverData.cDisplayNameService
            lbServiceInfo["bg"] = "#34A853"
        else:

            lbServiceInfo["text"] = "Tag de serviço do Appserver não está instalado :(\nNome: " + self.appserverData.cNameService + "\nNome de Exibição no ini: " + self.appserverData.cDisplayNameService
            lbServiceInfo["bg"] = "#EA4335"
        lbServiceInfo.pack(padx=5,pady=5,side=LEFT)

        linhaPanelServiceAndPortApp = FrameNoStyle(self.panelServiceAndPortApp)
        linhaPanelServiceAndPortApp["bg"] = "white"
        linhaPanelServiceAndPortApp["width"] = 2.5
        linhaPanelServiceAndPortApp.pack(fill=Y,padx=5,pady=5,side=LEFT,anchor=W)

        lbPort = Label(self.panelServiceAndPortApp,justify=LEFT)
        lbPort["font"] = ("Roboto","20")
        lbPort["fg"] = "white"
        lbPort["text"] = self.appserverData.cport
        if(self.appserverData.lServiceExists):

            lbPort["bg"] = "#34A853"
        else:

            lbPort["bg"] = "#EA4335"
        lbPort.pack(padx=5,pady=5,side=LEFT)

    def createTopInformation(self):

        self.topInformationFrame = FrameNoStyle(self)
        self.topInformationFrame["bg"] = "#9E9E9E"
        self.topInformationFrame.pack(fill=X,padx=10,pady=5)

        self.lbMainInformation = Label(self.topInformationFrame,justify=LEFT)
        self.lbMainInformation["font"] = ("Roboto","20")
        self.lbMainInformation["fg"] = "white"
        self.lbMainInformation["text"] = "# " + str(self.numberOfAppserver) + "\n" + self.appserverData.cdir
        self.lbMainInformation["bg"] = "#9E9E9E"
        self.lbMainInformation.pack(side=LEFT)

        self.btOpenLocal = Button(self.topInformationFrame)
        self.btOpenLocal["bg"] = "#4285F4"
        self.btOpenLocal["font"] = ("Roboto Black","15")
        self.btOpenLocal["fg"] = "white"
        self.btOpenLocal["text"] = "Abrir"
        self.btOpenLocal["relief"] = "flat"
        self.btOpenLocal["height"] = 2
        self.btOpenLocal["command"] = self.OpenLocalAppserver
        self.btOpenLocal.pack(side=RIGHT,anchor=S)

    
    def configEvents(self):

        self.bind("<Configure>",self.configureWidgets)

    def configureWidgets(self,event):

        self.lbMainInformation["wraplength"] = event.width - 80

    def OpenLocalAppserver(self):
       
        subprocess.Popen('explorer ' + self.appserverData.cdir.rstrip('appserver.ini'))