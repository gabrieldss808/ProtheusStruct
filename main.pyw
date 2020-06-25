# //-------------------------------------------------------------------
# /*/ ProtheusStruct

# ProtheusStruct: App responsável por analisar os arquivos da estrutura
# Protheus a partir de uma pasta Raíz

# @author Gabriel Da Silva Souza
# @since 23/06/2020
# @version 1.0
# /*/
# //-------------------------------------------------------------------'''
import kivy
import os
import sys
from kivy.app import App
from interface import MainInterface

#Criação do App
class ProtheusStruct(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
 
        self.icon = self.resource_path("icon.ico")

    def build(self,**kwargs):

        mainInter = MainInterface()     

        return mainInter
    
    def resource_path(self,relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath("./icons")

        return os.path.join(base_path, relative_path)

# Execução
if __name__ == "__main__":
    
    ProtheusStruct().run()
