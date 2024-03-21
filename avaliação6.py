# 6 - Compressor

# Sua tarefa é comprimir uma string de no máximo 200 caracteres, usando o seguinte esquema:

# - Adjacentes que se repetem: [S]k que significa: S repetido k vezes (onde k é um número inteiro de um byte, lembre-se que o comprimento da String não excede 200).

# - Repete com lacunas: [S]k{S_1}t_1{S_2}t_2...{S_r}, onde 1 ≤ t_i < k, t_i < t_{i+1} que significa: escrever S para k vezes, em seguida, introduza a String S_i após a t_i ocorrência de S.

# Note que a compressão é feita de forma recursiva, para S, S_1, ..., S_r mencionado acima, onde tudo pode ser comprimido.

# Por exemplo: para a string original

# I_am_WhatWhat_is_WhatWhat

# O resultado ideal seria:

# I_am_[What]4{_is_}2

# Entrada

# Há, no máximo, 20 casos de teste, cada caso de teste é uma string contendo não mais do que 200 caracteres imprimíveis, sem espaços em branco (ou seja, sem espaços e sem tabulações), colchetes (ou seja, não há {'(', ')', '[','] ',' {','} '}) e nem dígitos. As letras são case-sensitive.

# *
# 1 ponto

# Obs: Bati muita cabeça tentando solucionar essa questão, fiz várias pesquisas, aprendi sobre regex e tentei implementar na questão. Infelizmente no momento atual ainda não fui capaz de solucionar esse problema. 
# Irei estudar mais a fundo sobre expressões regulares e logo mais serei capaz de solucionar a questão. Mas se quiser testar só o último exemplo de entrada ele funciona perfeitamente haha :D

import re
from collections import Counter

def split_string(input_string):
    if len(set(input_string)) == 1:
        first_char = input_string[0]
        k = len(input_string)
        output = f'{len(f"[{first_char}]{k}")} [{first_char}]{k}'
        return output
    elif '_' in input_string and any(char.isupper() for char in input_string):
        substrings = re.findall(r'(?<=[a-z])_(?=[A-Z])|[A-Z][a-z]*', input_string)
        return substrings
    else:
        return [input_string]

input_str = input("")
print(split_string(input_str))


