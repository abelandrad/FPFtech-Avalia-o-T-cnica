# 7 – Procurando palavras na diagonal principal

# Em Algelandia, o passatempo preferido são os jogos de Caça Palavras. Um destes tem as seguintes características:

# As palavras ocorrem apenas no sentido da diagonal principal; As palavras podem ocorrer com letras maiúsculas e/ou minúsculas; Se uma dada palavra existe, ela ocorre uma única vez e em qualquer posição da diagonal; As palavras podem existir tanto na forma normal quanto invertida, ou seja, a leitura da diagonal pode ocorrer na forma top-down ou bottom-up.

# Neste contexto, a figura abaixo demonstra como as palavras “workshop”, “videogame” e “scanner” podem ocorrer no jogo Figura abaixo. 

# Entrada

# A primeira linha contém três inteiros: 1) N que representa a quantidade palavras que iremos verificar se existem no jogo, limitado por [1,100]; 2) M que representa a quantidade de linhas da matriz, limitado por [10,1000]; 3) P que representa a quantidade de colunas da matriz, limitado por [10,1000]. Além disso, cada palavra N segue o limite: [6,100].

# Saída

# Conforme a existência de cada palavra N, informe:

# 1 Palavra "X" na diagonal principal 

# 2 Palavra "X" acima da diagonal principal 

# 3 Palavra "X" abaixo da diagonal principal 

# 4 Palavra "X" inexistente

# Onde X é a palavra procurada, além disso, X deve estar em lowercase.

# *
# 1 ponto


entrada = input().split()
num_palavras = int(entrada[0])
num_linhas = int(entrada[1])
num_colunas = int(entrada[2])
palavras = []

for _ in range(num_palavras):
    palavra = input().strip()
    palavras.append(palavra.lower())

matriz = []
for _ in range(num_linhas):
    linha = input().lower()[:num_colunas]
    matriz.append(list(linha))

matriz = matriz[::-1]
diagonais = []
for d in range(num_linhas + num_colunas - 1):
    diagonal_atual = ""
    for x in range(max(0, d - num_colunas + 1), min(num_linhas, d + 1)):
        diagonal_atual = matriz[x][d - x] + diagonal_atual
    diagonais.append(diagonal_atual)

nao_encontradas = []
encontradas = {}
for palavra in palavras:
    encontrada = False
    for i in range(len(diagonais)):
        if palavra in diagonais[i] or palavra[::-1] in diagonais[i]:
            encontrada = True
            if i == num_linhas - 1:
                encontradas[palavra] = 1
            elif i > num_linhas - 1:
                encontradas[palavra] = 2
            else:
                encontradas[palavra] = 3
    if not encontrada:
        nao_encontradas.append(palavra)

for palavra in nao_encontradas:
    print('4 Palavra "' + palavra + '" inexistente')

for palavra, posicao in encontradas.items():
    if posicao == 1:
        print(f'1 Palavra "{palavra}" na diagonal principal')
    elif posicao == 2:
        print(f'2 Palavra "{palavra}" acima da diagonal principal')
    else:
        print(f'3 Palavra "{palavra}" abaixo da diagonal principal')
