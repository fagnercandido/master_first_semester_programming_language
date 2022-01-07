def insira():
    while True:
        entrada = input("Insira um inteiro impar entre -20 e -10: ")
        if entrada and entrada.lstrip("-").isdigit() and isInteger(entrada) and int(entrada) >= -20 and int(entrada) <= -10 and int(entrada) % 2 != 0:
            print('obrigado')
            break

def isInteger(number):
    if '.' not in number:
        return True
    return False

insira()