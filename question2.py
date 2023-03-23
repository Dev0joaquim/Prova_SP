# QUESTÃO 2)
number = int(input("Digite um número para verificar na sequência de Fibonacci: "))  # número a ser verificado na sequência de Fibonacci
a, b = 0, 1  # valores iniciais da sequência de Fibonacci

while b < number: #Eu tinha colocado <= e estava dando erro quando rodava o código (caia sempre no else), ainda bem que testei antes de enviar ;)
    a, b = b, a + b

if b == number:
    print(f"{number} pertence à sequência de Fibonacci!")
else:
    print(f"{number} não pertence à sequência de Fibonacci.");

# Nesse código, a variável number é definida pelo valor digitado pelo usuário (que precisa ser convertido de string para número inteiro).
# Os valores iniciais da sequência de Fibonacci (a e b) são definidos como 0 e 1, respectivamente. Daí, uso um laço de repetição (while) para calcular a sequência de Fibonacci até que o valor de b seja maior ou igual ao valor de numero.
# Se o valor de b for igual a numero, a mensagem "'número digitado' pertence à sequência de Fibonacci!" será exibida. Se não, a mensagem "'número digitado' não pertence à sequência de Fibonacci." que será exibida.




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
