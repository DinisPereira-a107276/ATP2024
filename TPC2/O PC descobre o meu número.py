# Relatório TP2
## Data:2024-09-16
## Autor: Dinis Pereira a107276

## Resumo

# O TPC2 consistiu em fazer o computador adivinhar o número em que estamos a pensar.




##O PC descobre o meu número

import random

min = 0
max = 100

tentativas = 1
finished = False
computador = random.randint(min,max)

while not finished:
    resposta = input(f"Estás a pensar no número {computador}? Se sim escreve (=) , se for maior escreve (+) e se for menor escreve (-) : ")

    if resposta == "=":
        print(f"Acertei em {tentativas} tentativas!")
        finished = True
    elif resposta == "+":
        min = computador + 1
        computador = random.randint(min,max)
        tentativas = tentativas + 1
    elif resposta == "-":
        max = computador -1
        computador = random.randint(min,max)
        tentativas = tentativas + 1
    else:
        print("OPÇÃO INVÁLIDA")