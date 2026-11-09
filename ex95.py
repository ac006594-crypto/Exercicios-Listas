nomes = []
notas = []

for i in range(5):
    nome = input("Digite o nome do aluno: ")
    nota = float(input("Digite a nota "))

    nomes.append(nome)
    notas.append(nota)

soma = 0

for nota in notas:
    soma += nota

media = soma / 5

print("\nMédia da turma:", media)

print("\nAlunos com nota menor que 7:")

for i in range(5):
    if notas[i] < 7:
        print(nomes[i])