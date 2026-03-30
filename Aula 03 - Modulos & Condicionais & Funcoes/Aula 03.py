import math

# Raiz de um numero

num = int(input("Digite um numero: "))
raiz = math.sqrt(num)
print(f"A raiz de {num} é {raiz}")

# Seno de um grau

graus = 30
radiano = graus / 180 * math.pi
seno = math.sin(radiano)
print(seno)

# Random

import random

randomNum = random.random()
print(randomNum)

intRandomNum = random.randint(1, 10)
print(intRandomNum)

randomRangeNum = random.randrange(1, 10)
print(randomRangeNum)