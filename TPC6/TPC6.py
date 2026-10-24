from matplotlib import pyplot as plt

def medias(tabMeteo):
    res = []
    for data,tmin,tmax,_ in tabMeteo:
        media = (tmin+tmax)/2
        res.append((data,media))
    return res

def guardaTabMeteo(t, fnome):
    file = open(fnome,'w')
    file.write('Dia || Temp. Min. || Temp. Max. || Precipitacao')
    for dias in t:
        diaInt,t_min,t_max,prec = dias
        ano,mes,dia = diaInt
        file.write(f'\n{dia}/{mes}/{ano} || {t_min} || {t_max} || {prec}')
        file.close
    return

def carregaTabMeteo(fnome):
    res = []
    file = open(fnome,'r')
    file.readline()
    for line in file:
        data, t_min, t_max, prec = line.split(' || ')
        dia,mes,ano = data.split('/')
        day=(int(ano),int(mes),int(dia[0:]))
        res.append((day,float(t_min),float(t_max),float(prec)))
    file.close()
    return res

def minMin(tabMeteo):
    minima = tabMeteo[0][1]
    for _,tmin,_,_ in tabMeteo:
        if minima>=tmin:
            minima=tmin
    return minima

def amplTerm(tabMeteo):
    res = []
    for data,tmin,tmax,_ in tabMeteo:
        amp = tmax-tmin
        res.append((data,amp))
    return res

def maxChuva(tabMeteo):
    max_data=tabMeteo[0][0]
    max_prec=tabMeteo[0][3]
    for dia,_,_,prec in tabMeteo:
        if max_prec<=prec:
            max_prec = prec
            max_data=dia
    return (max_data, max_prec)

def diasChuvosos(tabMeteo, p):
    l = []
    for data,_,_,prec in tabMeteo:
        if prec > p:
            dia = (data,prec)
            l.append(dia)
    return l

def maxPeriodoCalor(tabMeteo, p):
    max_contador = 0
    contador = 0
    for *_,prec in tabMeteo:
        if prec < p:
            contador+=1
            if max_contador < contador:
                        max_contador = contador
        else:
            contador = 0

    return max_contador

def grafTabMeteo(t):
    y_min = [tmin for _,tmin,*_ in t]
    y_max = [tmax for *_,tmax,_ in t]
    y_prec = [prec for *_,prec in t]
    x = [f'{data[0]}/{data[1]}/{data[2]}' for data,*_ in t]
    plt.plot(x,y_max, color='red', marker='o', label='Tmáx ºC')
    plt.plot(x,y_min, color='purple', marker='o', label='Tmin ºC')
    plt.title('Temperaturas Mínimas')
    plt.legend()
    plt.grid()
    plt.show()

    plt.bar(x,y_prec, label='Precitipatação (mm)')
    plt.title('Precipitação')
    plt.legend()
    plt.show()
    return

def criarDia(l):
    if len(l) != 0:
        data,*_ = l[-1]
        ano = int(input('Indique o ano: '))
        while ano < data[0]:
            ano = int(input('Insira o ano por ordem, por favor: '))
        mes = int(input('Indique o mês: '))
        while mes < data[1]:
            mes = int(input('Insira o mês por ordem, por favor: '))
        dia = int(input('Indique o dia: '))
        while dia <= data[2]:
            dia = int(input('Insira o dia por ordem, por favor: '))
    else:
        ano = int(input('Indique o ano: '))
        mes = int(input('Indique o mês: '))
        dia = int(input('Indique o dia: '))
    diaf = (ano,mes,dia)
    tmin = float(input('Introduza a temperatura mínima: '))
    tmax = float(input('Introduza a temperatura máxima: '))
    while tmax < tmin:
        tmax = float(input('Está a introduzir uma temperatura máxima maior que a mínima, introduza algo válido: '))
    prec = float(input('Introduza o valor da sua precipitação (0-1): '))
    while prec < 0 or prec > 1:
        prec = float(input('Reintroduza uma precipitação válida: '))
    return (diaf,tmin,tmax,prec)

def acrescentaDia(l):
    return l.append(criarDia(l))

def criaTabela(n):
    l = []
    while n > 0:
        l.append(criarDia(l))
        n-=1
    return l

def listaTabela(l):
    print('\n  DATA  ||  Temp. Mín  ||  Temp. Máx  ||  Precipitação')
    for data,tmin,tmax,prec in l:
        print(f'{data[0]}/{data[1]}/{data[2]}||{tmin}||{tmax}||{prec}')
    return

def maxMax(l):
    maximo = l[0][2]
    for _,_,tmax,_ in l:
        if maximo<=tmax:
            maximo=tmax
    return maximo

l = []
i = 0

print ('''>>> Programa de gerenciamento de dias e a sua metereologia
>>> INFO: 
 - Tabela de Metereologia = [(Data, Temp. Mínima, Temp. Máxima, Precipitação);
 - Data = (Ano, Mês, Dia);
 - Ano = Mês = Dia = Int;
 - Temp. Mínima = Temp. Máxima = Precipitação = Float.''')
menus = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','0']

print('''\n=========== MENU ===========
(1)  Criar uma tabela metereológica de n dias;
(2)  Acrescentar um dia à tabela;
(3)  Listar a tabela metereológica;
(4)  Guardar tabela em um ficheiro de texto;
(5)  Importar ficheiro de texto para a tabela;
(6)  Média das temperaturas mínimas e máximas em cada dia;
(7)  Indica qual é a menor das temperaturas mínimas dos dias;
(8)  Indica qual é a maior das temperaturas máximas dos dias;
(9)  Indica as amplitudes térmicas dos dias;
(10) Indica os dias com precipitação maior que o indicador;
(11) Indica o nº de dias mais consecutivos com precipitação menor que o indicador;
(12) Indica o dia com maior precipitação;
(13) Gráfico dos dias e as suas Temps e precipitação;
(0)  Sair do programa''')
escolha = input('\n>>> ')

