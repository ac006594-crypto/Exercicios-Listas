print("Algoritmo para ler idade de 7 pessoas")
print()

idade = [0] * 7

# Solicitar valores ao usuário
for i in range(len(idade)):
    idade[i] = int(input(f"Digite a {i + 1}ª idade: "))

print("\n--- Resultado da Verificação ---")

#
for i in range(len(idade)):
    if idade[i] >= 18:
        print(f"Pessoa {i + 1} ({idade[i]} anos): Você é maior de idade")
    else:
        print(f"Pessoa {i + 1} ({idade[i]} anos): Você é menor de idade")
    print("-----")
