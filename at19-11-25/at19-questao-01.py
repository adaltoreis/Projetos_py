"""
1 - Crie um programa que gere senhas aleatórias com letras, números e símbolos e que o usuário 
 também escolha o tamanho da senha  para criar senhas seguras automaticamente.

"""

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
