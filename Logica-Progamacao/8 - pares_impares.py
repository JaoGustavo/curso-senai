numeros = []

for i in range(8):
    numero = int(input("Digite um número inteiro: "))
    numeros.append(numero)

pares = []
impares = []

for n in numeros:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

pares.sort()
impares.sort()

print("Números pares:", pares)
print("Números ímpares:", impares)