temperaturas = [[28, 31, 34, 33], [25, 27, 29, 28], [32, 35, 36, 34], [24, 26, 25, 27]]
salaAtual = 0
maiorRisco = 0
salaMaiorRisco = 0

for sala in temperaturas:
    salaAtual += 1
    totalTemperaturas = len(sala)
    somaTemperaturas = 0
    registrosCriticos = 0

    for salaTemps in sala:
        somaTemperaturas += salaTemps
        if salaTemps >= 33:
            registrosCriticos += 1
    
    if maiorRisco < registrosCriticos:
        maiorRisco = registrosCriticos
        salaMaiorRisco = salaAtual

    mediaTemp = somaTemperaturas / totalTemperaturas

    print(f"Sala {salaAtual}")
    print(f"Média: {mediaTemp:.2f}")
    print(f"Registros críticos: {registrosCriticos}")
    print("")

print(f"Sala com maior risco: Sala {salaMaiorRisco}")
