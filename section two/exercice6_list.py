"""Exercício 6 - Listas
Escreva um programa que:
Leia 3 números inteiros.
Armazene esses números em uma lista.

Imprima:
A lista completa.
O primeiro elemento da lista.
A soma de todos os elementos da lista.
Exemplo
Entrada:
5
7
2
Saída:
[5, 7, 2]
5
14"""

import os

os.system("cls" if os.name == "nt" else "clear")  # Limpando a tela ao iniciar o programa

# Lendo 3 números inteiros
numeros = []
for i in range(3):
    num = int(input())
    numeros.append(num)

# Imprimindo a lista completa
print(numeros)

# Imprimindo o primeiro elemento da lista
print(numeros[0])

# Imprimindo a soma de todos os elementos da lista
print(sum(numeros))