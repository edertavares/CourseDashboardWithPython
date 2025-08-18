"""Exercício 8 - Set
Escreva um programa que:

Leia cinco números inteiros (podendo haver repetidos).

Armazene-os em um set para eliminar duplicatas.

Imprima:

O set resultante.

A quantidade de elementos únicos.

O maior elemento do set.

Exemplo
Entrada:

4

7

4

9

7
"""
import os
os.system("cls" if os.name == "nt" else "clear")  # Limpando a tela ao iniciar o programa
filmSet = set()  # Inicializando um set vazio

for n in range(5): # Loop para ler 5 números inteiros
    num = int(input())
    filmSet.update({num}) # Adicionando o número ao set
    n += 1

print("Tipo de dados: ", type(filmSet))  # Exibindo o tipo da variável filmSet
print("Set resultante:", filmSet)
print("Quantidade de elementos únicos:", len(filmSet))
print("Maior elemento do set:", max(filmSet))