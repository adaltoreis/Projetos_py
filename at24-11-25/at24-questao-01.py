"""1 -  Crie um programa que lê um arquivo CSV de  com a biblioteca , calcule e exiba a  e o 
 da coluna tempo_execucao,  caso e o arquivo não exista ou houver erro na leitura, mostre uma mensagem de erro. """


# arquivo: calcula_estatisticas_csv_pandas.py
from pathlib import Path
import pandas as pd

def main():
    caminho = input("Informe o caminho do arquivo CSV: ").strip()
    arquivo = Path(caminho)

    try:
        if not arquivo.exists():
            raise FileNotFoundError(f"Arquivo não encontrado: {arquivo}")

        # Lê o CSV e tenta converter a coluna para numérico
        df = pd.read_csv(arquivo, encoding="utf-8")
        if "tempo_execucao" not in df.columns:
            raise KeyError("A coluna 'tempo_execucao' não existe no CSV.")

        serie = pd.to_numeric(df["tempo_execucao"], errors="coerce")  # coerce converte inválidos para NaN
        validos = serie.dropna()

        if validos.empty:
            print("Não há valores numéricos válidos na coluna 'tempo_execucao'.")
            return

        media = validos.mean()
        desvio = validos.std(ddof=1)  # desvio padrão amostral
        print(f"Média de tempo_execucao: {media:.4f}")
        print(f"Desvio padrão de tempo_execucao: {desvio:.4f}")

    except FileNotFoundError as e:
        print(f"Erro: {e}")
    except KeyError as e:
        print(f"Erro: {e}")
    except Exception as e:
        print(f"Falha ao ler/calcular: {e}")

if __name__ == "__main__":
    main()
