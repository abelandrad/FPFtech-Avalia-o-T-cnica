# 1 – Descriptografia

# Solicitaram para que você construísse um programa simples de descriptografia. Este programa deve possibilitar descriptografar mensagens codificadas que foram recebidas depois de serem criptografadas. O processo é muito simples. São feitas três passadas em todo o texto para a criptografia, e para descriptografar você deve fazer o processo inverso.

# Para criptografar, na primeira passada, somente caracteres que sejam letras minúsculas e maiúsculas devem ser deslocadas 3 posições para a direita, segundo a tabela ASCII: letra 'a' deve virar letra 'd', letra 'y' deve virar caractere '|' e assim sucessivamente. Na segunda passada, a linha deverá ser invertida. Na terceira e última passada, todo e qualquer caractere a partir da metade em diante (truncada) devem ser deslocados uma posição para a esquerda na tabela ASCII. Neste caso, 'b' vira 'a' e 'a' vira '`'.


# Por exemplo, se a entrada for “Texto #3”, o primeiro processamento sobre esta entrada deverá produzir “Wh{wr #3”. O resultado do segundo processamento inverte os caracteres e produz “3# rw{hW”. Por último, com o deslocamento dos caracteres da metade em diante, o resultado final deve ser “3# rvzgV”.


# Considere que o texto antes de passar pela criptografia, não contém os caracteres especiais ‘[’, ‘]’, ‘{’, ‘}’, ‘|’, ‘\’.

# Lembrando esse é o processo de criptografia, você deve fazer o processo inverso pra descriptografar o texto.

# Entrada

# A entrada contém vários casos de teste. A primeira linha de cada caso de teste contém um inteiro N (1 ≤ N ≤ 1*10⁴), indicando a quantidade de linhas que o problema deve tratar. As N linhas contém cada uma delas M (1 ≤ M ≤ 1*10³) caracteres.

# Saída

# Para cada entrada, deve-se apresentar a mensagem descriptografada.

n = int(input('Digite a quantidade de linhas: '))

for i in range(n):
    string = input('Digite o texto criptografado: ').strip()
    string_array = list(string)

    for j in range(len(string_array)):
        if string_array[j].isalpha():
            string_array[j] = chr(ord(string_array[j]) - 3)

    metade = len(string_array) // 2

    for k in range(metade, len(string_array)):
        if string_array[k] != " ":
            string_array[k] = chr(ord(string_array[k]) + 1)

    new_str = ''.join(string_array[::-1])

    print(new_str)
