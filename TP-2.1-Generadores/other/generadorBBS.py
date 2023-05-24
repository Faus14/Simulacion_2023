import math

def bbs(p, q, seed, n):
    # Inicialización
    m = p * q
    x = seed
    result = []

    # Generación de n números pseudoaleatorios
    for i in range(n):
        x = pow(x, 2, m)  # x_n = x_n-1^2 mod m
        bit = x % 2
        result.append(bit)

    return result

# Ejemplo de uso
p = 24672462467892469787
q = 396736894567834589803
seed = 1234567890
n = 10

bits = bbs(p, q, seed, n)
print(bits)
