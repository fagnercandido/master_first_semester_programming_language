def soma10(lista):
    for index, item in enumerate(lista, start=0):
        for indexIntern, itemIntern in enumerate(lista, start=0):
            if item+itemIntern == 10 and index != indexIntern and index < indexIntern:
                print(str(index)+" "+str(indexIntern))



lista = [10,3,5,5,0]
soma10(lista)