
print("Algoritmo para solicitar 10 valores inteiros")
print()

valores = [0] * 10

for i in range(len(valores)):
    valores[i] = int(input(f"Digite o {i + 1}º valor: "))

soma = 0
multiplicacao = 1

for i in range(len(valores)):
    if (i + 1) % 2 != 0:
        soma += valores[i]
    else:
        multiplicacao *= valores[i]

print("\nSoma dos valores nas posições ímpares:", soma)
print("Multiplicação dos valores nas posições pares:", multiplicacao)
