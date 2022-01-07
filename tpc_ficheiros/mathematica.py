def le_inteiro_positivo():
    while True:
        numero = input("Insira um inteiro positivo: ")
        # no negative and positive number
        if numero and numero.lstrip("-").isdigit() and int(numero) > 0:
            return int(numero)

def fatorial(numero):
    # factorial of 1 or 0 is one, case no, multiple less one
    return 1 if (numero == 1 or numero == 0) else numero * fatorial(int(numero) - 1)