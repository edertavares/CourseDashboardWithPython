
import os
os.system("cls" if os.name == "nt" else "clear")  # Limpando a tela ao iniciar o programa
# Lista de filmes 
movieList = ["O Senhor dos Anéis", "Harry Potter", "Star Wars", "Matrix"]

# Iterando valores através do while
i = 0
while i < len(movieList):
    print(movieList[i])
    i += 1


print()  # Linha em branco para melhor visualização
# Quando a condição for atendida o loop será encerrado
i = 0
while i < len(movieList):
    if movieList[i] == "Star Wars":
        break
    print(movieList[i])
    i += 1

print()  # Linha em branco para melhor visualização
# Quando a condição for atendida o loop irá para a proxima iteração
i = 0
while i < len(movieList):
    if movieList[i] == "Star Wars":
        i += 1
        continue
    print(movieList[i])
    i += 1

# Avaliação do filme utilizando o while
print() # impriminto uma linha em branco
movieName = input("Digite o nome do filme que você assistiu: \n")
movieRate = int(input("Digite quantas avaliações deseja fazer: \n"))

i = 0
totalRate = 0
while i < movieRate:
    totalRate = int(input("Digite sua avaliação (1-5): \n"))
    i += 1


os.system("cls" if os.name == "nt" else "clear")  # Limpando a tela ao iniciar o programa
print(f"Obrigado por avaliar o filme '{movieName}'!")

if movieRate > 0:
    averageRate = totalRate / movieRate
    print(f"A média de avaliações para o filme '{movieName}' é: {averageRate:.2f}")
else:
    print("Nenhuma avaliação foi feita.")

