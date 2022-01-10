import os

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

def calcula_ocorrencia_de_letras(filename):
    letters = {}
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            words = line.split()
            for word in words:
                for letter in word:
                    if letter.isalpha():
                        if letter.lower() in letters:
                            total = letters.get(letter.lower())
                            total = total + 1
                            letters[letter.lower()] = total
                        else:
                            letters[letter.lower()] = 1
    return dict(sorted(letters.items(), key=lambda item: item[1], reverse=True))
