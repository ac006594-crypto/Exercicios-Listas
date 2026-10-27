print("Algoritmo para solicitar 12 valores e separar par de ímpar")
print()

valores = [0] * 12

for i in range(len(valores)):
    valores[i] = int(input(f"Digite o {i + 1}º valor: "))

# 1. Mostra apenas os pares
print("\n--- Todos os números PARES ---")
for i in range(len(valores)):
    if valores[i] % 2 == 0:
        print(valores[i])

# 2. Mostra apenas os ímpares
print("\n--- Todos os números ÍMPARES ---")
for i in range(len(valores)):
    if valores[i] % 2 != 0:
        print(valores[i])
