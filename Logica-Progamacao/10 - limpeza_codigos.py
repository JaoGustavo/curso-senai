codigos = [101, 102, 103, 104, 105, 106, 107]

del codigos[2]

codigo_removido = codigos.pop(-1)
print("Código removido:", codigo_removido)

codigos.clear()
print("Lista final:", codigos)