import os

os.system("cls" if os.name == "nt" else "clear")  # Limpando a tela ao iniciar o programa

movieName = "Top Gun Maverick"
#String[inicio:fim] - índice começa na posiçõa 0 / índice final -1

print("Nome do filme:", movieName[0:]) # Exibindo o nome completo do filme ocultando o índice final 

#Buscar toda a string até a ultima posição
total = len(movieName)  # Obtendo o tamanho total da string
print("Total de caracteres no nome do filme:", total)   
print("Nome do filme:", movieName[0:total])  # Exibindo o nome completo do filme

# Buscar toda string da 3 a última posição 
line = "-" *100
print(line) #imprimindo a linha
print("Nome do filme:", movieName[3:])  # Exibindo o nome do filme a partir do índice 3
print(line)  # Imprimindo a linha novamente
#Buscar toda String de 2 em 2 caracteres
print("Nome do filme:", movieName[::2])  # Exibindo o nome do filme de 2 em 2 caracteres
print(line)  # Imprimindo a linha novamente
#buscar string nos índices impares
print("Nome do filme:", movieName[1::2])  # Exibindo o nome do filme nos índices ímpares
#inverter uma string 
print(line)  # Imprimindo a linha novamente
print("Nome do filme invertido:", movieName[::-1])  # Invertendo a string do nome do filme