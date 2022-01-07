def listar(numero):
    lista = []
    contador = 2
    if numero <= 0 or type(numero) == float:
        return []
    while True:
        if contador % 2 == 0:
            lista.append(contador)
            if len(lista) == numero:
                return lista
        contador = contador + 1
print(listar(5))