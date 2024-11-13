#TPC 6
## Data:2024-10-07
## Autor: Dinis Pereira a107276

#Este TPC consiste em criar salas com alunos e colocar essa turma em ficheiros.
#aluno=(nome,id, [notaTPC, notaProj, notaTeste])-tuplo
#turma=[alunos]-lista

tecla = 19
numturma = []
escola = []
continua = 0

def turma():
    return 
    
def menu():
    print("""\nSeja bem vindo! Deseja:
    1. Criar Turma
    2. Inserir aluno
    3. Listar turma
    4. Consultar aluno por id
    5. Guardar turma
    6. Carregar uma turma de um ficheiro
    0. Sair da aplicação
          """)

def criarturma(escola):
    escola.append([])
    print("Turma adicionada!")

def listaturma(escola):
    contadorT = 1
    for turma in escola:
        print(f"\nTurma {contadorT}:")
        for aluno in turma:
            print(f"{aluno[0]}(id:{aluno[1]})| Nota TPC: {aluno[2][0]}; Nota Projeto: {aluno[2][1]}; Nota Teste: {aluno[2][2]}")
        contadorT += 1

def inseriraluno(escola):
    listaturma(escola)
    turma = int(input(f"A que turma deseja adicionar: ")) - 1
    if turma > len(escola):
        print("Insira uma turma existente.")
        inseriraluno(escola)
    else:
        nome_aluno = (str(input("Nome do aluno: ")))
        id_aluno = (str(input("Id do aluno: ")))
        notas = []
        notaTPC = float(input("Nota do TPC: "))
        notaPROJETO = float(input("Nota do Projeto: "))
        notaTESTE = float(input("Nota do Teste: "))
        notas.append(notaTPC)
        notas.append(notaPROJETO)
        notas.append(notaTESTE)
        aluno = (nome_aluno, id_aluno, notas)
        escola[turma].append(aluno)
        print(f"O aluno com as seguintes informações[{aluno}]foi adicionado à turma {turma + 1}")

def consultaraluno(escola):
        num_turma = 0
        alunoencontrado = False
        id = input("Qual é o id que deseja procurar? ")
        for turma in escola:
            num_turma += 1
            for aluno in turma:
                if aluno[1] == id:
                    print(f"""O aluno com o id {id} pertence à turma {num_turma}:
{aluno[0]}(id:{aluno[1]})| Nota TPC: {aluno[2][0]}; Nota Projeto: {aluno[2][1]}; Nota Teste: {aluno[2][2]}""")
                    alunoencontrado = True
        if not alunoencontrado:
            print(f"O aluno com id {id} não existe na escola!")


def escreve(escola):
    text = ""
    for turma in escola:
        for aluno in turma:
            text += str(aluno[0]) + "," + str(aluno[1]) + "," + str(aluno[2][0])+ "," + str(aluno[2][1]) + "," + str(aluno[2][2])
            text +="::"
        text += "\n"

    return text

def guardarT(escola):
    file = open("escola.txt", "w")
    file.write(escreve(escola))
    file.close()
    print("Ficheiro guardado em escola.txt")

def carregar(fnome):
    escola = []
    with open(fnome, "r") as file:
        for linha in file:
            if linha.strip() != "":
                turma = []
                alunoS = linha.strip().split("::")
                for aluno in alunoS:
                    campos = aluno.split(",")
                    if len(campos) == 5:
                        nome = campos[0]
                        id = campos[1]
                        notas = [float(campos[2]), float(campos[3]), float(campos[4])]
                        turma.append((nome, id, notas))
                    else:
                        print("Formato inesperado encontrado:", campos)
                escola.append(turma)
            else:
                turma = []
                escola.append(turma)
    print(f"Informações carregadas de {fnome}")
        
    return escola

while tecla != 0:
    menu()
    try:
        tecla = int(input("Escolhe uma das opções: "))
    except ValueError:
        print("Por favor, insira um número válido.")
        continue
        
    if tecla == 1:
        criarturma(escola)

    if tecla == 2:
        inseriraluno(escola)

    if tecla == 3:
        listaturma(escola)
        continua = input("Carrega no enter para continuar")

    if tecla == 4:
        consultaraluno(escola)
        continua = input("Carrega no enter para continuar")

    if tecla == 5:
        guardarT(escola)

    if tecla == 6:
        escola = carregar("escola.txt")
        print(escola)


        

print("Adeus!")