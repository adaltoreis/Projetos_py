"""
2 - Criar um código que registre as notas de alunos e calcular a média da turma.

"""

def media_turma():
    notas = []
    qtd = int(input("Quantos alunos? "))
    for i in range(qtd):
        nota = float(input(f"Digite a nota do aluno {i+1}: "))
        notas.append(nota)
    media = sum(notas) / len(notas)
    print(f"Média da turma: {media:.2f}")

media_turma()