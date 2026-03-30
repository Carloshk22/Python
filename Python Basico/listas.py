nomes = []

for i in range(3):
    nome = input("Digite um nome: ")
    nomes.append(nome)

print("Nomes cadastrados:")

for nome in nomes:
    print("-", nome)