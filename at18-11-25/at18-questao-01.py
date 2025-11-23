"""1 - Crie uma função que calcule a gorjeta a ser deixada em um restaurante, baseada no valor total da conta e na porcentagem de
gorjeta desejada. Calcula o valor da gorjeta baseado no total da conta e na porcentagem desejada.
Parâmetros:
a - valor_conta (float): O valor total da conta
b - porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 10 para 10%)
c - retorna: float: O valor da gorjeta calculada"""


# arquivo: gerador_senha.py
import string
import secrets

def gerar_senha(tamanho: int) -> str:
    if tamanho < 4:
        raise ValueError("O tamanho deve ser pelo menos 4 para garantir variedade de caracteres.")

    # Conjuntos de caracteres
    minusculas = string.ascii_lowercase
    maiusculas = string.ascii_uppercase
    digitos = string.digits
    simbolos = string.punctuation

    # Garantir pelo menos 1 de cada categoria
    senha = [
        secrets.choice(minusculas),
        secrets.choice(maiusculas),
        secrets.choice(digitos),
        secrets.choice(simbolos),
    ]

    # Preencher o restante com qualquer categoria
    todos = minusculas + maiusculas + digitos + simbolos
    for _ in range(tamanho - 4):
        senha.append(secrets.choice(todos))

    # Embaralhar de forma segura
    secrets.SystemRandom().shuffle(senha)
    return "".join(senha)

def main():
    try:
        tamanho = int(input("Informe o tamanho da senha (>= 4): ").strip())
        senha = gerar_senha(tamanho)
        print(f"Senha gerada: {senha}")
        print("Dica: armazene senhas em um gerenciador confiável (ex.: 1Password, Bitwarden).")
    except ValueError as e:
        print(f"Entrada inválida: {e}")

if __name__ == "__main__":
    main()
