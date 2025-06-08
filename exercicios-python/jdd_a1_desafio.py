# Escreva um programa em Python que solicita ao usuário para digitar seu nome, 
# o valor do seu salário mensal e o valor do bônus que recebeu.
# O programa deve, então, imprimir uma mensagem saudando o usuário pelo nome e 
# informando o valor final do salário + o bônus.

nome: str = input("Digite o seu nome: ")
salario = float(input("Informe o seu salário: "))
bonus = float(input("Digite a porcentagem do seu bônus: "))
CONSTANTE_BONUS: float = 1000.00

valor_bonus = CONSTANTE_BONUS + (salario * bonus)

print(f"Olá, {nome} o seu bônus é de R$ {valor_bonus:.2f}")
