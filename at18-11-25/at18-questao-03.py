"""3 - Crie um programa que serve para calcular o preço final de um produto após aplicar um desconto percentual.
a - Cálculo de desconto: Calcula o valor do desconto baseado em uma porcentagem.
b - Preço final: Determina o novo preço após o desconto.
c - Formatação: Arredonda o resultado para 2 casas decimais (centavos).
d - Interação com usuário: Pede os valores necessários e mostra o resultado formatado.
"""


def calcular_desconto(preco: float, porcentagem: float) -> float:
    """
    Calcula o valor do desconto baseado em uma porcentagem.

    Parâmetros:
        preco (float): Preço original do produto.
        porcentagem (float): Percentual de desconto (ex.: 15 para 15%).

    Retorna:
        float: Valor do desconto.
    """
    if preco < 0:
        raise ValueError("O preço não pode ser negativo.")
    if porcentagem < 0:
        raise ValueError("A porcentagem de desconto não pode ser negativa.")
    return preco * (porcentagem / 100.0)


def preco_final(preco: float, porcentagem: float) -> float:
    """
    Determina o novo preço após o desconto.

    Retorna:
        float: Preço final após aplicar o desconto.
    """
    desconto = calcular_desconto(preco, porcentagem)
    return preco - desconto


def programa_desconto():
    """
    Interação com o usuário:
    - Solicita preço e porcentagem.
    - Exibe desconto e preço final formatados com 2 casas decimais.
    """
    try:
        preco_str = input("Digite o preço do produto (ex.: 199.90): ").strip().replace(",", ".")
        porcent_str = input("Digite a porcentagem de desconto (ex.: 15): ").strip().replace(",", ".")

        preco = float(preco_str)
        porcentagem = float(porcent_str)

        desc = calcular_desconto(preco, porcentagem)
        final = preco_final(preco, porcentagem)

        print(f"\nValor do desconto: R$ {desc:.2f}")
        print(f"Preço final: R$ {final:.2f}")
    except ValueError as e:
        print(f"Entrada inválida: {e}")


# Para executar como programa:
# if __name__ == "__main__":
#     programa_desconto()
