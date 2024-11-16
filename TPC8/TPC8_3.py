redeSocial = [
    {
        'id': 'p1',
        'conteudo': 'Os melhores filmes de Star Wars são os originais',
        'autor': 'ggy',
        'dataCriacao': '2023-07-23',
        'comentarios': [
            {'comentario': 'Completamente de acordo...', 'autor': 'jj'},
            {'comentario': 'Gosto mais das prequels', 'autor': 'pqf'}
        ]
    },
    {
        'id': 'p2',
        'conteudo': 'Qual é o melhor filme de animação?',
        'autor': 'pqf',
        'dataCriacao': '2023-07-24',
        'comentarios': [
            {'comentario': 'Rei Leão', 'autor': 'jj'},
            {'comentario': 'Frozen', 'autor': 'mnl'},
            {'comentario': 'Big Hero 6', 'autor': 'ggy'}
        ]
    }
]



# a) `quantosPost`, que indica quantos posts estão registados:

def quantosPost(redeSocial):
    npost = 0
    for n in redeSocial:
        npost += 1
    return npost

print(quantosPost(redeSocial))

# b)  `postsAutor`, que devolve a lista de posts de um determinado autor:

def postsAutor(redeSocial, autor):
    for n in redeSocial:
        if n['autor'] == autor:  # Acessando a chave 'autor' dentro de cada post
            print(n)
    return 
autor='ggy'
print(postsAutor(redeSocial,autor))

# c) `autores`, que devolve a lista de autores de posts ordenada alfabeticamente:

def ordenar(lista):
    n = len(lista)
    for a in range(n):
        for b in range(0, n-a-1):
            if lista[b] > lista[b+1]:
                lista[b], lista[b+1] = lista[b+1], lista[b]
    return lista

def autores(redeSocial):
    autores = []
    for n in redeSocial:
        if n['autor'] not in autores:
            autores.append(n['autor'])
    for n in n['comentarios']:
        if n['autor'] not in autores:
            autores.append(n['autor'])
    ordenar(autores)
    return  autores

print(autores(redeSocial))

# d) `insPost`, que acrescenta um novo post à rede social a partir dos parâmetros recebidos e devolve a nova rede social.

redeSocial = [
    {
        'id': 'p1',
        'conteudo': 'Os melhores filmes de Star Wars são os originais',
        'autor': 'ggy',
        'dataCriacao': '2023-07-23',
        'comentarios': [
            {'comentario': 'Completamente de acordo...', 'autor': 'jj'},
            {'comentario': 'Gosto mais das prequels', 'autor': 'pqf'}
        ]
    },
    {
        'id': 'p2',
        'conteudo': 'Qual é o melhor filme de animação?',
        'autor': 'pqf',
        'dataCriacao': '2023-07-24',
        'comentarios': [
            {'comentario': 'Rei Leão', 'autor': 'jj'},
            {'comentario': 'Frozen', 'autor': 'mnl'},
            {'comentario': 'Big Hero 6', 'autor': 'ggy'}
        ]
    }
]

def insPost(redeSocial, conteudo, autor, dataCriacao, comentarios):
    n = len(redeSocial) + 1
    idn=(f'p{n}')
    post=({
        'id': idn,
        'conteudo': conteudo,
        'autor': autor,
        'dataCriacao': dataCriacao,
        'comentarios': comentarios
    })
    redeSocial.append(post)
    return 

insPost(redeSocial, 'Novo post!', 'Eu', 'Agora', ('comentario1','comentario2'))
print(redeSocial)

# e)  `remPost`, que remove um post da rede, correspondente ao `id` recebido.

redeSocial = [
    {
        'id': 'p1',
        'conteudo': 'Os melhores filmes de Star Wars são os originais',
        'autor': 'ggy',
        'dataCriacao': '2023-07-23',
        'comentarios': [
            {'comentario': 'Completamente de acordo...', 'autor': 'jj'},
            {'comentario': 'Gosto mais das prequels', 'autor': 'pqf'}
        ]
    },
    {
        'id': 'p2',
        'conteudo': 'Qual é o melhor filme de animação?',
        'autor': 'pqf',
        'dataCriacao': '2023-07-24',
        'comentarios': [
            {'comentario': 'Rei Leão', 'autor': 'jj'},
            {'comentario': 'Frozen', 'autor': 'mnl'},
            {'comentario': 'Big Hero 6', 'autor': 'ggy'}
        ]
    }
]



print(redeSocial)

def remPost(redeSocial, id):
    for n in redeSocial:
        if n['id'] == id:
            redeSocial.remove(n)
    return redeSocial

print(remPost(redeSocial, 'p2'))

# f) `postsPorAutor`, que devolve uma distribuição de posts por autor (à semelhança do que foi feito nas aulas).

redeSocial = [
    {
        'id': 'p1',
        'conteudo': 'Os melhores filmes de Star Wars são os originais',
        'autor': 'ggy',
        'dataCriacao': '2023-07-23',
        'comentarios': [
            {'comentario': 'Completamente de acordo...', 'autor': 'jj'},
            {'comentario': 'Gosto mais das prequels', 'autor': 'pqf'}
        ]
    },
    {
        'id': 'p2',
        'conteudo': 'Qual é o melhor filme de animação?',
        'autor': 'pqf',
        'dataCriacao': '2023-07-24',
        'comentarios': [
            {'comentario': 'Rei Leão', 'autor': 'jj'},
            {'comentario': 'Frozen', 'autor': 'mnl'},
            {'comentario': 'Big Hero 6', 'autor': 'ggy'}
        ]
    }
]

def postsPorAutor(redeSocial):
    for n in autores(redeSocial):
        for i in redeSocial:
            if i['autor']== n:
                print(f"""Autor: {n}
                      Post: {i}
                """)
    return 

print(postsPorAutor(redeSocial))

# g) `comentadoPor`, que recebe um autor e devolve a lista de posts comentados por esse autor.

def comentadoPor(redeSocial, autor):
    fin=[]
    for n in redeSocial: 
        for i in n['comentarios']:
            if i['autor'] == autor:
                fin.append(n)


    return fin

print(comentadoPor(redeSocial, 'mnl'))
