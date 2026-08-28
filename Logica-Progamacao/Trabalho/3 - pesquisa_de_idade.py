criancas = 0
adolescentes = 0
adultos = 0
idosos = 0

for i in range(1, 11):
    idade = int(input("Digite a idade: "))
    
    if idade < 12:
        criancas =+ 1
    elif idade < 18:
        adolescentes =+ 1
    elif idade < 60:
        adultos =+ 1
    else:
        idosos =+ 1

print("Criancas:", criancas)
print("Adolescentes:", adolescentes)
print("Adultos:", adultos)
print("Idosos:", idosos)
