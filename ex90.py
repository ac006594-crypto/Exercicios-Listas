numeros = []

for i in range(18):
    numero = int(input("Digite um número inteiro: "))
    numeros.append(numero)

print("\nOrdem inversa:")

for numero in reversed(numeros):
    print(numero)