import math
import os

os.system('cls' if os.name == 'nt' else 'clear')

""" # 1 Acessar o número pi e imprimi-lo
print(math.pi)
print(f"{math.pi:.2f}")

# 2 Acesssar o número de Euler e imprimi-lo
print(math.e)   
print(f"{math.e:.2f}")

# 3 Arredondamento de números:
numero = 10.04
print(math.ceil(numero))  # Arredonda para cima
print(math.floor(numero)) # Arredonda para baixo

# 4 Cálculo de numero fatorial:
num2 = input("Digite um número inteiro:\n ")
print(math.factorial(int(num2)))  # Calcula o fatorial do número

# 5 Cálculo da potência:
base = int(input("Digite a base:\n "))
expoente = int(input("Digite o expoente:\n "))
print(math.pow(base, expoente))

# 6 Cálculo da raiz quadrada:
num3 = int(input("Digite um número para calcular a raiz quadrada:\n "))
print(math.sqrt(num3))  # Calcula a raiz quadrada do número 
print(f"{math.sqrt(num3):.2f}") """

# 7 MDC - Máximo Divisor Comum:
MDC = math.gcd(48, 64)
print(MDC)  # Imprime o valor do MDC entre 48 e 64

# 8 Logaritmos:
print(math.log(10))        # Logaritmo natural de 10