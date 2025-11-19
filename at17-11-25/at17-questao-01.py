"""1 - Criar um código que faça uma calculadora que tenha as operações básicas(+,-,*,/).
"""
def calculadora():
    print("Operações disponíveis: +, -, *, /")
    op = input("Escolha a operação: ")
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if op == '+':
        print(f"Resultado: {num1 + num2}")
    elif op == '-':
        print(f"Resultado: {num1 - num2}")
    elif op == '*':
        print(f"Resultado: {num1 * num2}")
    elif op == '/':
        if num2 != 0:
            print(f"Resultado: {num1 / num2}")
        else:
            print("Erro: divisão por zero!")
    else:
        print("Operação inválida!")

calculadora()


