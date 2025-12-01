"""2 - Crie um programa que cria um arquivo  com nome, idade e
cidade de algumas pessoas, que este programa escreva os dados em formato tabular e
 salva no arquivo escolhido pelo usuário, caso ocorra um erro ao salvar, mostre uma mensagem de falha. """



# arquivo: cria_tabela_pessoas.py
from pathlib import Path
import pandas as pd

def obter_dados_exemplo():
    return [
        {"nome": "Ana", "idade": 28, "cidade": "Belém"},
        {"nome": "Bruno", "idade": 35, "cidade": "Marituba"},
        {"nome": "Carla", "idade": 22, "cidade": "Ananindeua"},
    ]

def main():
    destino = input("Informe o caminho do arquivo de saída (ex.: dados.xlsx ou dados.csv): ").strip()
    arquivo = Path(destino)

    dados = obter_dados_exemplo()
    df = pd.DataFrame(dados)

    try:
        if arquivo.suffix.lower() == ".xlsx":
            # Para Excel, use o engine openpyxl
            df.to_excel(arquivo, index=False, engine="openpyxl")
            print(f"Arquivo Excel salvo com sucesso em: {arquivo}")
        elif arquivo.suffix.lower() == ".csv":
            df.to_csv(arquivo, index=False, encoding="utf-8")
            print(f"Arquivo CSV salvo com sucesso em: {arquivo}")
        else:
            raise ValueError("Extensão não suportada. Use .xlsx ou .csv.")
    except Exception as e:
        print(f"Falha ao salvar o arquivo: {e}")

if __name__ == "__main__":
    main()

