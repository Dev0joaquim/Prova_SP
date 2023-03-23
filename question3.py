import json

# Dados do faturamento mensal em formato JSON
dados = [
    {"dia": 1, "valor": 22174.1664},
    {"dia": 2, "valor": 24537.6698},
    {"dia": 3, "valor": 26139.6134},
    {"dia": 4, "valor": 0.0},
    {"dia": 5, "valor": 0.0},
    {"dia": 6, "valor": 26742.6612},
    {"dia": 7, "valor": 0.0},
    {"dia": 8, "valor": 42889.2258},
    {"dia": 9, "valor": 46251.174},
    {"dia": 10, "valor": 11191.4722},
    {"dia": 11, "valor": 0.0},
    {"dia": 12, "valor": 0.0},
    {"dia": 13, "valor": 3847.4823},
    {"dia": 14, "valor": 373.7838},
    {"dia": 15, "valor": 2659.7563},
    {"dia": 16, "valor": 48924.2448},
    {"dia": 17, "valor": 18419.2614},
    {"dia": 18, "valor": 0.0},
    {"dia": 19, "valor": 0.0},
    {"dia": 20, "valor": 35240.1826},
    {"dia": 21, "valor": 43829.1667},
    {"dia": 22, "valor": 18235.6852},
    {"dia": 23, "valor": 4355.0662},
    {"dia": 24, "valor": 13327.1025},
    {"dia": 25, "valor": 0.0},
    {"dia": 26, "valor": 0.0},
    {"dia": 27, "valor": 25681.8318},
    {"dia": 28, "valor": 1718.1221},
    {"dia": 29, "valor": 13220.495},
    {"dia": 30, "valor": 8414.61}
]

# Variáveis para armazenar o menor valor, maior valor e soma dos valores de faturamento diário
menor_valor = float("inf")
maior_valor = float("-inf")
soma_valores = 0.0

# Loop pelos dados de faturamento diário
for dado in dados:
    valor = dado["valor"]
    if valor != 0:
        # Atualiza o menor valor
        if valor < menor_valor:
            menor_valor = valor

        # Atualiza o maior valor
        if valor > maior_valor:
            maior_valor = valor

        # Soma o valor do faturamento diário para cálculo da média
        soma_valores += valor

# Cálculo da média de faturamento diário
dias_com_faturamento = sum(1 for dado in dados if dado["valor"] != 0)
media = soma_valores / dias_com_faturamento

# Contagem de dias com faturamento diário superior à média
dias_acima_da_media = sum(1 for dado in dados if dado["valor"] > media)

# Impressão dos resultados
