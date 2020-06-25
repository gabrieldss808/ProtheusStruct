import os
os.environ["KIVY_NO_CONSOLELOG"] = '1'

import kivy

from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView

class ResultScreen(Screen):
    pass

#Classe para definição do corpo do Aplicativo.
class ResultScreenCorpo(ScrollView):
    pass 

class MenuSuperior(BoxLayout):
    pass