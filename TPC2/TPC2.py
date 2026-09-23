import random

numero = random.randint (0,100)
limite_min = 0
limite_max = 100
contador = 0
resposta = "s"
while resposta != "n":

    escolha = int(input("Escolha qual jogo quer jogar:\n1- Tente adivinhar o nº que o computador pensou;" 
        "\n2- Computador tenta adivinhar o seu nº\n (Escolha 1/2): "))
    if escolha == 1:
        resposta = int(input("Introduza um inteiro para tentar adivinhar o nº aleatório: "))
        while resposta != numero:
            contador +=1
            if resposta > numero:
                resposta = int(input("O número é menor, tente novamente: "))
            else:
                resposta = int(input("O número é maior, tente novamente: "))
        print (f"Acertou!! em {contador} tentativas!")

    elif escolha == 2:
        while resposta != "Acertou!":
            numero2 = random.randint (limite_min, limite_max)
            contador +=1
            print (f"\nO número que a máquina pensou foi {numero2}\n")
            resposta = input ("A máquina acertou? Se sim, escreva:\n-Acertou!\n-Errou, o número que pensei é maior\n"
                "-Errou, o númerou que pensei é menor\n- ")  
            if resposta == "Errou, o número que pensei é maior":
                limite_min = numero2 + 1
            else:
                limite_max = numero2 - 1
        print (f"A máquina acertou em {contador} tentativas")
    else:
        print ("Não existe o que escolheu.")

    resposta = input("Deseja jogar novamente? (s/n): ")

print ("Até à próxima!")       