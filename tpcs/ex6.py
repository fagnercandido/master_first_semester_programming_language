datas = [('Maria', 'Santos', 10), ('Manuel', 'Sa', 15), ('André', 'Gil', 7), ('Vanda', 'Esteves', 12)]
filtro = input("Escolha um criterio de ordenação ('nome', 'apelido' ou 'idade'): ")
if filtro != 'nome' and filtro != 'apelido' and filtro != 'idade':
    print('Input inválido')
else:
    dicionarioFiltros = {
        "nome": 0,
        "apelido": 1,
        "idade": 2
    }
    print(sorted(datas, key=lambda tuple: tuple[dicionarioFiltros[filtro]]))
