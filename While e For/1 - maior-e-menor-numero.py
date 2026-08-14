contador = 1
maior = 0
menor = 0

while contador <= 10:
    numero = float(input(f"Digite o {contador}º número: "))

    if contador == 1:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
            
    contador += 1

print(f"O maior valor digitado foi: {maior}")
print(f"O menor valor digitado foi: {menor}")