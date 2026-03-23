def question(text, prefix):
    print(text)
    return input(f"> {prefix}")

print("FIAP 23/03/2026 CHECKPOINT")
print("="*70)

print("Exercicio 02")

produto = question("Qual o seu produto?", "")
preco = float(question("Qual o preço do produto?", "R$"))
quantidade = float(question(f"Quantos {produto}s você deseja comprar?", ""))
desconto = float(question("Qual o desconto da sua compra?", ""))

valorBruto = preco * quantidade
valorDesconto = valorBruto * (desconto * 0.01)
valorFinal = valorBruto - valorDesconto

print("-"*70)
print(f"Produto: {produto}")
print(f"Valor bruto: R${valorBruto:.2f}")
print(f"Desconto: R${desconto:.2f} ({desconto:.0f}%)")
print(f"Valor final: R${valorFinal:.2f}")
print("-"*70)
print("")

print("="*70)
print("Exercicio 03")

nome = question('Qual é o seu nome?', "")
valor_de_hora_de_trabalho = float(question('Quantas horas você trabalhou por dia?', ""))
DiasTrabalho = int(question('Quantos dias você trabalhou?', ""))

quantidade_de_horas_no_mes = valor_de_hora_de_trabalho * DiasTrabalho
bonus = float(question('Qual foi o seu bonus do mes?', ""))
desconto = float(question('Qual é o desconto total do mes?', ""))

ValorBruto = valor_de_hora_de_trabalho * quantidade_de_horas_no_mes + bonus
ValorLiquido =  ValorBruto * (desconto * 0.01)

print("-"*70)
print(f'Nome do colaborador: {nome}')
print(f'Horas trabalhadas por dia: {valor_de_hora_de_trabalho:.0f} horas')
print(f'Horas trabalhadas no mês: {quantidade_de_horas_no_mes:.0f} horas')
print(f'Bônus: R${bonus:.2f}')
print(f'Desconto: R${desconto:.2f} ({desconto:.0f}%)')
print(f'Seu salario bruto: R${ValorBruto:.2f}')
print(f'Seu salario liquido: R${ValorLiquido:.2f}')
print("-"*70)
