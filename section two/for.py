# Listad de filmes 
import os

os.system("cls" if os.name == "nt" else "clear")  # Limpando a tela ao iniciar o programa

moviesList = [
    "O Senhor dos Anéis: A Sociedade do Anel",
    "Harry Potter e a Pedra Filosofal",
    "Star Wars: Episódio IV - Uma Nova Esperança",
    "Jurassic Park",
    "Matrix"
]

#  Iterando os valores de uma lista
for movie in moviesList:
    print(f"Filme: {movie}") # Exibindo o nome do filmes

print()  # Linha em branco para melhor visualização

# Quando a condição for atendida, o loop será encerrado. 
for movie in moviesList:
    print(f"Filme: {movie}") # Exibindo o nome do filmes
    if movie == "Star Wars: Episódio IV - Uma Nova Esperança":
        break  # Interrompendo o loop quando encontrar o filme "Star Wars"

print()  # Linha em branco para melhor visualização

#Quando a condição for atendida o loop irá para a próxima iteração.
for movie in moviesList:
    if movie == "Star Wars: Episódio IV - Uma Nova Esperança":
        continue  # Pulando a iteração quando encontrar o filme "Star Wars"
    print(f"Filme: {movie}") # Exibindo o nome do filmes

#Avaliação do filme 
movieName = input("Digite o nome do filme que você assistiu: \n")
movieRate = int(input("Digite quantas avaliações deseja fazer: \n"))

totalRate = 0
os.system("cls" if os.name == "nt" else "clear")  # Limpando a tela ao iniciar o programa
for i in range(movieRate):  # Loop para ler as avaliações
    rate = float(input(f"Digite a avaliação {i + 1} (de 0 a 10): \n"))
    totalRate += rate  # Somando as avaliações 

os.system("cls" if os.name == "nt" else "clear")  # Limpando a tela ao iniciar o programa
if movieRate > 0:
    averageRate = totalRate / movieRate
    print(f"A média de avaliações para o filme '{movieName}' é: {averageRate:.2f}")
else:
    print("Nenhuma avaliação foi feita.")