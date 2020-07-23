from ProtheusStructClassMain import ProtheusStruct

# Protheus Struct app que analisa arquivos da estrutura Protheus e retorna as principais informações do Ambiente Protheus
#A partir dos appserver.ini e smartclient.ini
# Para mais detalhes: https://github.com/gabrieldss808/ProtheusStruct/blob/master/README.md

AppExec = ProtheusStruct()

AppExec.ConfigAppComponents()

AppExec.mainloop()