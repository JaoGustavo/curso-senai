quantidade = int(input("Quantos produtos serão cadastrados? "))


total_compra = 0
produto_mais_caro = ""
maior_preco = 0

for i in range:
    print(f"\n--- {i}º PRODUTO ---")
    nome = input("Nome do produto: ")
    preco = float(input("Preço do produto: R$ "))

    total_compra += preco

    if i == 1 or preco > maior_preco:
        maior_preco = preco
        produto_mais_caro = nome

print(f"Valor total da compra: R$ {total_compra:.2f}")
print(f"Produto mais caro: {produto_mais_caro} (R$ {maior_preco:.2f})")