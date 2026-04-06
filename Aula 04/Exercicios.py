# Exercise 1 - Audio Player

import pygame
from contourpy.util.data import simple


# Exercise 2 - Pair or Odd Checker

def pair_or_odd(num):
    if num % 2 == 0:
        print(f"O numero {num} é par")
    elif num % 2 == 1:
        print(f"O numero {num} é impar")

# Exercise 3 - Highest number

def highest_number(num1, num2):
    if num1 == num2:
        print("Ambos numeros são iguais")
    elif num1 > num2:
        print(f"{num1} é maior que {num2}")
    elif num2 > num1:
        print(f"{num2} é maior que {num1}")

# Exercise 4 - Grades

def grades_media(grade1, grade2, grade3, grade4):
    media = (grade1 + grade2 + grade3 + grade4) / 4

    if media >= 7:
        print("Aprovado")
    elif media < 5:
        print("Reprovado")
    elif media >= 5 and media < 7:
        print("Em recuperação")

# Exercise 5 - Multiple numbers

def multiple_numbers(numA, numB):
    if numA % numB == 0 or numB % numA == 0:
        print("Os numeros são multiplos")
    else:
        print("Os numeros não são multiplos")

### Question Loader

def question_loader(questionNum):
    print(f"Carregando exercicio {questionNum}.")

    if questionNum == 2:
        num = int(input("Digite um numero: "))
        pair_or_odd(num)
    elif questionNum == 3:
        num1 = int(input("Digite o primeiro numero: "))
        num2 = int(input("Digite o segundo numero: "))
        highest_number(num1, num2)
    elif questionNum == 4:
        grade1 = float(input("Digite a primeira nota: "))
        grade2 = float(input("Digite a segunda nota: "))
        grade3 = float(input("Digite a terceira nota: "))
        grade4 = float(input("Digite a quarta nota: "))
        grades_media(grade1, grade2, grade3, grade4)
    elif questionNum == 5:
        numA = float(input("Digite o numero A: "))
        numB = float(input("Digite o numero B: "))
        multiple_numbers(numA, numB)
    else:
        print(f"Exercicio {questionNum} não finalizado.")

questionNum = int(input("Qual exercicio você quer carregar? "))
question_loader(questionNum)
