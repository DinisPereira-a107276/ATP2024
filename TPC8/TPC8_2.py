# a) Especifique uma função que dada uma string e uma substring não vazia, 
# calcula  o número de vezes em que a substring aparece na string, sem que haja sobreposição de substrings:

def strCount(s, subs):
    countador = 0
    posição = 0
    while posição != -1:
        posição = s.find(subs, posição)
        if posição != -1:
            countador += 1
            posição += len(subs)

    return countador

print(strCount("catcowcat", "cat"))
print(strCount("catcowcat", "cow"))
print(strCount("catcowcat", "dog"))

# b) Especifique uma função que recebe uma lista de números inteiros positivos e 
# devolve o menor produto que for possível calcular multiplicando os 3 menores inteiros da lista:

#min1<min2<min3
def produtoM3(lista):
    min1 = lista[0]
    min2 = lista [0]
    min3 = lista [0]
    for n in lista:
        if n < min1:
            min3 = min2
            min2 = min1
            min1 = n
        else:
            if n < min2:
                min3 = min2
                min2 = n
            else:
                if n < min3:
                    min3 = n
    if min1 > min2:
        min1, min2 = min2, min1
    if min1 > min3:
        min1, min3 = min3, min1
    if min2 > min3:
        min2, min3 = min3, min2


    produto = min1*min2*min3
    return  produto

print(produtoM3([12,3,7,10,12,8,9]))

# c) Especifique uma função que dado um número inteiro positivo, 
# repetidamente adiciona os seus dígitos até obter apenas um dígito que é retornado como resultado:

def reduxInt(n):
    somafinal=100
    while somafinal > 9:
        soma=0
        digito =[int(d) for d in str(n)]
        for h in digito:
            soma += h
        somafinal = soma
        n = soma

    return soma

print(reduxInt(6))

# d) Especifique uma função que recebe duas strings, `string1` e `string2`, 
# e devolve o índice da primeira ocorrência de `string2` em `string1`, caso não ocorra nenhuma vez a função deverá retornar `-1`:

def myIndexOf(s1, s2):
    posição=-1
    if s2 in s1:
        for n in range(len(s1)):
            if s1[n:n+len(s2)] == s2:
                posição = n
    return posição

print(myIndexOf("Hoje está um belo dia de sol!", "está"))