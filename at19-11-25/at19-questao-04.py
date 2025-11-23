"""
4 - Crie um programa que realize consultas a  em relação ao Real (BRL) usando a API mostre valor atual,
 máxima, mínima e data/hora da última atualização, caso a moeda não existir ou houver erro na requisição,
   retorne uma mensagem de erro.

"""

# arquivo: cambio_brl.py
import requests

BASE_URL = "https://economia.awesomeapi.com.br/json/last"

def consultar_cambio(moeda: str):
    moeda = moeda.strip().upper()
    if not moeda.isalpha() or len(moeda) != 3:
        print("Falha: informe o código da moeda com 3 letras (ex.: USD, EUR, GBP).")
        return

    url = f"{BASE_URL}/{moeda}-BRL"
    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        dados = resp.json()

        # A chave é algo como "USDBRL", "EURBRL"...
        chave = f"{moeda}BRL"
        info = dados.get(chave)

        if not info:
            print("Falha: moeda não encontrada ou resposta inválida.")
            return

        bid = info.get("bid")
        high = info.get("high")
        low = info.get("low")
        datahora = info.get("create_date")

        if None in (bid, high, low, datahora):
            print("Falha: dados incompletos na resposta da API.")
            return

        print(f"Câmbio {moeda}/BRL")
        print(f"Valor atual: {bid}")
        print(f"Máxima     : {high}")
        print(f"Mínima     : {low}")
        print(f"Última atualização: {datahora}")

    except requests.exceptions.Timeout:
        print("Falha: tempo de conexão excedido (timeout).")
    except requests.exceptions.ConnectionError:
        print("Falha: erro de conexão com a API.")
    except requests.exceptions.HTTPError as e:
        print(f"Falha HTTP: {e}")
    except Exception as e:
        print(f"Falha inesperada: {e}")

if __name__ == "__main__":
    moeda = input("Informe a moeda (ex.: USD, EUR, GBP): ")
    consultar_cambio(moeda)
