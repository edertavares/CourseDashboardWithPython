import random
import os
os.system('cls' if os.name == 'nt' else 'clear')

#  Selecionando um valor aleatório de uma lista 
list1 = [1,2,3,4,5,6,7,8,9,10]
print("Valor aleatório selecionado: \n", random.choice(list1))

# Gerar um número aleatório em um intervalo de valores
r1 = random.randint(1, 100)
print("\nNúmero aleatório entre 1 e 100: \n", r1)

#  Seleciona um caractere aleatório de uma string
str1 = "Curso de Python"
r2 = random.choice(str1)
print("\nCaractere aleatório selecionado da string: \n", r2)

#  seleciona mais de um valor aleatório de uma lista
#  random.sample(sequencia, tamanho)
print(random.sample(list1, 2))
print(random.sample(list1, 3))
s = "Ola, mundo!"
print(random.sample(s, 2))

# Programa de sorteiro

done = False
while not done:
    print("\nO que você deseja fazer?")
    print("1 - Sortear um número")
    print("2 - Sair")

    choice = input("Digite sua escolha (1 ou 2):\n ")
    if choice == "1":
        rand_num = random.randint(1, 10)
        print(f"Número sorteado: {rand_num}")
    elif choice == "2":
        done = True
    else:
        print("Escolha inválida. Tente novamente.")
print("Programa encerrado.")