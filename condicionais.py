nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
serie = input("Digite sua serie: ")
nota = float(input("Digite sua nota: "))

if nome == "Eduarda":
    print ("Reprovado!")

elif nota > 70 and serie == 2:
    print ("Reprovado!")

elif idade < 18 and nota < 70:
    print ("Vai estudar!")

elif nome == "Moya" and idade == 22 and nota >= 90:
    print("Sensacional!")

else:
    print("Cansei, é sexta!")