"""Exercício 7 - Tupla
Escreva um programa que:
Crie uma tupla com os nomes de três cidades lidas pelo usuário.

Imprima:
A tupla completa.
O último elemento da tupla.

A quantidade de elementos da tupla.
Exemplo
Entrada:
Recife
Salvador
Fortaleza
Saída:
('Recife', 'Salvador', 'Fortaleza')
Fortaleza
3"""

cidades = []
for i in range(3):
    cidade = input()
    cidades.append(cidade)

cidades = tuple(cidades)
print(cidades)
print(cidades[-1])
print(len(cidades))
print(type(cidades))
