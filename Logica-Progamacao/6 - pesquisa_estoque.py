estoque = ["Multímetro", "Protoboard", "Resistor", "Multímetro", "Cabo", "Multímetro", "Protoboard"]

equipamento = input("Digite o nome do equipamento: ")
equipamento = equipamento.strip().title()

if equipamento in estoque:
    quantidade = estoque.count(equipamento)
    print("O item", equipamento, "aparece", quantidade, "vezes no estoque.")
else:
    print("Equipamento não encontrado no estoque!")