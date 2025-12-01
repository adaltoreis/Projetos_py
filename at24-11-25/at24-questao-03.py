"""3 -  Crie um programa que leia um arquivo  informado pelo usuário, percorrendo cada linha do arquivo e a exibe na tela, caso 
o arquivo não seja encontrado, mostre uma mensagem de erro."""


# arquivo: le_arquivo_texto.py
from pathlib import Path

def main():
    caminho = input("Informe o caminho do arquivo de texto (.txt): ").strip()
    arquivo = Path(caminho)

    try:
        if not arquivo.exists():
            raise FileNotFoundError(f"Arquivo não encontrado: {arquivo}")

        with arquivo.open("r", encoding="utf-8") as f:
            for i, linha in enumerate(f, start=1):
                print(f"{i:03d}: {linha.rstrip()}")  # mostra número da linha
    except FileNotFoundError as e:
        print(f"Erro: {e}")
    except Exception as e:
        print(f"Falha na leitura: {e}")

if __name__ == "__main__":
    main()
