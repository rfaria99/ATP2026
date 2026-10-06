import random

def estaOrdenadaCD (lista,ordem):
    i = 0
    x = True
    if ordem == 'C':
        while i < len(lista)-1:
            if lista [i] > lista [i+1]:
                x = False
            i += 1
    elif ordem == 'D':
        while i < len(lista)-1:
            if lista [-(i+1)] > lista[-(i+2)]:
                x = False
            i += 1
    return x

def verificaVazio (lista):
    x = False
    if len(lista) == 0:
        x = True
    return x

def criaLista (n):
    return ([random.randint (1,100) for elem in range (n)])

def lerLista (n):
    l = []
    while n > 0:
        x = int(input('Introduza um inteiro para adicionar à lista: '))
        l.append(x)
        n -= 1
    return l

def soma (lista):
    total = 0
    for elem in lista:
        total += elem
    return total

def media (lista):
    x = soma (lista)
    m = x / len(lista)
    return m

def maiorElem (lista):
    temp = lista[0]
    for elem in lista:
        if elem >= temp:
            temp = elem
    return temp

def menorElem (lista):
    temp = lista[0]
    for elem in lista:
        if elem <= temp:
            temp = elem
    return temp

def procuraElem (lista, elem):
    i = 0
    pos = []
    while i < len(lista):
        if elem == lista[i]:
            pos.append(i)
        i+=1
    if len(pos) == 0:
        pos = [-1]
    return pos

pos = []
l = []
i = 0
resposta = ""
print('''\nBem vindo à aplicação de manipulação de uma lista de inteiros, por predifinição a lista começa como vazia, aqui estão as opções:
- (1): Criar lista de n elementos (a máquina cria uma lista de 1 a 100 de n elementos);
- (2): Ler lista de n elementos (o utilizador que cria);
- (3): Soma dos elementos da lista;
- (4): Média dos elementos da lista;
- (5): Entrega o maior elemento da lista;
- (6): Entrega o menor elemento da lista;
- (7): Indica se a lista está ordenada por ordem crescente;
- (8): Indica se a lista está ordenada por ordem crescente;
- (9): Procura um elemento à escolha do utilizador e entrega as sua posições, se existir (caso não exista, entrega -1);
- (0): Sair do programa''')

resposta = input('\nOpção: ')

while resposta != "0":
    while int(resposta) < 0 or int(resposta) > 9:
        resposta = input('\nOpção inválida, escolha uma opção: ')
    if resposta == '1':
        n = int(input('\nIndique quantos elementos quer na sua lista aleatória?: '))
        l = criaLista (n)
        print(f'\nA lista criada pela máquina é: {l}')
    elif resposta == '2':
        n = int(input('\nIndique quantos elementos quer na sua lista?: '))
        l = lerLista (n)
        print(f'A sua lista é: {l}')
    elif resposta == '3':
        somaLista = soma(l)
        print(f'A sua soma dos elementos é: {somaLista}')
    elif resposta == '4':
        if verificaVazio (l):
            print('\nA sua lista está vazia, não é possível fazer a média')
        else:
            x = media (l)
            print(f'\nA média da sua lista é: {x:.2f}')
    elif resposta == '5':
        if verificaVazio (l):
            print('\nA sua lista está sem elementos, é impossível encontrar o maior elemento.')
        else:
            x = maiorElem(l)
            print(f'\nO maior elemento da lista é: {x}')
    elif resposta == '6':
        if verificaVazio (l):
            print('\nA sua lista está sem elementos, é impossível encontrar o menor elemento.')
        else:
            x = menorElem(l)
            print(f'\nO menor elemento da lista é: {x}')
    elif resposta == '7':
        if verificaVazio(l):
            print('\nNão dá para verificar se está ordenado por ordem crescente, pois a lista está vazia.')
        elif estaOrdenadaCD(l, 'C'):
            print('\nA lista está ordenada por ordem crescente.')
        else:
            print('\nA lista não está ordenada por ordem crescente.')
    elif resposta == '8':
        if verificaVazio(l):
            print ('\nNão dá para verificar se está ordenado por ordem decrescente, pois a lista está vazia.')
        elif estaOrdenadaCD(l, 'D'):
            print ('\nA lista está ordenada por ordem decrescente.')
        else:
            print('\nA lista não está ordenada por ordem decrescente.')
    elif resposta == '9':
        elem = int(input('\nQual é o elemento que quer verificar a posição na lista?: '))
        pos = procuraElem (l, elem)
        print(f'\nA(s) posição(ões) é/são: {pos}')
    resposta = input('\nQual opção escolhe agora?: ')

print ('Volte mais tarde!')