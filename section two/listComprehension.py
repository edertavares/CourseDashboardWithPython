import os
os.system('cls' if os.name == 'nt' else 'clear')

movieList = ["O Senhor dos Anéis", "Harry Potter", "Star Wars", "Matrix", "O Poderoso Chefão", "Pulp Fiction"] #criando uma lista dos principais filmes 
""" # Utilizando list comprehension para criar uma nova lista com os filmes em maiúsculas
upperMovieList = [movie.upper() for movie in movieList]
print(upperMovieList)  # Imprimindo a nova lista com os filmes em maiúsculas """

#1 Listando valores dentro de uma list compreehension 

""" numberList = [i for i in range(15) if i < 10] #criando uma lista com números de 0 a 14 e filtrando apenas os números menores que 10
print(numberList) #imprimindo a lista filtrada """

# 2 Filmes que possuem a letra "e" no Título
""" eMovieList = [movie for movie in movieList if 'x' in movie.lower()] #criando uma lista com os filmes que possuem a letra "e" no título, ignorando maiúsculas e minúsculas
print(eMovieList)  # Imprimindo a lista com os filmes que possuem a letra "e" """

# 3 Listando os filmes não assinstidos 
""" watchedMovies = ["Harry Potter", "Matrix"] #criando uma lista com os filmes que já foram assistidos
unwatchedMovies = [movie for movie in movieList if movie not in watchedMovies] #criando uma nova lista com os filmes que não foram assistidos
print(unwatchedMovies)  # Imprimindo a lista com os filmes não assistidos
 """

# 4 Encontrando um filme pleo nome
searchMovie = (input("Digite o nome do filme que deseja encontrar: ")) #pedindo para o usuário digitar o nome do filme que deseja encontrar
foundMovies = [movie for movie in movieList if searchMovie.lower() in movie.lower()] #criando uma nova lista com os filmes que possuem o nome digitado pelo usuário, ignorando maiúsculas e minúsculas
if foundMovies: #verificando se a lista não está vazia
    print("Filmes encontrados:")
    for movie in foundMovies:
        print(f"- {movie}")
else:
    print("Nenhum filme encontrado.")
# Imprimindo a lista com os filmes encontrados  