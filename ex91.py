numeros = []

for i in range(12):
    numero = int(input("Digite um número inteiro: "))
    numeros.append(numero)

print("\nNúmeros pares:")

for numero in numeros:
    if numero % 2 == 0:
        print(numero)

print("\nNúmeros ímpares:")

for numero in numeros:
    if numero % 2 != 0:
        print(numero)