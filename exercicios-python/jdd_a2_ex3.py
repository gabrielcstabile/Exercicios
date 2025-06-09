# Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado

def multiplicar_inteiro(msg):
    while True:
        try:
            num = int(input(msg))
            return num
        except ValueError:
            print ("Digite um nº inteiro: ")

n1 = multiplicar_inteiro ("Digite o primeiro nº: ")
n2 = multiplicar_inteiro ("Digite o segundo nº: ")

print(f'A multiplicação de {n1} por {n2} é: {n1 * n2}.')