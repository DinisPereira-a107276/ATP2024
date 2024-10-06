# Relatório TP3
## Data:2024-09-23
## Autor: Dinis Pereira a107276

## Resumo

# O TPC3 consistiu em fazer o computador jogar connosco o jogo dos 21 pauzinhos.




# O PC joga primeiro.

import random
acabou = False
min = 1
max = 4
comp = random. randint(min,max)
triomax = 3
trio = random.randint(min,triomax)
inicial = 21
atual = inicial - comp

jogador = int(input(f"Olá jogador, eu retiro {comp} a {inicial} dando assim {atual}.Quanto vais retirar de 1-4?"))

atual2 = atual - jogador

while acabou == False:
    soma5 = jogador + comp
    comp = random. randint(min,max)

    if jogador < 1 or jogador > 4 :
        print("ERRO!")
        jogador = input("Adeus...")
        acabou = True

    if atual2 == 1:
        print("Ganhaste!")
        acabou = True

    elif atual2 < 6 and 0 < atual2:
        comp = atual2 - 1
        atual3 = atual2 - comp
        print(f"Eu retiro {comp} a {atual2} dando assim {atual3}, ou seja, eu ganhei!!!")
        acabou = True

    elif soma5 == 5:
        comp = random. randint(min,max)
        atual3 = atual2 - comp
        jogador = int(input(f"Eu retiro {comp} a {atual2} dando assim {atual3}.É a tua vez:"))
        atual2 = atual3 - jogador

    elif atual2 == 0:
        print("ERRO!")
        acabou = True

    elif 6 < atual2 and atual2< 10:
        comp = atual2 - 4 - 2
        atual3 = atual2 - comp
        jogador = int(input(f"Eu retiro {comp} a {atual2} dando assim {atual3}.É a tua vez:"))
        atual2 = atual3 - jogador

    elif jogador + comp < 5:
        comp == 5 - jogador - comp
        atual3 = atual2 - comp
        jogador = int(input(f"Eu retiro {comp} a {atual2} dando assim {atual3}.É a tua vez:"))
        atual2 = atual3 - jogador
        
    elif jogador + comp > 4:
        comp = 10 - jogador - comp
        atual3 = atual2 - comp
        jogador = int(input(f"Eu retiro {comp} a {atual2} dando assim {atual3}.É a tua vez:"))
        atual2 = atual3 - jogador
    
    else:
        atual3 = atual2 - comp
        jogador = int(input(f"Eu retiro {comp} a {atual2} dando assim {atual3}.É a tua vez:"))
        atual2 = atual3 - jogador
        
        
        