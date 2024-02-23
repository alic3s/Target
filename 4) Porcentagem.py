faturamento_por_estado = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

total_mensal = sum(faturamento_por_estado.values())

percentuais_por_estado = {}
for estado, valor in faturamento_por_estado.items():
    percentual = (valor / total_mensal) * 100
    percentuais_por_estado[estado] = percentual

for estado, percentual in percentuais_por_estado.items():
    print("{}: {:.2f}%".format(estado, percentual))
