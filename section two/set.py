import os

os.system("cls" if os.name == "nt" else "clear")  # Limpando a tela ao iniciar o programa

filmSet = {"O Senhor dos Anéis - A Sociedade do Anel", "Harry Potter e a Pedra Filosofal", "Matrix Reloaded", "Matrix Revolutions", 
            "Harry Potter e a Câmara Secreta"}

print("Tipo de dados: ", type(filmSet))  # Exibindo o tipo da variável filmList
print()
# Buscar o tamanho do set
print("Contagem FilmSet", len(filmSet))  # Exibindo o número total de filmes na lista
print()
# Valor True e 1 são considerados o mesmo valor
exampleSet = {"Inception", True, 1, 2.5}
print("Contagem ExampleSet", len(exampleSet)) # exibindo o conjunto de exemplo
print("Valores exempleSet: ", exampleSet)  # Exibindo o conjunto de exemplo
print
# Adicionar ítens de outro set 
filmSet.update(exampleSet) #Atualizando o conjunto de filmes
print(filmSet)  # Exibindo a lista atualizada de filmes
print("Contagem de valores únicos FilmSet:", len(filmSet))
print
#Removendo ítens do Set
filmSet.discard("Inception")
print("Contagem de valores únicos FilmSet após remoção:", len(filmSet))
print("Valores FilmSet após remoção:", filmSet)  # Exibindo o conjunto de filmes após a remoção
print
# Testando o Remove
filmSet.remove(1)
print("Contagem de valores únicos FilmSet após remoção:", len(filmSet))
print("Valores FilmSet após remoção:", filmSet)  # Exibindo o conjunto de filmes após a remoção