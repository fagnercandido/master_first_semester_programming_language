import os
import csv
from matplotlib import pyplot as plt

def pede_pasta():
    while True:
        name = input('Este programa analisa o tipo de ficheiros presente numa pasta. Insira o caminho para uma pasta: ')
        if os.path.isdir(name):
            return name

def faz_calculos(directory):
    os.chdir(directory)
    files = [file for file in os.listdir(directory) if os.path.isfile(os.path.join(directory, file))]
    result = {}
    for file in files:
        _, file_extension = os.path.splitext(file)
        if file_extension[1:] in result:
            item = result.get(file_extension)
            item['volume'] = item['volume']+os.path.getsize(file)/1024
            item['quantidade'] = item['quantidade']+1
        else:
            result[file_extension[1:]] = {'volume': os.path.getsize(file)/1024, 'quantidade': 1}
    return result

def guarda_resultados(directory, result):
    nome_ficheiro_csv = os.path.basename(directory)
    nome_ficheiro_csv = nome_ficheiro_csv + '.csv'
    print(nome_ficheiro_csv)
    with open(nome_ficheiro_csv, 'w', newline='') as ficheiro:
        campos = ['Extensao','Quantidade','Tamanho[kByte]']
        writer = csv.DictWriter(ficheiro, fieldnames=campos)
        writer.writeheader()
        for key, value in result.items():
            writer.writerow({'Extensao': key, 'Quantidade': value['quantidade'], 'Tamanho[kByte]': value['volume']})
    print(f'Os resultados foram guardados no ficheiro {nome_ficheiro_csv}')

def faz_grafico_queijos(result):
    plt.pie([item['volume'] for item in result.values()], labels=[*result], autopct='%1.0f%%')
    plt.title('Gráfico Queijos Volume')
    plt.show()

    plt.pie([item['quantidade'] for item in result.values()], labels=[*result], autopct='%1.0f%%')
    plt.title('Gráfico Queijos Quantidade')
    plt.show()

def faz_grafico_barras(result):
    plt.bar([*result], [item['volume'] for item in result.values()])
    plt.title('Gráfico Barras Volume')
    plt.show()

    plt.bar([*result], [item['quantidade'] for item in result.values()])
    plt.title('Gráfico Barras Quantidade')
    plt.show()