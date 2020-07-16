
class logController():

    def clearLog(self):

        self.consoleLog = open('strucProt.log','w')

        self.consoleLog.write("")

    #Metodo responsável por atualizar os console log da ultima execução do App
    def consoleLogAdd(self, menssageText):

        self.consoleLog = open('strucProt.log','a')

        self.consoleLog.write(menssageText + '\n')

        self.consoleLog.close()