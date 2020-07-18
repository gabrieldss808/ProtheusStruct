# ProtheusStruct
Projeto do Prothus Struct, é uma aplicação em Python que analisa arquivos da estrutura do Protheus e retorna as informações necessárias para analisar a configuração de estrutura feita

# Ideia Principal
A ideia é que a partir de uma pasta principais passada pelo usuário, o aplicativo analise os arquivos e tragam as informações do AppServer, configuração de porta, RPOs, serviços Ativos do Protheus e as configurações de conexão do Smartclient e de forma visual para facilitar a analise.
Com isso na area de Suporte é possivel trazer mais agilidade na aplicação de Patchs para o Protheus e também manutenções, trazendo agilidade para os analistas que perdem muito tempo com analise de ambientes e estruturas do Protheus.

# Versão Console

Feita para ter um acesso acelerado a ferramenta.

[Download ProtheusStruct Console Version](dist/ProtheusStructConsoleVersion.rar)

O funcionamento dele consiste em informar a pasta aonde será analisado e o programa irá gerar um arquivo txt com o resultado:

![gif](https://user-images.githubusercontent.com/45453977/87819848-52753b00-c843-11ea-8a17-d947daef5431.gif)

***Abaixo as Chaves de pesquisa padrão do Appserver.ini***

{'SOURCEPATH','PORT','ROOTPATH','SERVER','ALIAS'}

***E também as chaves de pesquisa do Smartclient.ini***

{'SERVER','PORT','ENVSERVER'}

<H3>Também Possui um arquivo de configuração para poder adicionar chaves de pesquisa do Ini, tanto para o AppServer, quanto para o Smartclient e também o nome do RPO que é pesquisado:</H3>

***Ele precisa estar com o Nome abaixo:***

![image](https://user-images.githubusercontent.com/45453977/87817516-7b93cc80-c83f-11ea-9791-e66455bfcd31.png)

***Segue o exemplo de configuração:***

![image](https://user-images.githubusercontent.com/45453977/87817212-f3adc280-c83e-11ea-8765-dcf97d09d7d4.png)

# Protheus Struct Visual Interface:

***Em desenvolvimento***

![dormrm](https://user-images.githubusercontent.com/45453977/87856311-b0ae2680-c8f4-11ea-9b02-01830a710976.gif)

