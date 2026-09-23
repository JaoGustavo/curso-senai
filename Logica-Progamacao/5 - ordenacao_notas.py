notas_turma = [5.5, 9.0, 2.5, 10.0, 7.2, 4.0]

nota_turmas.sort()
print("Ordem crescente", notas_turmas)

notas_turma.sort(reverse=True)
print("Ordem decrescente:", notas_turma)

print("Menor nota:", min(notas_turma))
print("Maior nota:", max(notas_turma))