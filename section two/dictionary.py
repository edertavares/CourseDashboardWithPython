import os

os.system("cls" if os.name == "nt" else "clear")  # Limpando a tela ao iniciar o programa

filmInception = {
    "title": "Inception",
    "director": "Christopher Nolan",
    "year": 2010,
    "genre": ["Sci-Fi", "Thriller", "Action"],
    "rating": 8.8
}

print("Tipo de dados: \n", type(filmInception))  # Exibindo o tipo da variável filmInception
print("Quantidade de registros no dicionário: \n", len(filmInception))  # Exibindo o número total de chaves no dicionário
print()
print("Dados do dicionário: \n  ")
print(filmInception)  # Exibindo o dicionário completo