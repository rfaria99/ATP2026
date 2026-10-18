def criarAluno():
    nome = input('\nIntroduza o nome do/a aluno/a: ')
    id = input('\nIntroduza a identificação do/a aluno/a: ')
    l = []
    i = 0
    while i < 3:
        if i == 0:
            nota = float(input('\nIntroduza a nota (0-20) do TPC: '))
        if i == 1:
            nota = float(input('\nIntroduza a nota (0-20) do Projeto: '))
        if i == 2:
            nota = float(input('\nIntroduza a nota (0-20) do Teste: '))
        i+=1
        while nota < 0 or nota > 20:
            nota = float(input('\nA nota dada é inválida, reintroduza: '))
        l.append(nota)
    aluno = (nome,id,l)
    return aluno

def verificaVazio (l):
    return len(l) == 0

def criarTurma(n):
    l = []
    i = 0
    while i < n:
        l.append(criarAluno())
        i+=1
    return l

def inserirAluno(l):
    return l.append(criarAluno())

def listarTurma(l):
    print ('\nNOME ||   ID   || NOTAS: TPC, PROJETO, TESTE')
    for aluno in l:
        nome,id,notas = aluno
        print(f'{nome}||{id}||{notas[0]:.2f},{notas[1]:.2f},{notas[2]:.2f}')
    return

def consultaID (l, id):
    contador = 0
    for aluno in l:
        nome,iden,_ = aluno
        if id == iden:
            print(f'\nÉ o aluno {nome}')
            contador += 1
    if contador == 0:
        print ('\nNão existe um(a) aluno/a com esse ID')
    return

def guardarTurma (l, fnome):
    file = open(fnome, 'w')
    file.write('NOME ||   ID   || NOTAS: TPC, PROJETO, TESTE')
    for aluno in l:
            nome,id,notas = aluno
            file.write(f'\n{nome}||{id}||{notas[0]:.2f},{notas[1]:.2f},{notas[2]:.2f}')
    file.close()

def carregarTurma (fnome):
    l = []
    file = open(fnome,'r')
    file.readline()
    for line in file:
        notaT = []
        nome,id,notas = line.split('||')
        notaLista = notas.split(',')
        for nota in notaLista:
            notaT.append(float(nota))
        aluno = (nome,id,notaT)
        l.append(aluno)
    file.close()
    return l

l = []
i = 0

print (""">>>>>>>> Menu <<<<<<<<

>>> Escolha a operação que quer efetuar à sua turma:

> (1) Crie uma Turma;
> (2) Insira um(a) aluno/a na Turma;
> (3) Listar a Turma;
> (4) Consulta aluno/a por ID;
> (5) Guardar turma num ficheiro;
> (6) Carregar uma turma a partir do ficheiro;
> (0) Sair do programa.""")

opcao = input('\nEscolha a sua opção:\n>>> ')
menus = ['1','2','3','4','5','6','0']

while opcao != '0':
    while not(opcao in menus) or len(opcao)!=1:
        print ("""\n>>>>>>>> Menu <<<<<<<<

>>> Escolha a operação que quer efetuar à sua turma:

> (1) Crie uma Turma;
> (2) Insira um aluno na Turma;
> (3) Listar a Turma;
> (4) Consulta aluno por ID;
> (5) Guardar turma num ficheiro;
> (6) Carregar uma turma a partir do ficheiro;
> (0) Sair do programa.""")

        opcao = input('\nA sua escolha foi inválida, tente novamente:\n>>> ')
    if opcao == '1':
        n = int(input('\nDe quantos alunos quer a sua turma: '))
        l = criarTurma (n)
        if verificaVazio(l):
            print('\nTurma não foi criada com sucesso.')
        else:
            print('\nA sua Turma foi criada.')
    elif opcao == '2':
        inserirAluno(l)
    elif opcao == '3':
        if verificaVazio(l):
             print('\nNão existe uma turma para listar.')
        else:
            listarTurma(l)
    elif opcao == '4':
        if verificaVazio(l):
            print('\nNão existe uma Turma para poder consultar o aluno.')
        else:
            id = input('\nQual é a identificação do/a aluno/a?\n>>> ')
            consultaID(l, id)
    elif opcao == '5':
        if verificaVazio(l):
            print('\nNão existe uma Turma para guardar num ficheiro.')
        else:
            nomeFicheiro = input('\nQual o nome que quer dar ao seu ficheiro (após escolher, mantenha sempre o mesmo, por turma)?\n>>> ')
            guardarTurma(l, nomeFicheiro)
    elif opcao == '6':
        nomeFicheiro = input('\nQual o nome que quer dar ao seu ficheiro (após escolher, mantenha sempre o mesmo, por turma)?\n>>> ')
        l = carregarTurma(nomeFicheiro)
        if len(l) != 0:
            print('Turma carregada com sucesso.')
        else:
            print('Não foi possível extrair a Turma do ficheiro.')

    print ("""\n>>>>>>>> Menu <<<<<<<<

>>> Escolha a operação que quer efetuar à sua turma:

> (1) Crie uma Turma;
> (2) Insira um aluno na Turma;
> (3) Listar a Turma;
> (4) Consulta aluno por ID;
> (5) Guardar turma num ficheiro;
> (6) Carregar uma turma a partir do ficheiro;
> (0) Sair do programa.""")

    opcao = input('\nEscolha a sua opção:\n>>> ')

print('Até a próxima!')