from csv import reader
from threading import Thread
from time import sleep
from tkinter import DoubleVar
from tkinter import X,LEFT
from tkinter import Label
from tkinter import Button
from tkinter.ttk import Style
from tkinter.ttk import Frame
from tkinter.ttk import Progressbar
from scanStruct import scanStruct
from childrenClasses.logController import logController


class ProcessScreen(Frame):

    progressBarRun = Progressbar
    progressBarStyle = Style
    progressNumber = DoubleVar
    TextProgressProcess = Label
    scanStructObject = scanStruct
    log = logController
    btProcessFinish = Button
    
    def configureScreen(self):

        self.bind("<Configure>", self.configureWidth)

        self.log = logController()

        self.progressNumber = DoubleVar()
        self.progressBarStyle = Style()
        self.progressBarStyle.theme_use('clam')
        self.progressBarStyle.configure("Horizontal.TProgressbar", troughcolor ='#616161', background="#34A853",lightcolor='#34A853',darkcolor="#34A853")
        self.progressBarRun = Progressbar(self,style="Horizontal.TProgressbar",variable=self.progressNumber,maximum=10)
        self.progressBarRun.pack(fill=X,padx=10,pady=10)

        self.TextProgressProcess = Label(self)
        self.TextProgressProcess["bg"] = "#9E9E9E"
        self.TextProgressProcess["font"] = ("Roboto Black","20")
        self.TextProgressProcess["fg"] = "white"
        self.TextProgressProcess["text"] = "Procurando arquivos da estrutura Protheus..."
        self.TextProgressProcess.pack(padx=10,pady=15)


        self.btProcessFinish = Button(self)
        self.btProcessFinish["font"] = ("Roboto Black","20")
        self.btProcessFinish["fg"] = "white"
        self.btProcessFinish["relief"] = "flat"
        self.btProcessFinish["command"] = self.ProcessFinish

    def configureWidth(self,event):

        self.TextProgressProcess["wraplength"] = event.width - 15

    def executeProcess(self,dirMainExec):
        
        self.scanStructObject = scanStruct(dirMainExec)

        self.ConfigScan()

        taskExecuteProcess = Thread(target=self.ExecuteScan,args=[])
        taskExecuteProcess.start()

    def ExecuteScan(self):

        executeScanTask = Thread(target=self.scanStructObject.execute,args=[])
        executeScanTask.start()

        while (self.scanStructObject.isExecuteProcess):
            
            taskUpdProgress = Thread(target=self.updProgressBarRun,args=[])
            taskUpdProgress.start()

            sleep(0.5)

            if(self.progressNumber.get() == 10):

                clearTask = Thread(target=self.ClearProgressBar,args=[])
                clearTask.start()

        stageTask = Thread(target=self.updExecuteProcess,args=[])
        stageTask.start()

        self.btProcessFinish.pack(fill=X,padx=40,pady=20)

        if (self.scanStructObject.wasFoundSomething):

            if (len(self.scanStructObject.getApperservers()) > 0):

                self.master.appservers = self.scanStructObject.getApperservers()
            if (len(self.scanStructObject.getSmartclients()) > 0):

                self.master.smartclients = self.scanStructObject.getSmartclients()
            
            self.btProcessFinish["bg"] = "#34A853"
            self.btProcessFinish["text"] = "Proximo >"
            self.TextProgressProcess["text"] = "Pronto, agora é só ver os resultados!! :)"
        else:

            self.btProcessFinish["bg"] = "#EA4335"
            self.btProcessFinish["text"] = "< Anterior"
            self.TextProgressProcess["text"] = "Não foi encontrado nada nessa pasta :("
    
    def updExecuteProcess(self):

        self.TextProgressProcess["text"] = "Gerando Cards do resultado..."
        self.progressNumber.set(10)

    def ClearProgressBar(self):

        self.progressNumber.set(0)
    
    def updProgressBarRun(self):

        self.progressNumber.set(self.progressNumber.get() + 1)
    
    def ProcessFinish(self):

        if (self.scanStructObject.wasFoundSomething):

            self.master.gotoResult()
        else:
            
            self.master.returnToHome()

    def ConfigScan(self):

        linha = ''
        StringErro = ''

        try:

            with open('configConsoleMode.csv','r') as configArqCSV :

                readerArq = reader(configArqCSV,delimiter=';')

                for linha in readerArq:

                    if(linha[0].upper() == 'APPSERVERKEYS'):

                        for appServerKey in linha:
                            
                            if(appServerKey.upper() == 'APPSERVERKEYS'):
                                
                                pass
                            else:

                                self.scanStructObject.addAppServerKey(appServerKey)
                    if(linha[0].upper() == 'SMARTCLIENTKEYS'):

                        for smartclientKey in linha:

                            if(smartclientKey.upper() == 'SMARTCLIENTKEYS'):

                                pass
                            else:

                                self.scanStructObject.addSmartClientKey(smartclientKey)
                    if(linha[0].upper() == 'RPONAME'):

                        self.scanStructObject.cNameRPO = linha[1] + ".rpo"

        except Exception as e:

            StringErro+= '###########################################################\n'
            StringErro+= "Erro no CSVConfig: \t" + str(e) + "\n"
            StringErro+= '###########################################################\n'

            self.log.consoleLogAdd(StringErro)