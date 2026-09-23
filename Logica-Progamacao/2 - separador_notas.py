notas = [7.5, 4.0, 9.2, 5.5, 3.8, 10.0, 6.5, 2.0]

soma = sum(notas)
quantidade = len(notas)
media = soma / quantidade

print("A média da turma é:", media)

aprovados = []
recuperacao = []

for n in notas:
    if n > 6.0:
        aprovados.append(n)
    else:
        recuperacao.append(n)

print("Total de aprovados:", len(aprovados))
print("Total em recuperação:", len(recuperacao))