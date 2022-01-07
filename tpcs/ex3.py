def getNumber(number):
    if '.' not in number:
        return int(number)
    return float(number)

entradaA = input("Insira um número: ")
entradaB = input("Insira um número: ")

numeroA = getNumber(entradaA)
numberoB = getNumber(entradaB)

if numeroA < numberoB:
    print(f'{numeroA} é menor que {numberoB}')
elif numeroA > numberoB:
    print(f'{numeroA} é maior que {numberoB}')
else:
    print(f'{numeroA} e {numberoB} são iguais')