import subprocess

from tkinter import Label
from tkinter import Button
from tkinter.ttk import Frame
from tkinter import Frame as FrameNoStyle
from tkinter import NW,S,W,X,Y,LEFT,RIGHT,BOTH
from childrenClasses.classChildrens import smartclient
from childrenClasses.informationSmartclientPop import InformationSmartclientPop

class SmartclientResultCard(Frame):

    smartclientData = smartclient
    numberOfSmartclient = int()
    lbMainInformation = Label
    btShowContentSmartclient = Button
    informatioContentScreen = InformationSmartclientPop

    def configureVisualization(self,Smartclient=smartclient,numberOfSmartclient=0):

        self.smartclientData = Smartclient
        self.numberOfSmartclient = numberOfSmartclient
        
        self.configEvents()

        self.createVisualComponents()

    def createVisualComponents(self):

        self.createTopInformation()

        linhaSmartclientResultCard = FrameNoStyle(self)
        linhaSmartclientResultCard["bg"] = "white"
        linhaSmartclientResultCard["height"] = 2
        linhaSmartclientResultCard.pack(fill=X,pady=5,padx=10)

        self.createPanelMainContent()

    def createPanelMainContent(self):

        self.btShowContentSmartclient = Button(self)
        self.btShowContentSmartclient["bg"] = "#4285F4"
        self.btShowContentSmartclient["font"] = ("Roboto Black","15")
        self.btShowContentSmartclient["fg"] = "white"
        self.btShowContentSmartclient["text"] = "Abrir conteúdo"
        self.btShowContentSmartclient["relief"] = "flat"
        self.btShowContentSmartclient["command"] = self.ShowSmartclientContentCommand
        self.btShowContentSmartclient.pack(fill=X,padx=10,pady=10)

    def ShowSmartclientContentCommand(self):
        
        self.informatioContentScreen = InformationSmartclientPop()
        self.informatioContentScreen.ConfigPop()
        self.informatioContentScreen.inputContent(self.smartclientData)
        self.informatioContentScreen.mainloop()

    def createTopInformation(self):

        self.topInformationFrame = FrameNoStyle(self)
        self.topInformationFrame["bg"] = "#9E9E9E"
        self.topInformationFrame.pack(fill=X,padx=10,pady=5)

        self.lbMainInformation = Label(self.topInformationFrame,justify=LEFT)
        self.lbMainInformation["font"] = ("Roboto","20")
        self.lbMainInformation["fg"] = "white"
        self.lbMainInformation["text"] = "# " + str(self.numberOfSmartclient) + "\n" + self.smartclientData.cdir
        self.lbMainInformation["bg"] = "#9E9E9E"
        self.lbMainInformation.pack(side=LEFT)

        self.btOpenLocal = Button(self.topInformationFrame)
        self.btOpenLocal["bg"] = "#4285F4"
        self.btOpenLocal["font"] = ("Roboto Black","15")
        self.btOpenLocal["fg"] = "white"
        self.btOpenLocal["text"] = "Abrir"
        self.btOpenLocal["relief"] = "flat"
        self.btOpenLocal["height"] = 2
        self.btOpenLocal["command"] = self.OpenLocalSmartclient
        self.btOpenLocal.pack(side=RIGHT,anchor=S)

    def configEvents(self):

        self.bind("<Configure>",self.configureWidgets)

    def configureWidgets(self,event):

        self.lbMainInformation["wraplength"] = event.width - 80

    def OpenLocalSmartclient(self):
       
        subprocess.Popen('explorer ' + self.smartclientData.cdir.rstrip('smartclient.ini'))