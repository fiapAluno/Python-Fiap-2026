# Audio Player

# Pair or Odd Checker

def pair_or_odd(num):
    if num % 2 == 0:
        print(f"O numero {num} é par")
    elif num % 2 == 1:
        print(f"O numero {num} é impar")

num_pair_or_odd = int(input("Digite um numero: "))
pair_or_odd(num_pair_or_odd)

# Highest number

def highest_number(num1, num2):
    if num1 == num2:
        print("Ambos numeros são iguais")
    elif num1 > num2:
        print(f"{num1} é maior que {num2}")
    elif num2 > num1:
        print(f"{num2} é maior que {num1}")

num1_highest_number = int(input("Digite o primeiro numero: "))
num2_highest_number = int(input("Digite o segundo numero: "))
highest_number(num1_highest_number, num2_highest_number)

# Grades

def grades_media(grade1, grade2, grade3, grade4):
    media = (grade1 + grade2 + grade3 + grade4) / 4

    if media >= 7:
        print("Aprovado")
    elif media < 5:
        print("Reprovado")
    elif media >= 5 and media < 7:
        print("Em recuperação")

grade1_grades_media = float(input("Digite a primeira nota: "))
grade2_grades_media = float(input("Digite a segunda nota: "))
grade3_grades_media = float(input("Digite a terceira nota: "))
grade4_grades_media = float(input("Digite a quarta nota: "))
grades_media(grade1_grades_media, grade2_grades_media, grade3_grades_media, grade4_grades_media)

#