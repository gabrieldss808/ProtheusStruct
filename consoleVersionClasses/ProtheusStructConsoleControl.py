import tkinter as tk
import os

from time import sleep
from threading import Thread
from csv import reader
from tkinter import filedialog
from scanStruct import scanStruct
from childrenClasses.logController import logController

class ProtheusStructConsole():

    scanStructObject = scanStruct
    DirScanMain = ''
    log = logController

    def __init__(self):

        self.log = logController()
        self.log.clearLog()


    def getPath(self):

        ConfigFileDialog = tk.Tk()
        ConfigFileDialog.withdraw()

        self.DirScanMain = filedialog.askdirectory()

        self.scanStructObject = scanStruct(self.DirScanMain)
    
    def executeScan(self):

        executeTask = Thread(target=self.scanStructObject.execute,args=[])
        executeTask.start()

        while (self.scanStructObject.isExecuteProcess):

            os.system('cls') or None
            print("Procurando arquivos da estrutura Protheus.")
            sleep(1)
            os.system('cls') or None
            print("Procurando arquivos da estrutura Protheus...")   
            sleep(1)
            os.system('cls') or None
            print("Procurando arquivos da estrutura Protheus......")

        print("Processamento Concluído")
    
    def generateTextOutput(self):

        NumberOfAppserver = len(self.scanStructObject.getApperservers())
        NumberOfSmartclient = len(self.scanStructObject.getSmartclients())

        stringResult = ""

        stringResult += "".rjust(len(self.DirScanMain)+19,'#') + "\n"
        stringResult += "".rjust(len(self.DirScanMain)+19,'#') + "\n"
        stringResult += "### Para a Pasta: " + self.DirScanMain + "\n"
        stringResult += "### Foram encontrados: " + str(NumberOfAppserver) + " AppServers\n"
        stringResult += "### Foram encontrados: " + str(NumberOfSmartclient) + " Smartclients\n"
        stringResult += "".rjust(len(self.DirScanMain)+19,'#') + "\n"
        stringResult += "".rjust(len(self.DirScanMain)+19,'#') + "\n\n"

        stringResult += "##################################################################\n"
        stringResult += "##################    Appservers Encontrados    ##################\n"
        stringResult += "##################################################################\n"

        for appserver in self.scanStructObject.getApperservers():

            stringResult += "######################\n"
            stringResult += "# Appserver " + str(self.scanStructObject.getApperservers().index(appserver)+1) + "\n"
            stringResult += "######################\n"
            stringResult += "Local: " + appserver.cdir + "\n"
            stringResult += "Porta: " + appserver.cport + "\n"
            if(appserver.lServiceExists):
                stringResult += "Existe um Serviço instalado com o Nome: " + appserver.cDisplayNameService + "\n"
                stringResult += "Id do Serviço: " + appserver.cNameService + "\n"
            stringResult += "######################\n"
            stringResult += "### Conteúdo do ini ##\n"
            stringResult += "######################\n"
            stringResult += appserver.cContent + "\n"
            stringResult += "######################\n"
            stringResult += "######################\n"
            stringResult += "###  Lista de RPOs  ##\n"
            stringResult += "######################\n"
            for rpo in appserver.listRpo:
                stringResult += "RPO # " + str(appserver.listRpo.index(rpo)+1) + "\n"
                stringResult += "Local: " + str(rpo.cDir) + "\n"
                if(rpo.lEncontrado):
                    stringResult += "Ultima Alteração: " + rpo.cDataAlteracao + "\n"
                stringResult += "Seção do Ini: " + rpo.cSection + "\n"
                stringResult += "##################################################################\n"
            stringResult += "##################################################################\n"
        
        stringResult += "##################################################################\n"
        stringResult += "#################    Smartclients Encontrados    #################\n"
        stringResult += "##################################################################\n"

        for smartclient in self.scanStructObject.getSmartclients():

            stringResult += "######################\n"
            stringResult += "# Smartclient " + str(self.scanStructObject.getSmartclients().index(smartclient)+1) + "\n"
            stringResult += "######################\n"
            stringResult += "Local: " + smartclient.cdir +"\n"
            stringResult += "######################\n"
            stringResult += "### Conteúdo do ini ##\n"
            stringResult += "######################\n"
            stringResult += smartclient.cContent + "\n"
            stringResult += "######################\n"

        return stringResult
            
    def generateResult(self):

        print("Gerando txt de resultado")
        
        StringResult = self.generateTextOutput()

        txtResult = open('ResultProcess.txt','w',1,'utf-8')

        txtResult.write(StringResult)


    def ConfigScan(self):

        linha = ''
        StringErro = ''

        try:

            with open('configScan.csv','r') as configArqCSV :

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