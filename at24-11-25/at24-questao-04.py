"""4 -   Crie um programa que leia e escreva arquivos no formato , que salve em um dicionário
 com nome, idade e cidade em um arquivo JSON e depois leia o mesmo arquivo exibindo os dados, caso
 o arquivo não existir ou ocorrer erro ao salvar, mostre uma mensagem de falha."""


# arquivo: json_pessoas.py
from pathlib import Path
import json

def main():
    caminho = input("Informe o caminho do arquivo JSON (ex.: pessoa.json): ").strip()
    arquivo = Path(caminho)

    pessoa = {"nome": "Daniel", "idade": 30, "cidade": "Marituba"}

    # Escrever JSON
    try:
        with arquivo.open("w", encoding="utf-8") as f:
            json.dump(pessoa, f, ensure_ascii=False, indent=2)
        print(f"JSON salvo com sucesso em: {arquivo}")
    except Exception as e:
        print(f"Falha ao salvar o JSON: {e}")
        return

    # Ler JSON
    try:
        if not arquivo.exists():
            raise FileNotFoundError(f"Arquivo JSON não encontrado: {arquivo}")

        with arquivo.open("r", encoding="utf-8") as f:
            dados = json.load(f)
        print("Dados lidos do JSON:")
        print(f"Nome:  {dados.get('nome')}")
        print(f"Idade: {dados.get('idade')}")
        print(f"Cidade:{dados.get('cidade')}")
    except FileNotFoundError as e:
        print(f"Erro: {e}")
    except json.JSONDecodeError as e:
        print(f"Falha ao ler o JSON (formato inválido): {e}")
    except Exception as e:
        print(f"Falha ao ler o arquivo JSON: {e}")

if __name__ == "__main__":
    main()
