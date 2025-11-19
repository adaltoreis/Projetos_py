""""
3 - Criar um código que serve para verificar se uma senha digitada pelo usuário atende a critérios básicos de segurança.
a - deve ter pelo menos 8 caracteres.
b - deve conter pelo menos um número.

-----------------------------------------

def verificar_senha():
    senha = input("Digite a senha: ")
    if len(senha) < 8:
        print("Senha muito curta! Deve ter pelo menos 8 caracteres.")
    elif not any(char.isdigit() for char in senha):
        print("Senha deve conter pelo menos um número.")
    else:
        print("Senha válida!")

verificar_senha()

--------------------------------------
"""

def verificar_senha(senha):
    """
    Função para verificar se uma senha atende aos critérios básicos de segurança:
    - Pelo menos 8 caracteres
    - Pelo menos um número
    """
    # Critério 1: Deve ter pelo menos 8 caracteres
    if len(senha) >= 8:
        print("Critério 1 OK: A senha tem pelo menos 8 caracteres.")
        criterio1 = True
    else:
        print("Critério 1 FALHOU: A senha deve ter pelo menos 8 caracteres.")
        criterio1 = False

    # Critério 2: Deve conter pelo menos um número
    tem_numero = any(char.isdigit() for char in senha)
    if tem_numero:
        print("Critério 2 OK: A senha contém pelo menos um número.")
        criterio2 = True
    else:
        print("Critério 2 FALHOU: A senha deve conter pelo menos um número.")
        criterio2 = False

    # Resultado final
    if criterio1 and criterio2:
        print("Senha válida!")
        return True
    else:
        print("Senha inválida! Corrija os critérios acima.")
        return False

# Exemplo de uso:
senha_usuario = input("Digite sua senha: ")
verificar_senha(senha_usuario)



