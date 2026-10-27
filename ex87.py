
print("Algoritmo para multiplicar os valores de dois vetores")
print()

X = [0] * 8
Y = [0] * 8

# Solicita os 8 valores do vetor X
print("--- Digite os valores do vetor X ---")
for i in range(len(X)):
    X[i] = int(input(f"Digite o {i + 1}º valor: "))

# Solicita os 8 valores do vetor Y
print("\n--- Digite os valores do vetor Y ---")
for i in range(len(Y)):
    Y[i] = int(input(f"Digite o {i + 1}º valor: "))

# Multiplica os valores das mesmas posições
print("\n--- Resultado das multiplicações ---")
for i in range(len(X)):
    resultado = X[i] * Y[i]
    print(f"Posição {i + 1}: {X[i]} x {Y[i]} = {resultado}")
