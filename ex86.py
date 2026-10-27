print("Algoritmo para contar quantas vezes X aparece no vetor")
print()

# 1. Criar o vetor com 10 posições
vetor = [0] * 10

# 2. Solicitar os 10 números inteiros ao usuário
for i in range(len(vetor)):
    vetor[i] = int(input(f"Digite o {i + 1}º valor inteiro: "))

print()

# 3. Solicitar o número X que será buscado
x = int(input("Digite o número X que deseja buscar no vetor: "))

# 4. Inicializar o contador de ocorrências
contador = 0

# 5. Percorrer o vetor e contar quantas vezes X aparece
for i in range(len(vetor)):
    if vetor[i] == x:
        contador += 1  # Soma 1 ao contador toda vez que encontra o número X

print()
print(f"O número {x} aparece {contador} vez(es) dentro do vetor.")
