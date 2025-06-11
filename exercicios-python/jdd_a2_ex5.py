# Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.

def calcula_quadrado(msg) -> int:
    while True:
        try:
            num = int(input(msg))
            return num ** 2
        except ValueError:
            print("Digite um nº inteiro!")
        except KeyboardInterrupt:
            print('\nOperação encerrada pelo usuário.')
            exit(1)
        except EOFError:
            print('\nEntrada encerrada inesperadamente.')
            exit(1)

n = calcula_quadrado("Digite o nº que você quer elevar ao quadrado: ")
print(f'O quadrado do número digitado é: {n} ')
