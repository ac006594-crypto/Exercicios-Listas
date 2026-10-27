print("Algoritimo para solicite 18 valores para o usuário e salve-os em um vetor e dar o resultado invertido ")
print()

valores = [0] * 18

#solicitar valores usuario 
for i in range(len(valores)):
    valores[i] = float(input(f"Digite o {i + 1}º valor: "))


# O [::-1] cria uma cópia da lista invertida para o loop
for i in range(len(valores[::-1])):
    # Acessa os valores já invertidos
    print(valores[::-1][i])
    print("-----")