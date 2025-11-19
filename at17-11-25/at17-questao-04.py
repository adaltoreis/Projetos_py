"""
4 - Criar um código que serve para analisar números digitados pelo usuário, classificando-os como pares ou ímpares e contabilizando quantos de cada tipo foram inseridos.

"""

def analisar_numeros():
    
    pares = 0
    impares = 0

    print("Digite números (digite '0' para encerrar):")
    while True:
        try:
            numero = int(input("Número: "))
            if numero == 0:
                break
            if numero % 2 == 0:
                print(f"{numero} é PAR")
                pares += 1
            else:
                print(f"{numero} é ÍMPAR")
                impares += 1
        except ValueError:
            print("Por favor, digite um número válido.")

    print("\nResumo:")
    print(f"Total de números pares: {pares}")
    print(f"Total de números ímpares: {impares}")



analisar_numeros()
