def listar_repetidas(lista):
    letrasPorQuantidade = {}
    listaMaioresQueUm = []
    for item in lista:
        for letra in item:
            if letrasPorQuantidade.get(letra.lower()):
                total = letrasPorQuantidade.get(letra.lower())
                letrasPorQuantidade[letra.lower()] = total + 1
            else:
                letrasPorQuantidade[letra.lower()] = 1
    for key in sorted(letrasPorQuantidade.items(), key=lambda x: x[0], reverse=True):
        if key[1] > 1:
            listaMaioresQueUm.append(key[0])
    print(sorted(listaMaioresQueUm))

lista = ["Ana", "Mario", "Antonio"]
listar_repetidas(lista)