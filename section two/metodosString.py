import os

os.system("cls" if os.name == "nt" else "clear")  # Limpando a tela ao iniciar o programa

movieName = "Top Gun Maverick"
movieDescription = "Um piloto de caça precisa enfrentar seu passado enquanto treina uma nova geração de pilotos."

print(movieName.upper())  # Exibindo o nome do filme em letras maiúsculas
print(movieDescription.lower())  # Exibindo a descrição do filme em letras minúsculas   
print(movieName.title())  # Exibindo o nome do filme com a primeira letra de cada palavra em maiúscula
print(movieDescription.capitalize())  # Exibindo a descrição do filme com a primeira letra em maiúscula
print(movieName.center(10, "*"))    # Centralizando o nome do filme em uma largura de 10 caracteres, preenchendo com "*"
print(movieName.find("u")) # Encontrando a posição da letra "U" no nome do filme
print(movieDescription.find("o"))  # Encontrando a posição da palavra "o" no nome do filme
print(movieName.replace("Top", "Bottom"))  # Substituindo "Top" por "Bottom" no nome do filme