nomes = []
idades = []

for i in range(7):
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))

    nomes.append(nome)
    idades.append(idade)

print("\nPessoas com 18 anos ou mais:")

for i in range(7):
    if idades[i] >= 18:
        print(nomes[i])