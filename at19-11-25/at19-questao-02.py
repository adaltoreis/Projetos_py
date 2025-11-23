"""
2 -   Crie um programa que  acesse a API  para buscar um usuário fictício aleatório. exibindo o nome,
 e-mail e país desse usuário, caso houver erro na conexão, mostre uma mensagem de falha.

"""


# arquivo: usuario_aleatorio.py
import requests

URL = "https://randomuser.me/api/"

def buscar_usuario_aleatorio():
    try:
        resp = requests.get(URL, timeout=10)
        resp.raise_for_status()  # dispara erro para status HTTP 4xx/5xx
        dados = resp.json()

        resultado = dados.get("results", [])
        if not resultado:
            print("Falha: resposta sem resultados.")
            return

        usuario = resultado[0]
        nome = usuario.get("name", {})
        nome_completo = f"{nome.get('title', '').strip()} {nome.get('first', '').strip()} {nome.get('last', '').strip()}".strip()
        email = usuario.get("email", "sem e-mail")
        pais = usuario.get("location", {}).get("country", "país desconhecido")

        print("Usuário aleatório")
        print(f"Nome : {nome_completo}")
        print(f"E-mail: {email}")
        print(f"País : {pais}")

    except requests.exceptions.Timeout:
        print("Falha: tempo de conexão excedido (timeout).")
    except requests.exceptions.ConnectionError:
        print("Falha: erro de conexão com a API.")
    except requests.exceptions.HTTPError as e:
        print(f"Falha HTTP: {e}")
    except Exception as e:
        print(f"Falha inesperada: {e}")

if __name__ == "__main__":
    buscar_usuario_aleatorio()
