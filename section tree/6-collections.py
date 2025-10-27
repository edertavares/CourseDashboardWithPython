from collections import Counter, namedtuple, deque
from operator import itemgetter
import os

os.system('cls' if os.name == 'nt' else 'clear')

#  Lista de fruatas (Contagem)

fruits = ['apple', 'banana', 'orange', 'apple', 'orange', 'banana', 'apple']
print("Lista de frutas:\n", fruits)
print("Contagem de frutas:\n", Counter(fruits))

os.system('cls' if os.name == 'nt' else 'clear')
# Named Tuple (Tupla Nomeada)
game = namedtuple('game', ['name','price', 'note'])
g1 = game('The Last of Us', 150, 9.5)
g2 = game('God of War', 200, 9.7)
print("\nJogo 1:", g1)  
print("Jogo 2:", g2)

# ordenando dicionários 
students = {"Pedro": 22, "Ana": 20, "Maria": 21, "João": 23}
a = sorted(students.items(), key = itemgetter(0)) # ordena por chave
print(a)

#  utilizando deque (double-ended queue)
deq = deque([20, 40, 60, 80, 100])
print("\nDeque inicial:", deq)
deq.appendleft(10)
print("\nDeque após appendleft(10):", deq)
deq.append(90)
deq.popleft()
print("Deque após append(90) e popleft():", deq)
deq.pop()
print("Deque após pop():", deq)