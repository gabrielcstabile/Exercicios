# Escreva um programa que receba dois números flutuantes e realize sua adição.

def somar_floats():
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        resultado = num1 + num2
        print(f"A soma de {num1} + {num2} é: {resultado}")

    except ValueError:
        print("Erro: você deve digitar números válidos (ex: 3.14, -7.2).")
    except EOFError:
        print("\nEntrada encerrada inesperadamente (Ctrl + D / Ctrl + Z).")
    except KeyboardInterrupt:
        print("\nExecução interrompida pelo usuário (Ctrl + C).")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

somar_floats()
