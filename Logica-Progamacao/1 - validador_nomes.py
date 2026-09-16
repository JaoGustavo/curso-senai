lista_alunos = []

for contador in range(1, 6):
    nome_aluno = input(f"Digite o nome do aluno {contador}: ")
    nome_formatado = nome_aluno.strip().title()

    if nome_formatado in lista_alunos:
        print("Aluno já cadastrado na lista!")
    else:
        lista_alunos.append(nome_formatado)

print("\nLista final de alunos cadastrados:")
print(lista_alunos)