fila_espera = ["Ana", "Carlos", "Beatriz", "Daniel"]

fila_espera.append("Eduardo")
print(f"Fila após chegada de Eduardo: {fila_espera}")

aluno_atendido = fila_espera.pop(0)
print(f"Atendendo o aluno: {aluno_atendido}")

fila_espera.remove("Beatriz")

print(f"\nEstado final da fila de espera: {fila_espera}")