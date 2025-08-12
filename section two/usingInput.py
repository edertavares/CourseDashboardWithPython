#aprendendo a usar o imput
import os

os.system("cls" if os.name == "nt" else "clear")#limpando a tela ao iniciar o programa
name = input("Qual o nome do filme?\n")
yearLauche = int(input("Qual o ano de lançamento?\n"))
noteMove = float(input("Qual a nota do filme?\n"))
planIncluded = input("O plano está incluído? (True/False)\n")
movieDescription = """Top Gun Maverick é um filme de guerra, aventura e Ação"""
line = "="

#limpando a tela
os.system("cls" if os.name == "nt" else "clear")
print()  #linha em branco

#exibindo os dados na tela
print("O nome do filme é: " + name)
print("O ano de lançamento é: " + str(yearLauche))
print("A nota do filme é: " + str(noteMove))
print("O plano está incluído: " + planIncluded)
#multiplicação de string
print(line * 50)
print("A descrição do filme é: " + movieDescription)
#procurar uma palavra dentro do texto

print("Top" in name)  #verificando se a palavra "Top" está no nome do filme
print("Gun" in movieDescription)  #verificando se a palavra "Gun" está na descrição do filme

print()  #linha em branco
print("Exibindo o tipo de dados: \n")
#exibindo os tipos dos dados na tela
print((type(name)))
print((type(yearLauche)))
print((type(noteMove)))
print((type(planIncluded)))
print((type(movieDescription)))