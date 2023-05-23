#############################################
#                                           #
# ALGORITMO DE CUADRADOS MEDIOS             #
#                                           #
#############################################

def AlgorithmMiddleSquare(seed: int, n: int) -> list:
    """seed: int || seed should be greater than 999
    n: int || n is cycle length"""
    r_i = []
    X_n = seed
    D = len(str(seed))
    if (D < 3):
        D = 4
    inf = D//2+int(D & 1)
    sup = (2*D)-(D//2)
    for i in range(n):
        X_n = X_n**2
        str_X_n = str(X_n)
        if len(str_X_n) < (2*D):
            str_X_n = "0"*((2*D)-len(str_X_n))+str_X_n
        str_X_n = str_X_n[inf:sup]
        X_n = int(str_X_n)  # X_n=Y_n pero no tiene sentido crear otra variable
        r_i.append(float(f"0.{str_X_n}"))

    return r_i


# print(AlgorithmMiddleSquare(57359, 100), sep="\t")

#############################################
#                                           #
# ALGORITMO DE PRODUCTOS MEDIOS             #
#                                           #
#############################################

def AlgorithmMiddleProduct(seed1: int, seed2: int, n: int) -> list:
    """seed1: int || seed1 should be greater than 999
    seed2: int || seed2 should be greater than 999
    seed1, seed2: should have the same number of digits
    n: int || n is cycle length"""
    r_i = []
    X_n, X_n2 = seed1, seed2
    D = len(str(seed1))
    if (D < 3):
        D = 4
    inf = D//2+int(D & 1)
    sup = (2*D)-(D//2)
    for i in range(n):
        X_n = X_n*X_n2
        str_X_n = str(X_n)
        if len(str_X_n) < (2*D):
            str_X_n = "0"*((2*D)-len(str_X_n))+str_X_n
        str_X_n = str_X_n[inf:sup]
        X_n, X_n2 = X_n2, int(str_X_n)
        r_i.append(float(f"0.{str_X_n}"))

    return r_i


# print(AlgorithmMiddleProduct(5015, 5734, 5))

#############################################
#                                           #
# ALGORITMO DE MULTIPLICADOR CONSTANTE      #
#                                           #
#############################################

def AlgorithmConstMultiplier(seed: int, multplier: int, n: int) -> list:
    """seed: int || seed should be greater than 999
    multiplier:int || multiplier should be greater than 999
    seed, multiplier: should have the same number of digits
    n: int || n is cycle length"""
    r_i = []
    X_n, A = seed, multplier
    D = len(str(seed))
    if (D < 3):
        D = 4
    inf = D//2+int(D & 1)
    sup = (2*D)-(D//2)
    for i in range(n):
        X_n = X_n*A
        str_X_n = str(X_n)
        if len(str_X_n) < (2*D):
            str_X_n = "0"*((2*D)-len(str_X_n))+str_X_n
        str_X_n = str_X_n[inf:sup]
        X_n = int(str_X_n)  # X_n=Y_n pero no tiene sentido crear otra variable
        r_i.append(float(f"0.{str_X_n}"))

    return r_i


# print(AlgorithmConstMultiplier(9803, 6965, 5))

#############################################
#                                           #
# ALGORITMO DE GLC                          #
#                                           #
#############################################

def AlgorithmGLC(a: int, x: int, c: int, m: int) -> list:
    """a:int || a is multiplier
    x:int || x is seed
    c:int || c is increment
    m:int || m is max cycle length"""
    pass
