
from consoleVersionClasses.ProtheusStructConsoleControl import ProtheusStructConsole

# Protheus Struct versão console
# Software responsável por obter os dados da Estrutura Protheus e facilitar a analise de ambientes, porém na versão console
#feita para ter acesso rapido a ferramenta, essa versão foi feita antes da versão visual.
# Para mais detalhes: https://github.com/gabrieldss808/ProtheusStruct/blob/master/README.md

ProtheusStructCon = ProtheusStructConsole()

ProtheusStructCon.getPath()

ProtheusStructCon.ConfigScan()

ProtheusStructCon.executeScan()

ProtheusStructCon.generateResult()
