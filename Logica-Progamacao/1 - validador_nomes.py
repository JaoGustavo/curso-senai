alunos = []

for i in range(5):
    nome = input("Digite o nome do aluno: ")
    

    nome = nome.strip()
    nome = nome.title()
    
    if nome in alunos:
        print("Aluno já cadastrado na lista!")
    else:
        alunos.append(nome)

print("Lista final:")
print(alunos)