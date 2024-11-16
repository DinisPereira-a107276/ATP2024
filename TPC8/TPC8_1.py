# a) Lista formada pelos elementos que não são comuns às duas listas:

lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]  
ncomuns = []

for n in lista1:
    if n not in lista2:
        ncomuns.append(n)

for n in lista2:
    if n not in lista1:
        ncomuns.append(n)

print(ncomuns)

# b) Lista formada pelas palavras do texto compostas por mais de 3 letras:

texto = """Vivia há já não poucos anos algures num concelho do Ribatejo 
    um pequeno lavrador e negociante de gado chamado Manuel Peres Vigário"""
lista = []
palavras = texto.split()
for n in palavras:
    if len(n) > 3:
        lista.append(n)

print(lista)

# c) Lista formada por pares do tipo (índice, valor) com os valores da lista dada:

lista = ['anaconda', 'burro', 'cavalo', 'macaco']
listaRes = []
indice = 1
for n in lista:
    listaRes.append((indice,n))
    indice += 1

print(listaRes)