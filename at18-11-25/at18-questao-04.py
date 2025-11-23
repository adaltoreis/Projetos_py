
"""4 - Crie um programa que calcule a quantos dias um individuo está vivo de acordo com a data do dia."""


from datetime import date, datetime

def dias_vivo(data_nascimento: date, data_referencia: date | None = None) -> int:
    """
    Calcula quantos dias um indivíduo está vivo.

    Parâmetros:
        data_nascimento (date): Data de nascimento.
        data_referencia (date | None): Data de referência (padrão: hoje).

    Retorna:
        int: Número de dias vivido (não negativo).

    Observações:
        - Considera anos bissextos automaticamente via datetime.
        - Se a data de nascimento for no futuro, retorna 0.
    """
    if data_referencia is None:
        data_referencia = date.today()

    if data_nascimento > data_referencia:
        return 0

    delta = data_referencia - data_nascimento
    return delta.days


def programa_dias_vivo():
    """
    Interação:
    - Solicita a data de nascimento no formato dd/mm/aaaa.
    - Exibe a quantidade de dias vividos até hoje.
    """
    entrada = input("Digite sua data de nascimento (dd/mm/aaaa): ").strip()
    try:
        # Suporta 'dd/mm/aaaa'
        nascimento = datetime.strptime(entrada, "%d/%m/%Y").date()
        total_dias = dias_vivo(nascimento)
        print(f"Você está vivo há {total_dias} dias.")
    except ValueError:
        print("Data inválida. Use o formato dd/mm/aaaa (ex.: 07/09/1995).")


# Para executar como programa:
# if __name__ == "__main__":
#     programa_dias_vivo()
