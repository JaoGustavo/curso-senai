numero_secreto = 123
tentativas = 0

while True:

    palpite = int(input("Tente adivinhar o numero: "))
    tentativas += 1

    if palpite == numero_secreto:
        print("Acertou!")
        break


print("Tentativas:", tentativas)