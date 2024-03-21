# 2 - Revisão de contrato

# Durante anos, todos os contratos da Associação de Contratos da Modernolândia (ACM) foram datilografados em uma velha máquina de datilografia.

# Recentemente Sr. Miranda, um dos contadores da ACM, percebeu que a máquina apresentava falha em um, e apenas um, dos dígitos numéricos. Mais especificamente, o dígito falho, quando datilografado, não é impresso na folha, como se a tecla correspondente não tivesse sido pressionada. Ele percebeu que isso poderia ter alterado os valores numéricos representados nos contratos e, preocupado com a contabilidade, quer saber, a partir dos valores originais negociados nos contratos, que ele mantinha em anotações manuscritas, quais os valores de fato representados nos contratos. Por exemplo, se a máquina apresenta falha no dígito 5, o valor 1500 seria datilografado no contrato como 100, pois o 5 não seria impresso. Note que o Sr. Miranda quer saber o valor numérico representado no contrato, ou seja, nessa mesma máquina, o número 5000 corresponde ao valor numérico 0, e não 000 (como ele de fato aparece impresso).

# Entrada

# A entrada consiste em diversos casos de teste, cada um em uma linha. Cada linha contém dois inteiros D e N (1 ≤ D ≤ 9, 1 ≤ N < 10¹⁰⁰ ), representando, respectivamente, o dígito que está apresentando problema na máquina e o número que foi negociado originalmente no contrato (que podem ser grande, pois Modernolândia tem sido acometida por hiperinflação nas últimas décadas).

# O último caso de teste é seguido por uma linha que contém apenas dois zeros separados por espaços em branco.

# Saída

# Para cada caso de teste da entrada o seu programa deve imprimir uma linha contendo um único inteiro V, o valor numérico representado de fato no contrato.

while True:    
    valor_contrato = ''
    digito_defeituoso, numero_original = input().split()
    if digito_defeituoso == '0' and numero_original == '0':
        print('0')
        break
    else:
        if numero_original == '0':
            valor_contrato = '0'
        else:
            for c in numero_original:
                if c != digito_defeituoso:
                    if valor_contrato != '0':
                        valor_contrato += c
        if valor_contrato == '':
            valor_contrato = ''
            print(valor_contrato)
        else:
            valor_contrato = int(valor_contrato)
            print(valor_contrato)