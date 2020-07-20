import datetime, time
import win32.lib.win32serviceutil 

from threading import Thread
from copy import copy,deepcopy
from pathlib import Path
from configparser import ConfigParser
from childrenClasses.logController import logController
from childrenClasses.classChildrens import appserver, smartclient, RPO
from childrenClasses.validService import ValidService


#Classe responsável pelo Processamento e obtenção dos dados da estrutura Protheus
class scanStruct():

    __appservers = list()
    __smartclients = list()
    __Struct = Path
    __executeSmart = bool
    __executeAppServer = bool
    appserverKeys = list()
    smartclientKeys = list()
    appserverNameArq = ""
    smartclientNameArq = ""
    cNameRPO = ''
    __log = logController
    __Maindir = ''
    __ValidServ = ValidService
    isExecuteProcess = bool
    wasFoundSomething = bool

    def __init__(self,dir=''):

        self.__Maindir = dir
        self.__Struct = Path(dir)
        self.appserverKeys = {'SOURCEPATH','PORT','ROOTPATH','SERVER','ALIAS'}
        self.smartclientKeys = {'SERVER','PORT','ENVSERVER'}
        self.appserverNameArq = "appserver"
        self.smartclientNameArq = "smartclient"
        self.cNameRPO = 'tttp120.rpo'
        self.__log = logController()
        self.__ValidServ = ValidService()

    def getProgressStatus(self):

        return self.__progressStatus

    def addAppServerKey(self,appServerKey=''):

        if(appServerKey != ''):

            self.appserverKeys.add(appServerKey.upper())

    def addSmartClientKey(self,smartClientKey=''):

        if(smartClientKey != ''):

            self.smartclientKeys.add(smartClientKey.upper())

    def execute(self):

        StringErroAp = ''
        StringErroSmar = ''
        self.__appservers.clear()
        self.__smartclients.clear()


        self.isExecuteProcess = True

        self.__log.consoleLogAdd('Scan Struct Iniciando... \n')

        try:

            self.__log.consoleLogAdd('Procurando Appservers...')

            self.__searchAppservers()
        except Exception as appserverError:
            
            StringErroAp+= '###########################################################\n'
            StringErroAp+= "Erro na Estrutura Appserver: \t" + str(appserverError) + "\n"
            StringErroAp+= '###########################################################\n'

            self.__log.consoleLogAdd(StringErroAp)

        try:

            self.__log.consoleLogAdd('Procurando Smartclients...')

            self.__searchSmartclient()
        except Exception as smartclientError:

            StringErroSmar+= '###########################################################\n'
            StringErroSmar+= "Erro na Estrutura Smartclient: \t" + str(smartclientError) + "\n"
            StringErroSmar+= '###########################################################\n'

            self.__log.consoleLogAdd(StringErroSmar)
        
        self.isExecuteProcess = False
        self.FoundSomething()

    def FoundSomething(self):

        if(self.getSmartclients() == {} and self.getApperservers() == {}):

            self.wasFoundSomething = False
        else:
            
            self.wasFoundSomething = True
        
    def getApperservers(self):

        if(len(self.__appservers) > 0):
            
            return self.__appservers
        else:

            return {}
    
    def getSmartclients(self):

        if(len(self.__smartclients) > 0):
            
            return self.__smartclients
        else:

            return {}

    def __searchSmartclient(self):

        StringErroSmar = ''
        
        if(self.smartclientNameArq == ""):

            smartclientsPure = list(self.__Struct.glob('**/*'+ self.smartclientNameArq +'.ini'))
        else:

            smartclientsPure = list(self.__Struct.glob('**/*'+ self.smartclientNameArq +'*.ini'))


        for smartclientPure in smartclientsPure:

            try:

                self.__log.consoleLogAdd('Filtrando Dados do Smartclient ' + str(smartclientPure))
                self.__createSmartclientObject(smartclientPure)
            except Exception as smartclientError:

                StringErroSmar+= '###########################################################\n'
                StringErroSmar+= "Erro no Smartclient: \t" + str(smartclientsPure) + '\n\t' + str(smartclientError) + "\n"
                StringErroSmar+= '###########################################################\n'

                self.__log.consoleLogAdd(StringErroSmar)
        
        self.__log.consoleLogAdd('Foram encontrados ' + str(len(self.__smartclients)) + ' Smartclients Na Busca da Pasta: ' + self.__Maindir)

    def __createSmartclientObject(self,smartclientPure):

        SmarArquivo = open(smartclientPure)
        boolSmartClient = False

        smartclientObject = copy(smartclient())
        smartclientObject.cdir = SmarArquivo.name

        Config = ConfigParser()
        Config.read_file(SmarArquivo)

        for section in Config.sections():

            for properties in Config[section].keys():

                if(properties.upper() in self.smartclientKeys):
                    
                    smartclientObject.cContent += 'Seção: ' + section + '\n\t ' + properties + ':'+Config[section][properties] + ' \n '
                    boolSmartClient = True
        
        if(boolSmartClient):

            self.__smartclients.append(smartclientObject)

        Config = None

    def __searchAppservers(self):

        StringErroAp = ''

        if(self.appserverNameArq == ""):

            appserversPure = list(self.__Struct.glob('**/*' + self.appserverNameArq + '.ini'))
        else:

            appserversPure = list(self.__Struct.glob('**/*' + self.appserverNameArq + '*.ini'))

        for appServerPure in appserversPure:

            try:

                self.__log.consoleLogAdd('Filtrando Dados do Appserver ' + str(appServerPure))
                self.__createAppserverObject(appServerPure)
            except Exception as appserverError:
                
                StringErroAp+= '###########################################################\n'
                StringErroAp+= "Erro no Appserver: \t" + str(appServerPure) + '\n\t' + str(appserverError) + "\n"
                StringErroAp+= '###########################################################\n'

                self.__log.consoleLogAdd(StringErroAp)

        self.__log.consoleLogAdd('Foram encontrados ' + str(len(self.__appservers)) + ' AppServers Na Busca da Pasta: ' + self.__Maindir)
  
    def __createAppserverObject(self,appServerPure):

        booleanSection = True
        boolAppserver = False
        AppArquivo = open(appServerPure)

        appserverObject = copy(appserver())
        appserverObject.cdir = AppArquivo.name

        Config = ConfigParser()
        Config.read_file(AppArquivo)

        for section in Config.sections():

            for properties in Config[section].keys():
                            
                if(properties.upper() in self.appserverKeys ):

                    boolAppserver = True

                    if(booleanSection):
                        appserverObject.cContent += 'Seção: ' + section + ' \n\t ' 
                        booleanSection = False

                    if(properties.upper() == 'SOURCEPATH'):

                        rpoDir = Path(Config[section][properties])
                        
                        try:
                            rpo =rpoDir/self.cNameRPO.upper()
                            open(rpo)
                        except:
                            rpo=None
                        
                        ArqRPO = RPO()
                        ArqRPO.cSection = section

                        if(rpo != None):

                            ArqRPO.lEncontrado = True
                            ArqRPO.cDir = rpoDir
                            ArqRPO.cDataAlteracao = str(datetime.datetime.fromtimestamp(rpo.stat().st_mtime))
                        else:
                            ArqRPO.lEncontrado = False
                            ArqRPO.cDir = rpoDir
                        
                        appserverObject.listRpo.append(ArqRPO)        
                    else:
                        appserverObject.cContent += ' \n\t ' + properties + ':'+Config[section][properties] + ' \n '

                if (section.upper() == 'SERVICE'):

                    if(properties.upper() == 'NAME'):

                        appserverObject.cNameService =  Config[section][properties]

                        if(self.__ValidServ.validService(Config[section][properties])):
                            
                            appserverObject.lServiceExists = True
                        else:
                            
                            appserverObject.lServiceExists = False
                    elif(properties.upper() == 'DISPLAYNAME'):
                        
                        appserverObject.cDisplayNameService =  Config[section][properties]
                
                if(section.upper() == 'TCP'):

                    if(properties.upper() == 'PORT'):

                        appserverObject.cport = Config[section][properties]

            booleanSection = True


        if(boolAppserver):

            self.__appservers.append(appserverObject)

        Config = None