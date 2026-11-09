numeros = []

for i in range(10):
    numero = int(input("Digite um número inteiro: "))
    numeros.append(numero)

soma = 0
multiplicacao = 1

for i in range(10):
    if i % 2 == 1:
        soma += numeros[i]
    else:
        multiplicacao *= numeros[i]

print("Soma das posições ímpares:", soma)
print("Multiplicação das posições pares:", multiplicacao)