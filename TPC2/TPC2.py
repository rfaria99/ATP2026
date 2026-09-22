import random

numero = random.randint (0,100)

resposta = "s"
while resposta != "n":
    resposta = int(input("Introduza um inteiro para tentar adivinhar o nº aleatório: "))
    while resposta != numero:
        if resposta > numero:
            resposta = int(input("O número é menor, tente novamente: "))
        else:
            resposta = int(input("O número é maior, tente novamente: "))
    print ("Acertou!!")
    resposta = input("Deseja jogar novamente? (s/n): ")

print ("Até à próxima!")       