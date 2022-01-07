def converte(dicionario):
    mapa = {}
    for key in dicionario:
        if mapa.get(dicionario.get(key)):
            items = mapa.get(dicionario.get(key))
            items.append(key)
        else:
            mapa[dicionario.get(key)] = [key]
    print(mapa)

d1 = {'bailar':'dance', 'brincar':'play', 'dancar':'dance', 'estudar':'study', 'jogar':'play'}
converte(d1)