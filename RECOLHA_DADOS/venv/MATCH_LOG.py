from collections import OrderedDict

def MATCH_LOG(lista):
    lista_2=[]
    for i in lista:
        info = i.split('/')
        nome_string = info[4] + '-Match-Logs'
        for l in range(6):
            ano = 2014 + l
            ano_string = str(ano) + '-' + str(ano+1)
            lista_2.append('https://fbref.com/en/players/' + info[3] + '/matchlogs/' + ano_string +  '/' + nome_string)

    return list(OrderedDict.fromkeys(lista_2))