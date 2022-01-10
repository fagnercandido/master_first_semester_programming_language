import os

def pede_nome():
    while True:
        name = input('Informe o nome do ficheiro: ')
        if os.path.exists(name) and os.path.splitext(name)[1] == '.txt':
            return name

def gera_nome(name):
    name_file, extension = os.path.splitext(name)
    return name_file+'.json'