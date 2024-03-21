# 3 – LED

# João quer montar um painel de leds contendo diversos números. Ele não possui muitos leds, e não tem certeza se conseguirá montar o número desejado. Considerando a configuração dos leds dos números abaixo, faça um algoritmo que ajude João a descobrir a quantidade de leds necessário para montar o valor.

# Obs.: Para programadores de Javascript, recomenda-se o uso de "input.trim().split('\n')" para evitar erros conhecidos.

# Ver figura abaixo.

# Entrada

# A entrada contém um inteiro N, (1 ≤ N ≤ 1000) correspondente ao número de casos de teste, seguido de N linhas, cada linha contendo um número (1 ≤ V ≤ 10¹⁰⁰) correspondente ao valor que João quer montar com os leds.

# Saída

# Para cada caso de teste, imprima uma linha contendo o número de leds que João precisa para montar o valor desejado, seguido da palavra "leds".

n = int(input('Digite a quantidade de linhas: '))

for i in range(n):
    valor = int(input('Digite o valor que quer montar: '))
    soma = 0

    for digit in str(valor):
        if digit == '1':
            soma += 2
        elif digit == '2' or digit == '3':
            soma += 5
        elif digit == '4':
            soma += 4
        elif digit == '5':
            soma += 5
        elif digit == '6':
            soma += 6
        elif digit == '7':
            soma += 3
        elif digit == '8':
            soma += 7
        elif digit == '9':
            soma += 6
    print(soma, "leds")
