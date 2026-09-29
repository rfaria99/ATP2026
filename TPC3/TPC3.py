import random
resposta ='s'
nums_chave = [1, 12, 23, 34, 45, 56, 67, 78, 89, 100]
print ('''Bem vindo ao jogo - Corrida até aos 100\nO jogador vai competir com a máquina para ver quem consegue chegar primeiro exatamente ao nº 100''')
while resposta != 'n':
    escolha = int(input("Escolha quem quer que seja o primeiro a começar (1/2):\n1- Máquina;\n2- O jogador\n"))
    total = 0
    total_temp = 0
    i = 0
    if escolha == 1:
        while total != 100:
            num_maquina = nums_chave[i] - total_temp
            total = total_temp + num_maquina
            if total < 100:
                num_utilizador = int(input(f'A máquina escolheu o nº {num_maquina}, o total vai em {total}.\nO jogador escolhe (de 1 a 10): '))
                while num_utilizador < 1 or num_utilizador > 10:
                        print ('Nº inválido')
                        num_utilizador = int(input(f'A máquina escolheu o nº {num_maquina}, o jogador escolhe (de 1 a 10): '))
                total_temp += num_maquina + num_utilizador
                i += 1
            else:
                print ("A máquina venceu")
    elif escolha == 2:
        while total != 100:
            num_utilizador = int(input("Escolha um nº (1 a 10): "))
            while num_utilizador < 1 or num_utilizador > 10:
                print ('Nº Inválido')
                num_utilizador = int(input("Escolha um nº (1 a 10): "))
            if total < 100:
                x = nums_chave[i] - num_utilizador
                if x >= 1 and x <= 10:
                    num_maquina = x
                else:
                    num_maquina = random.randint(1,10)
            total += num_maquina + num_utilizador 
    else:
         print ("Escolha inválida")