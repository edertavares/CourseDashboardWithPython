import hashlib
import os

os.system('cls' if os.name == 'nt' else 'clear')

# Verificar os algoritmos de hash disponíveis
print("Algoritmos de hash disponíveis:")
print(hashlib.algorithms_available)

# verificar algoritimos de acordo com sistema operacional
print(hashlib.algorithms_guaranteed)

#  utilizando o sha256
algorithm = hashlib.sha256()
print("Saída do algoritmo: \n")
print(algorithm.digest())
message = "A melhor forma de prever o futuro é criá-lo.".encode()
algorithm.update(message)
print(algorithm.hexdigest())

#utilizando o md5
md5 = hashlib.md5()
print("Saída do algoritmo: \n")
print(md5.digest())
md5.update(message)
print(md5.hexdigest())  