import statistics
import os

os.system('cls' if os.name == 'nt' else 'clear')

# 1 Aplicando a média
print(statistics.mean([3,2,3,8,9]))  # Imprime a média dos números na 

# 2 imprimindo média mediana
print(statistics.median([3,2,3,8,9]))  # Imprime a mediana dos números na lista 

# 3 Aplicando a moda
print(statistics.mode([3,2,3,8,9,3,2,3,3]))  # Imprime a moda dos números na lista

# 4 Desvio padrão
""" Quanto mais próximo de 0 for o desvio padrão, mais próximos os valores estão da média """
print(f"{statistics.stdev([3,2,3,8,9]):.2f}")  # Imprime o desvio padrão dos números na lista