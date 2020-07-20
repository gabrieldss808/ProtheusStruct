import os
import sys

from tkinter import Tk
from tkinter import PhotoImage
from tkinter import Label
from tkinter import Button
from tkinter.ttk import Frame
from tkinter import filedialog
from tkinter import X,LEFT,RIGHT,BOTH
from childrenClasses.imageHome import imageHome
from childrenClasses.FolderHomeFrame import FolderHomeFrame
from childrenClasses.stylesBackGround import BackgroundsStyle

class HomeScreen(Frame):

    IconHome = PhotoImage
    imgHome = imageHome
    lbDirLocal = Label
    btSearchLocal = Button
    frameDir = FolderHomeFrame
    DirScanMain = ""
    btProcess = Button

    def ConfigAppComponents(self):
        
        self.IconHome = PhotoImage(file=self.resource_path("logo.png"))

        self.imgHome = imageHome(self,image=self.IconHome)
        self.imgHome["bg"] = '#9E9E9E'
        self.imgHome.pack(pady=40)


        self.frameDir = FolderHomeFrame(self)
        self.frameDir["bg"] = "#616161"
        self.frameDir.bind("<Configure>",self.configureScreen)
        self.frameDir.pack(fill=X,padx=40,pady=10)

        self.lbDirLocal = Label(self.frameDir)
        self.lbDirLocal["font"] = "Roboto 20"
        self.lbDirLocal["fg"] = "white"
        self.lbDirLocal["text"] = "Select Folder >"
        self.lbDirLocal["bg"] = "#616161"
        self.lbDirLocal.pack(side=LEFT,fill=X)

        imgBtDir = PhotoImage(file=self.resource_path("dirIcon.png"))

        self.btSearchLocal = Button(self.frameDir)
        self.btSearchLocal["command"] = self.getPath
        self.btSearchLocal["font"] = ("Roboto Black","12")
        self.btSearchLocal["text"] = "Folder"
        self.btSearchLocal["fg"] = "white"
        self.btSearchLocal["bg"] = "#4285F4"
        self.btSearchLocal["relief"] = "flat"
        self.btSearchLocal.pack(side=RIGHT,fill=BOTH)

        self.btProcess = Button(self)
        self.btProcess["command"] = self.process        
        self.btProcess["font"] = ("Roboto","25")
        self.btProcess["text"] ="Process >"
        self.btProcess["fg"] = "white"
        self.btProcess["bg"] = "#34A853"
        self.btProcess["relief"] = "flat" 
        self.btProcess.pack(fill=X,padx=40,pady=25)

    def resource_path(self,relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath("./icons")

        return os.path.join(base_path, relative_path)

    def getPath(self):

        ConfigFileDialog = Tk()
        ConfigFileDialog.withdraw()

        self.DirScanMain = filedialog.askdirectory()

        self.lbDirLocal["wraplength"] = self.frameDir.winfo_width() - 15
        self.lbDirLocal["text"] = self.DirScanMain

    def configureScreen(self,event):

        self.lbDirLocal["wraplength"] = event.width - 15

    def process(self):

        if (self.DirScanMain != ""):

            self.master.process(self.DirScanMain)
            self.lbDirLocal["text"] = "Select Folder >"
        else:

            self.lbDirLocal["text"] = "Select a folder to continue >"

