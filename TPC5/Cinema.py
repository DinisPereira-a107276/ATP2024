#TPC 5


#.strip é tirar os espaços no input
#.split é aquilo de teres lista dentro de listas (1,2,(1,2,3)) que passa para 1 2 3 4 5

import random 

def crescente(lista):
    n = len(lista)
    for i in range(n):
        trocou = False
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                # Troca os elementos
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocou = True
    return lista



numsalas = ["1", "2", "3", "4", "5", "6"]
disponivel = False



def sala():
    rand = random.randint(1, 12)
    titulo = ""

    if rand < 4:
        titulo = "Deadpool"
    elif rand < 7:
        titulo = "Avatar"
    elif rand < 10:
        titulo = "Trolls"
    else:
        titulo = "Anyone but You"

    numlug = random.randint(80, 150)
    while numlug % 10 != 0:
        numlug = random.randint(80, 150)

    vendas = random.randint(1, numlug)
    lugares_vendidos = random.sample(range(1, numlug + 1), vendas)

    return [titulo, numlug, vendas, crescente(lugares_vendidos)]

cinema = [sala() for _ in range(6)] 


def menu():
    return ("""Seja bem vindo! Deseja:
    (1) Visualizar salas:
    (2) Filmes em exibição:
    (3) Lugares disponíveis:
    (4) Comprar bilhete:
    (5) Criar nova sala:
    (0) Desligar sistema:
    """)
    


tecla = 1

while tecla != 0:
    print(menu())
    try:
        tecla = int(input("Escolhe uma das opções: "))
    except ValueError:
        print("Por favor, insira um número válido.")
        continue


    if tecla == 1:
        for i in range(len(numsalas)):
            print(f"""A sala número {numsalas[i]} contém as seguintes informações:
                Filme: {cinema[i][0]}
                Lugares: {cinema[i][1]}
                Disponíveis: {cinema[i][1] - cinema[i][2]}
                """)
        input("Carrega para voltares ao menu:")


    elif tecla == 2:
        filmes = ["Deadpool", "Avatar", "Trolls", "Anyone but You"]
        for procuro in filmes:
            existe = False
            print(f"{procuro}:")
            for i in range(len(numsalas)):
                if cinema[i][0] == procuro:
                    print(f"Sala {numsalas[i]}")
                    existe = True
            if not existe:
                print(f"O filme {procuro} não está disponível no cinema.")
        input("Carrega para voltares ao menu:")


    elif tecla == 3:
        for i in range(len(numsalas)):
            print(f"Sala {numsalas[i]}: {cinema[i][0], cinema[i][1], cinema[i][2]}")
        
        escolha1 = str(input("Escolhe uma sala: "))
        
        if escolha1 not in numsalas:
            print("Escolha inválida! Tente novamente.")
        else:
            for i in range(len(numsalas)):
                if numsalas[i] == escolha1:
                    print(f"Lugares vendidos da Sala {escolha1}: {cinema[i][3]}")
                    disponivel = True
                    escolha2 = int(input(f"Escolhe um lugar de 1 a {cinema[i][1]}: "))
                    
                    if escolha2 < 1 or escolha2 > cinema[i][1]:
                        print("Lugar inválido! Tente novamente:")
                    elif escolha2 in cinema[i][3]:
                        disponivel = False
                        print(disponivel)
                    else:
                        print(disponivel)
                        salai = i
        input("Carrega para voltares ao menu:")


    elif tecla == 4:
        if not disponivel:
            print("Salecione um lugar disponível na opção 3 do menu.")
        else:
            resposta = input(f"Deseja comprar o bilhete para o filme {cinema[salai][0]}, na sala {numsalas[salai]}, no lugar {escolha2}? (s/n)")
            if resposta == 's':
                cinema[salai][3].append(escolha2)
                cinema[salai][2] += 1

                crescente(cinema[salai][3])

                print("Bilhete comprado com sucesso!")
            else:
                print("Compra cancelada.")

        input("Carrega para voltares ao menu:")


    elif tecla == 5:
        novasalanum = input("Qual o número da sala que queres criar: ")
        while novasalanum in numsalas:
            novasalanum = input("Essa sala já existe, cria outra: ")

        numsalas.append(novasalanum)  
        cinema.append(sala())  
        print(f"Sala {novasalanum}")
        print(cinema[-1])

        input("Carrega para voltares ao menu: ")


print("Adeus!")