# Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.

def retorna_resto (msg):
    while True:
        try:
            num = int(input(msg))
            return num
        except ValueError:
            print("Digite um nº inteiro")

num = retorna_resto("Digite um nº: ")
CONSTANTE_RESTO = 5

print(f'O resto da divisão do número {num} divido por 5 é: {num % CONSTANTE_RESTO}.')