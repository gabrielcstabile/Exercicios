# Escreva um programa que soma dois números inteiros inseridos pelo usuário.

def soma_inteiro(mensagem):
    while True:
        try:
            numero = int(input(mensagem))
            return numero
        except ValueError:
            print ("Erro! Isto não é um número inteiro. Tente de novo!")

print ("Informe dois números para saber a sua soma")

n1 = soma_inteiro ("Digite o primeiro nº ")
n2 = soma_inteiro ("Digite o segundo nº: ")

print(f'A soma de ambos os números é: {n1 + n2}')