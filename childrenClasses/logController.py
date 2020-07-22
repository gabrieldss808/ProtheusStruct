from datetime import datetime

class logController():

    def clearLog(self):

        self.consoleLog = open('strucProt.log','w',1,'utf-8')

        self.consoleLog.write("")

    #Metodo responsável por atualizar os console log da ultima execução do App
    def consoleLogAdd(self, menssageText):

        self.consoleLog = open('strucProt.log','a',1,'utf-8')

        self.consoleLog.write("####" + datetime.now().strftime("%d/%m/%Y %H:%M:%S") + '\n')

        self.consoleLog.write(menssageText + '\n')

        self.consoleLog.close()