while True:
  numero = input("Insira um inteiro negativo ímpar: ")
  if numero and numero.lstrip("-").isdigit() and int(numero) < 0 and int(numero) % 2 != 0:
    lista = []
    for item in range(int(numero), 1, 1):
      if(item % 2 == 0 and item != 0):
        lista.append(item)
    print(lista)
    break


