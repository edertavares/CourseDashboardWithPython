import os

os.system("cls" if os.name == "nt" else "clear")  # Limpando a tela ao iniciar o programa

filmMatrix = ["Matrix Reloaded", 2003, 8.5, "true"]
print(filmMatrix)  # Exibindo a lista completa

filmList = ["O Senhor dos Anéis - A Sociedade do Anel", "Harry Potter e a Pedra Filosofal", "Matrix Reloaded", "Matrix Revolutions", 
            "Harry Potter e a Câmara Secreta"]
print(filmList)  # Exibindo a lista completa de filmes

# Buscando os dois primeiros filmes da lista
print(filmList[0:2])  # Exibindo os dois primeiros filmes

# Buscando o último ítem da lista 
print(filmList[-1])  # Exibindo o último filme da lista

# Buscar um filme até uma determinada posição
print(filmList[:3])  # Exibindo os filmes até a terceira posição

# Buscar um filme de uma posição em diante
print(filmList[1:4])  # Exibindo os filmes a partir da segunda posição