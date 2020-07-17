import win32.lib.win32serviceutil 
from childrenClasses.logController import logController

class ValidService():
    
    __log = logController

    def __init__(self):
        super().__init__()

        self.__log = logController()

    def validService(self,nameService=''):

        service = win32.lib.win32serviceutil
        StringErro = ""

        try:

            service.QueryServiceStatus(nameService)
            return True
        except Exception as e:

            StringErro+= '###########################################################\n'
            StringErro+= "Erro no Serviço: " + nameService + "\t" + "Erro: " + str(e) + "\n"
            StringErro+= '###########################################################\n'

            self.__log.consoleLogAdd(StringErro)

            return False