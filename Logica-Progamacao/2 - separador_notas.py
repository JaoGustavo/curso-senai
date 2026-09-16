lista_notas = [7.5, 4.0, 9.2, 5.5, 3.8, 10.0, 6.5, 2.0]

media_turma = sum(lista_notas) / len(lista_notas)
print(f"Média da turma: {media_turma:.2f}")

lista_aprovados = []
lista_recuperacao = []

for nota_atual in lista_notas:
    if nota_atual >= 6.0:
        lista_aprovados.append(nota_atual)
    else:
        lista_recuperacao.append(nota_atual)

print(f"\nTotal de aprovados: {len(lista_aprovados)}")
print(f"Total em recuperação: {len(lista_recuperacao)}")