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


