import os
os.environ["KIVY_NO_CONSOLELOG"] = '1'

import kivy

from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class ResultScreen(Screen):
    pass

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

        self.ids.LbTextMainDir.text = self.textMainDir