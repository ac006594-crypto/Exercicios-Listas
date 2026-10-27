
print("Algoritmo para calcular a média dos alunos")
print()

alunos = [0] * 5
soma = 0

# Ler os nomes e as notas dos alunos
for i in range(len(alunos)):
    nome = input(f"Digite o nome do {i + 1}º aluno: ")
    nota = float(input(f"Digite a nota de {nome}: "))

    alunos[i] = [nome, nota]
    soma += nota

# Calcular e apresentar a média
media = soma / 5

print("\nMédia da turma:", media)

# Listar os alunos com nota menor que 7
print("\n--- Alunos com nota menor que 7 ---")

for i in range(len(alunos)):
    if alunos[i][1] < 7:
        print(alunos[i][0])
