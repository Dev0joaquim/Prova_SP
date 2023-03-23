# QUESTÃO 5)
# ler a string de entrada do usuário
input = input("Digite uma string: ")

# converter a string em lista para manipulação dos caracteres
list = list(input)

# inverter os caracteres da lista
for i in range(len(list) // 2):
    temp = list[i]
    list[i] = list[-i - 1]
    list[-i - 1] = temp

# converter a lista de volta para string
output = "".join(list)

# imprimir a string invertida
print(output)
