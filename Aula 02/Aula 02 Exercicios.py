def question(text):
    print(text)
    return input("> ")

print("FIAP 16/03/2026 EXERCICIOS")
print("="*70)

print("EXERCICIO 01")

pi = 3.14159
raio = int(question("Qual o raio do circulo?"))
area = pi * raio ** 2

print(f"A area do circulo é {area}")

print("="*70)
print("EXERCICIO 02")

fahrenheit = int(question("Digite a temperatura em Fahrenheits"))
celsius = (fahrenheit - 32) * 5 / 9

print(f"A temperatura em Celsius é {celsius:.0f} graus.")

print("="*70)
print("EXERCICIO 04")

livros = int(question("Quantos livros você comprou?"))
canetas = int(question("Quantas canetas você comprou?"))

precoLivro = 25
precoCaneta = 5

gastoTotal = livros * precoLivro + canetas * precoCaneta

print(f"O total gasto foi R${gastoTotal:.2f}")

print("="*70)
print("EXERCICIO 05")

velocidade = int(question("Qual a velocidade do carro? (km/h)"))
distancia = int(question("Quantos kms o carro percorreu?"))

tempo = distancia / velocidade

print(f"O carro percorreu {distancia}km em {tempo:.0f} horas.")

print("="*70)
print("EXERCICIO 06")

nota1 = int(question("Qual a primeira nota?"))
nota2 = int(question("Qual a segunda nota?"))
media = (nota1 + nota2) / 2

print(f"A media do aluno é {media:.0f}")

print("="*70)
print("EXERCICIO 07")

notaA = int(question("Qual a primeira nota?"))
notaB = int(question("Qual a segunda nota?"))

mediaPonderada = (notaA * 4 + notaB * 6) / 2

print(f"A media ponderada é {mediaPonderada:.0f}.")
