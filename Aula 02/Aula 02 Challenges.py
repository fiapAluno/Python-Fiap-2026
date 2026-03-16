from scipy.sparse import diags

def question(text):
    print(text)
    return input("> ")

print("FIAP 16/03/2026 CHALLENGES")
print("="*70)

print("CHALLENGE 01")

name = question("Insira seu nome")
print(f"Bem-vindo {name}")

print("="*70)
print("CHALLENGE 02")

dia = int(question("Que dia você nasceu?"))
mes = int(question("Que mês você nasceu?"))
ano = int(question("Que ano você nasceu?"))

print(f"Você nasceu na data {dia}/{mes}/{ano}")

print("="*70)
print("CHALLENGE 03")

print("CALCULADORA PYTHON")
num1 = int(question("Digite o primeiro numero da soma"))
num2 = int(question("Digite o segundo numero"))
soma = num1 + num2

print(f"A soma dos números é {soma}.")
