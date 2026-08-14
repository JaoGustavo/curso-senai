while True:
    idade = int(input("Digite uma idade entre 1 e 120: "))

    if idade <=120:
        break


if idade <= 10:
    print("Voce e crianca")

elif idade <= 17:
    print ("Voce e adolescente")

elif idade <= 60:
    print("Voce é adulto")

else:
    print("Voce é uma pessoa idosa")

