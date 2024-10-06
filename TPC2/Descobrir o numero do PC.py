# Relatório TP2
## Data:2024-09-16
## Autor: Dinis Pereira a107276

## Resumo

# O TPC2 consistiu em fazer o computador adivinhar o número em que estamos a pensar.




##Descobrir o número do PC

import random

min = 0
max = 100
resposta = random.randint(min,max)

nosso = int(input("Tenta adivinhar em que numero eu estou a pensar! "))
tentativas = 1

while nosso != resposta:
    if nosso > resposta:
        nosso = int(input("Tenta outra vez. Uma dica, o numero é menor: "))
        tentativas = tentativas + 1
    elif nosso < resposta:
        nosso = int(input("Tenta outra vez. Uma dica, o numero é maior: "))
        tentativas = tentativas + 1

print(f"PARABÉNS, acertaste em {tentativas} tentativas!")
