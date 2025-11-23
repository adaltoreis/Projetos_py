"""1 - Crie uma função que calcule a gorjeta a ser deixada em um restaurante, baseada no valor total da conta e na porcentagem de
gorjeta desejada. Calcula o valor da gorjeta baseado no total da conta e na porcentagem desejada.
Parâmetros:
a - valor_conta (float): O valor total da conta
b - porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 10 para 10%)
c - retorna: float: O valor da gorjeta calculada"""

def calcular_gorjeta(valor_conta: float, porcentagem_gorjeta: float) -> float:
    
    if valor_conta < 0:
        raise ValueError("O valor da conta não pode ser negativo.")
    if porcentagem_gorjeta < 0:
        raise ValueError("A porcentagem de gorjeta não pode ser negativa.")

    return valor_conta * (porcentagem_gorjeta / 100.0)


# Exemplo rápido:
# print(calcular_gorjeta(250.00, 12))  # Saída: 30.0
