print("Algoritimo para solicite 11 valores para o usuário e salve-os em um vetor ")
print()

valores = [0] * 11

#solicitar valores usuario 
for i in range(len(valores)):
    valores[i] = float(input(f"Digite o {i + 1}º valor: "))

print()

for i in range(len(valores)):
    print(valores[i])
    print("-----")