while escolha != '0':
    while not (escolha in menus) and len(escolha)!=1:
        print('''\n=========== MENU ===========
(1)  Criar uma tabela metereológica de n dias;
(2)  Acrescentar um dia à tabela;
(3)  Listar a tabela metereológica;
(4)  Guardar tabela em um ficheiro de texto;
(5)  Importar ficheiro de texto para a tabela;
(6)  Média das temperaturas mínimas e máximas em cada dia;
(7)  Indica qual é a menor das temperaturas mínimas dos dias;
(8)  Indica qual é a maior das temperaturas máximas dos dias;
(9)  Indica as amplitudes térmicas dos dias;
(10) Indica os dias com precipitação maior que o indicador;
(11) Indica o nº de dias mais consecutivos com precipitação menor que o indicador;
(12) Indica o dia com maior precipitação;
(13) Gráfico dos dias e as suas Temps e precipitação;
(0)  Sair do programa''')
        escolha = input('\nA sua opção foi inválida, escolha novamente:\n>>> ')
    if escolha == '1':
        n = int(input('\nIntroduza de quantos dias quer a sua tabela meteorológica: '))
        l = criaTabela(n)
        if len(l) != 0:
            print('\nTabela criada com sucesso')
        else:
            print('\nTabela não foi criada com sucesso')
    elif escolha == '2':
        acrescentaDia(l)
    elif escolha == '3':
        if len(l) == 0:
            print('\nNão existe tabela para listar')
        else:
            listaTabela(l)
    elif escolha == '4':
        if len(l) == 0:
            print('\nNão existe tabela para guardar.')
        else:
            nomeF = input('\nQual o nome que quer dar ao seu ficheiro que guarda a tabela?\n>>> ')
            guardaTabMeteo(l,nomeF)
    elif escolha == '5':
        nomeF = input('\nIndica o nome do ficheiro do qual quer carregar a tabela:\n>>> ')
        l = carregaTabMeteo(nomeF)
        if len(l) != 0:
            print ('\nTabela carregada com sucesso.')
        else:
            print('\nNão foi possível importar a tabela.')
    elif escolha == '6':
        if len(l) == 0:
            print('\nNão existe tabela para fazer média das temperaturas.')
        else:
            media = medias(l)
            for data,med in media:
                ano,mes,dia=data
                print(f'\nA média das temperaturas em {dia}/{mes}/{ano} = {med}')
    elif escolha == '7':
        if len(l) == 0:
            print('\nNão existe tabela para verificar mínimo das temps mínimas.')
        else:
            min = minMin(l)
            print(f'\nA temperatura mínima é = {min}')
    elif escolha == '8':
        if len(l) == 0:
            print('\nNão existe tabela para verificar máximo das temps máximas.')
        else:
            max = maxMax(l)
            print(f'\nA temperatura mnáxima é = {max}')
    elif escolha == '9':
        if len(l) == 0:
            print('\nNão existe tabela para verificar as amplitudes térmicas.')
        else:
            amp = amplTerm(l)
            for data, ampl in amp:
                ano,mes,dia=data
                print(f'\nA amplitude térmica em {dia}/{mes}/{ano} é {ampl}')
    elif escolha == '10':
        if len(l) == 0:
            print('\nNão existe tabela para indicar os dias chuvosos')
        else:
            indicador = float(input('\nHouve chuva para dias de precipitação maior que o indicador (indique um indicador): '))
            diaschuva=diasChuvosos(l,indicador)
            print('\nHouve dias de chuva em: ')
            for data,prec in diaschuva:
                dia,mes,ano=data
                print(f'Chuveu em {dia}/{mes}/{ano}, com uma precipitação de {prec}; ')
    elif escolha == '11':
        if len(l) == 0:
            print('\nNão existe tabela para verificar o nº maior de dias consecutivos com chuva menor que um indicador dado.')
        else:
            indicador = float(input('\nNão houve chuva em dias com índice de precipitação menores que o indicador (indique): '))
            dias = maxPeriodoCalor(l,indicador)
            print(f'\nO nº máximo de dias consecutivos sem chuva foi: {dias}')
    elif escolha == '12':
        if len(l) == 0:
            print('\nNão existe tabela para verificar dia de maior chuva.')
        else:
            diamax,precmax = maxChuva(l)
            ano,mes,dia = diamax
            print(f'\nO dia {dia}/{mes}/{ano} foi o de maior precipitação registado, com: {precmax}')
    elif escolha == '13':
        if len(l) == 0:
            print('\nNão existe tabela para fazer gráficos.')
        else:
            grafTabMeteo(l)

    print('''\n=========== MENU ===========
(1)  Criar uma tabela metereológica de n dias;
(2)  Acrescentar um dia à tabela;
(3)  Listar a tabela metereológica;
(4)  Guardar tabela em um ficheiro de texto;
(5)  Importar ficheiro de texto para a tabela;
(6)  Média das temperaturas mínimas e máximas em cada dia;
(7)  Indica qual é a menor das temperaturas mínimas dos dias;
(8)  Indica qual é a maior das temperaturas máximas dos dias;
(9)  Indica as amplitudes térmicas dos dias;
(10) Indica os dias com precipitação maior que o indicador;
(11) Indica o nº de dias mais consecutivos com precipitação menor que o indicador;
(12) Indica o dia com maior precipitação;
(13) Gráfico dos dias e as suas Temps e precipitação;
(0)  Sair do programa''')
    escolha = input('\n>>> ')

print('Até à próxima!')