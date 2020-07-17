#Classes para armazenagens de Dados Organizados
class appserver():

    cdir = ''
    cContent = ''
    cport = ''
    cNameService = ''
    cDisplayNameService = ''
    lServiceExists = bool
    listRpo = list()

    def __init__(self):

        self.cdir = ''
        self.cContent = ''
        self.cport = ''
        self.cNameService = ''
        self.cDisplayNameService = ''
        self.lServiceExists = bool
        self.listRpo = list()

class RPO():

    cDir = ''
    cDataAlteracao = ''
    lEncontrado = bool
    cSection = ''

class smartclient():

    cdir = ''
    cContent = ''

    def __init__(self):

        self.cdir = ''
        self.cContent = ''   
