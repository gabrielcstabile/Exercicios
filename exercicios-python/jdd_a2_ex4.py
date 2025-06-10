# Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo

def valida_inteiro(msg: str, permitir_zero: bool = True) -> int:
    while True:
        try:
            num = int(input(msg))
            if not permitir_zero and num == 0:
                print('Não utilize 0 no segundo valor.')
                continue
            return num
        
        except ValueError:
            print('Digite um nº inteiro')
        except KeyboardInterrupt:
            print('\nOperação encerrada pelo usuário.')
            exit(1)
        except EOFError:
            print('\nEntrada encerrada inesperadamente.')
            exit(1)
        
n1 = valida_inteiro('Digite o primeiro nº: ')
n2 = valida_inteiro('Digite o segundo nº: ', permitir_zero=False)

print(f'A divisão inteira entre {n1} e {n2} é: { n1 // n2}')