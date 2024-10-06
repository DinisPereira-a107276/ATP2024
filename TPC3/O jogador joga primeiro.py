# Relatório TP3
## Data:2024-09-23
## Autor: Dinis Pereira a107276

## Resumo

# O TPC3 consistiu em fazer o computador jogar connosco o jogo dos 21 pauzinhos.




# O Jogador joga primeiro

pauzinhos = 21
acabou = False

jogador = int(input(f"Olá, retira de 1-4 dos {pauzinhos} pauzinhos."))


while acabou == False:
    
    if jogador > 4 and jogador < 1:
        jogador = int(input(f"Tenta outra vez, retira de 1-4 dos {pauzinhos} pauzinhos."))
    
    elif pauzinhos == 1:
        print("Ganhei!!!")
    else:  
            soma5 = 5 - jogador
            pauzinhos = pauzinhos - jogador
            pauzinhosantigos = pauzinhos 
            pauzinhos = pauzinhos - soma5
            if pauzinhos == 1:
                print(f"Eu retiro {soma5} dos {pauzinhosantigos}, por isso ganhei!!!")
                acabou = True
            else:
                jogador = int(input(f"Eu retirei {soma5} dos {pauzinhosantigos}, retira de 1-4 dos {pauzinhos} pauzinhos."))