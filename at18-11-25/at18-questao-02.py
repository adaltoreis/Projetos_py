"""2-  Crie uma função que verifique se uma palavra ou frase é um palíndromo 
(lê-se igual de trás para frente, ignorando espaços e pontuação). Se o resultado é True, responda “Sim”,
 se o resultado for False, responda “Não”."""



import string

def eh_palindromo(texto: str) -> str:
    """
    Verifica se uma palavra ou frase é um palíndromo ignorando espaços e pontuação.
    Se True -> retorna 'Sim'
    Se False -> retorna 'Não'

    Regras:
      - Ignora espaços, pontuação e diferença entre maiúsculas/minúsculas.
      - Mantém letras e dígitos.

    Parâmetros:
        texto (str): A palavra ou frase a ser verificada.

    Retorna:
        str: 'Sim' se for palíndromo, 'Não' caso contrário.

    Exemplo:
        eh_palindromo("A grama é amarga!") -> 'Sim'
    """
    # Normaliza: remove pontuação e espaços, e coloca em minúsculas
    permitido = set(string.ascii_letters + string.digits + "áàâãäéèêëíìîïóòôõöúùûüçÁÀÂÃÄÉÈÊËÍÌÎÏÓÒÔÕÖÚÙÛÜÇ")
    filtrado = "".join(ch for ch in texto if ch in permitido)
    base = filtrado.lower()

    return "Sim" if base == base[::-1] else "Não"


# Exemplos:
# print(eh_palindromo("Socorram-me, subi no ônibus em Marrocos"))  # 'Sim'
