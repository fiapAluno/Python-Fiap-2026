age = int(input("Qual sua idade? "))

if age < 16:
    print("Você não pode votar.")
else:
    if (age >= 16 and age < 18) or (age > 70):
        print("O seu voto é opcional")
    else:
        print("Você é obrigado a votar")