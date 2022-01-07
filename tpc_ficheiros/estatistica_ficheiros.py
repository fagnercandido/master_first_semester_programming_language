import os

def pede_nome():
    while True:
        filename = input('Informe o nome do ficheiro: ')
        files = os.listdir('.')
        if any(filename in item for item in files):
            return filename

def calcula_linhas(filename):
    lines = sum(1 for line in open(filename))
    return lines

def calcula_carateres(filename):
    file = open(filename, 'r')
    return len(file.read())

def calcula_palavra_comprida(filename):
    file = open(filename, 'r')
    words = file.read().split()
    word_more_longer = len(max(words, key=len))
    return [word for word in words if len(word) == word_more_longer][0]

def guarda_resultados(filename):
    file = open('resultados.txt', 'a')
    file.write(f'Análise do ficheiro: {filename}\n')
    file.write(f'Numero de linhas: {calcula_linhas(filename)}\n')
    file.write(f'Numero de carateres: {calcula_carateres(filename)}\n')
    file.write(f'Comprimento máximo: {len(calcula_palavra_comprida(filename))}\n')
    file.close()