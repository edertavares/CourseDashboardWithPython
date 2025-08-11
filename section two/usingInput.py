#aprendendo a usar o imput
import os

name = input("Qual o nome do filme?\n")
yearLauche = input("Qual o ano de lançamento?\n")
noteMove = input("Qual a nota do filme?\n")
planIncluded = input("O plano está incluído? (True/False)\n")

os.system("cls" if os.name == "nt" else "clear")
print()  #linha em branco

#exibindo os dados na tela
print("O nome do filme é: " + name)
print("O ano de lançamento é: " + yearLauche)
print("A nota do filme é: " + noteMove)
print("O plano está incluído: " + planIncluded)