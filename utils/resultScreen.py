import os
os.environ["KIVY_NO_CONSOLELOG"] = '1'

import kivy

from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class ResultScreen(Screen):
    
    MainDir = ''
    appserversWidgets = list()
    smartclientsWidgets = list()

    def ConstructResults(self):
        
        self.GetWidgetsList()
        
        self.CreateResultBody()

    def GetWidgetsList(self):
        
        self.MainDir = self.get_root_window().children[0].MainDir
        self.appserversWidgets = self.get_root_window().children[0].appserversWidgets
        self.smartclientsWidgets = self.get_root_window().children[0].smartclientsWidgets

    def CreateResultBody(self):

        ResultScreenDadosObject = ResultScreenDados()

        ResultScreenDadosObject.add_widget(MainDirVisualization(self.MainDir,len(self.appserversWidgets),len(self.smartclientsWidgets)))

        for appserverWidgets in self.appserversWidgets:

            ResultScreenDadosObject.add_widget(appserverWidgets)

        

        self.children[0].ids.ScrollViewResult.add_widget(ResultScreenDadosObject)




#Classe para definição do corpo do Aplicativo.
class ResultScreenCorpo(BoxLayout):
    pass 

class TopMenu(BoxLayout):
    pass

class MainDirVisualization(BoxLayout):

    textMainDir = ''

    def __init__(self, textMainDir='',QtdAppServers=0,QtdSmarclients=0 ,**kwargs):
        super().__init__(**kwargs)

        self.textMainDir = 'Pasta Principal: ' + textMainDir + '\n'

        if(QtdAppServers > 1 and QtdSmarclients > 1):
            self.textMainDir += 'Foram Encontrados ' + str(QtdAppServers) + ' Appservers e ' + str(QtdSmarclients) + ' Smartclients\n'
        elif(QtdAppServers > 1):
            self.textMainDir += 'Foram Encontrados ' + str(QtdAppServers) + ' Appservers e ' + str(QtdSmarclients) + ' Smartclient\n'
        elif(QtdSmarclients > 1):
            self.textMainDir += 'Foi Encontrado ' + str(QtdAppServers) + ' Appserver e ' + str(QtdSmarclients) + ' Smartclients\n'
        elif(QtdAppServers == 0):
            self.textMainDir += 'Foi Encontrado ' + str(QtdAppServers) + ' Appserver e ' + str(QtdSmarclients) + ' Smartclients\n'
        elif(QtdAppServers == 1):            
            self.textMainDir += 'Foi Encontrado ' + str(QtdAppServers) + ' Appserver\n'

        self.ids.LbTextMainDir.text = self.textMainDir

class ResultScreenDados(BoxLayout):
    pass