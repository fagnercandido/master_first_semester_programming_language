while True:
  entrada = input("Insira uma palavra com 4 caracteres alfabeticos diferentes: ")
  if entrada.isalpha() and len(set(entrada)) == 4:
      print('obrigado')
      break