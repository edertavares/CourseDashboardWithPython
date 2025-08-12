"""Escreva um programa que leia uma palavra e um número inteiro n.
O programa deve:

Imprimir a palavra duas vezes concatenada (sem espaço).

Imprimir a palavra repetida n vezes (usando multiplicação de string)."""

import os
line = "=" * 100

os.system("cls" if os.name == "nt" else "clear")  # Limpando a tela ao iniciar o programa

word = input("Digite uma palavra: \n")
n = int(input("Digite um número inteiro: \n"))
print(line)  # Imprimindo a linha de separação
print("Palavra concatenada duas vezes:", word + word)  # Imprimindo a palavra duas vezes concatenada
print("Palavra repetida n vezes:", word * n)  # Imprimindo a palavra repetida n vezes
