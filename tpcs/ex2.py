#Crie um programa que pede ao utilizador para inserir números. Para cada número inserido, apenas o deverá armazenar numa lista se este fôr ímpar e positivo. Se o utilizador inserir o valor -1, a inserção deverá terminar, sendo impressos:
#numa linha os elementos da lista, separados por espaços, ordenados de forma decrescente
#noutra linha a média dos valores da lista
#Insira um numero: 

listaDeImparesPositivos = []
while True:
  numero = input("Insira um numero: ")
  if numero and numero.lstrip("-").isdigit() and int(numero) < 0 and int(numero) == -1:
      break
  if numero and numero.isdigit() and int(numero) > 0 and int(numero) % 2 != 0:
      listaDeImparesPositivos.append(int(numero))
listaDeImparesPositivos = sorted(listaDeImparesPositivos, reverse=True)
print(*listaDeImparesPositivos)
print(sum(listaDeImparesPositivos)/len(listaDeImparesPositivos))
