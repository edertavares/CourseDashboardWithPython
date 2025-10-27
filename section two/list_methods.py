import os

os.system("cls" if os.name == "nt" else "clear")  # Limpando a tela ao iniciar o programa

filmList = ["O Senhor dos Anéis - A Sociedade do Anel", "Harry Potter e a Pedra Filosofal", "Matrix Reloaded", "Matrix Revolutions", 
            "Harry Potter e a Câmara Secreta"]

# exibindo o tamanho da lista 
print(len(filmList))  # Exibindo o número total de filmes na lista

# Recuperar um ítem da lista pelo nome
print(filmList.index("Matrix Reloaded"))  # Exibindo a posição do filme "Matrix Reloaded"

 #Adicionar um ítem ao final da lista
filmList.append("O Hobbit - Uma Jornada Inesperada")
print(filmList)  # Exibindo a lista atualizada de filmes

# Ordenar Lista
filmList.sort()
print(filmList)  # Exibindo a lista ordenada de filmes

# Realizando uma cópia da lista
filmListCopy = filmList.copy()
print(filmListCopy)  # Exibindo a cópia da lista de filmes

# Excluindo um ítem da lista
filmListCopy.remove("Matrix Reloaded")
print(filmListCopy)  # Exibindo a cópia da lista de filmes após a remoção

# Remove todos os ítens da lista
filmList.clear()
print(filmList)  # Exibindo a lista de filmes após limpar todos os ítens