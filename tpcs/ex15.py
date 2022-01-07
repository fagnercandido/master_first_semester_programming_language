def soma(m,n):
    return m + n


def cria_lista_pares(lista):
    return list(filter(lambda n: n % 2 == 0, lista))


def calcula_media_pares(lista):
    pares = list(filter(lambda n: n % 2 == 0, lista))
    return sum(pares)/len(pares)

def conta_pares(lista):
    pares = list(filter(lambda n: n % 2 == 0, lista))
    return len(pares)

def calcula_maximo(lista):
    print("")
    maximo = lista[0]
    posicao = 0
    for index, item in enumerate(lista):
        if maximo < item:
            maximo = item
            posicao = index
    return posicao

def existe_na_lista(lista, n):
    return lista.count(n) > 0

def conta(valor,pessoas):
    return (valor+valor*0.1)/pessoas

print(conta(54.3, 4))