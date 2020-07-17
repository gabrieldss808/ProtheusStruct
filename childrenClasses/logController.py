from datetime import datetime

class logController():

    def clearLog(self):

        self.consoleLog = open('strucProt.log','w')

        self.consoleLog.write("")

    #Metodo responsável por atualizar os console log da ultima execução do App
    def consoleLogAdd(self, menssageText):

        self.consoleLog = open('strucProt.log','a')

        self.consoleLog.write("####" + datetime.now().strftime("%d/%m/%Y %H:%M:%S") + '\n')

        self.consoleLog.write(menssageText + '\n')

        self.consoleLog.close()