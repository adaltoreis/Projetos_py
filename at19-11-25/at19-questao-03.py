"""

3 - Crie um programa que consulte informações de um  na API , retorne logradouro, bairro, cidade e
 estado do CEP digitado, caso o CEP não existir ou houver erro na requisição, mostre uma mensagem de falha.

"""


# arquivo: consulta_cep.py
import requests
import re

def limpar_cep(cep: str) -> str:
    return re.sub(r"\D", "", cep)

def consultar_cep(cep: str):
    cep = limpar_cep(cep)
    if len(cep) != 8:
        print("Falha: CEP deve ter 8 dígitos.")
        return

    url = f"https://viacep.com.br/ws/{cep}/json/"
    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        dados = resp.json()

        if dados.get("erro"):
            print("Falha: CEP não encontrado.")
            return

        logradouro = dados.get("logradouro", "")
        bairro = dados.get("bairro", "")
        cidade = dados.get("localidade", "")
        estado = dados.get("uf", "")

        print(f"CEP: {cep}")
        print(f"Logradouro: {logradouro}")
        print(f"Bairro    : {bairro}")
        print(f"Cidade    : {cidade}")
        print(f"Estado    : {estado}")

    except requests.exceptions.Timeout:
        print("Falha: tempo de conexão excedido (timeout).")
    except requests.exceptions.ConnectionError:
        print("Falha: erro de conexão com a API.")
    except requests.exceptions.HTTPError as e:
        print(f"Falha HTTP: {e}")
    except Exception as e:
        print(f"Falha inesperada: {e}")

if __name__ == "__main__":
    cep = input("Digite o CEP (com ou sem máscara): ")
    consultar_cep(cep)
