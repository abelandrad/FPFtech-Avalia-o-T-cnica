# 4 - Prefacio

# Desenvolva um programa que calcule o quociente e o resto da divisão de dois números inteiros. Lembre-se que o quociente e o resto da divisão de um inteiro a por um inteiro não-nulo b são respectivamente os únicos inteiros q e r tais que 0 ≤ r < |b| e:

# a = b × q + r

# Caso você não saiba, o teorema que garante a existência e a unicidade dos inteiros q e r é conhecido como ‘Teorema da Divisão Euclidiana’ ou ‘Algoritmo da Divisão’.

# Entrada

# A entrada é composta por dois números inteiros a e b (-1.000 ≤ a, b < 1.000).

# Saída

# Imprima o quociente q seguido pelo resto r da divisão de a por b.

a = int(input("Digite o dividendo:"))
b = int(input("Digite o divisor: "))

if b == 0:
    print("Não é possível dividir por zero.")
else:
    q = a // b
    r = a % b

    if r < 0:
        r += abs(b)
        q = (a - r) // b

    print(f"O quociente é {q} e o resto é {r}")
