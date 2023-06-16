"""RNG algorithms"""

#############################################
#                                           #
# ALGORITMO DE CUADRADOS MEDIOS             #
#                                           #
#############################################


def AlgorithmMiddleSquare(seed: int, n: int) -> list:
    """# Middle square RNG
    ## Non linear RNG
    ## Inputs
    seed: int || seed should be greater than 999
    n: int || cycle length
    ## Output
    list || n sized random number list"""
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
    """# Middle product RNG 
    ## Non linear RNG
    ## Inputs
    seed1: int || seed1 should be greater than 999
    seed2: int || seed2 should be greater than 999
    seed1, seed2: should have the same number of digits
    n: int || cycle length
    ## Output
    list || n sized random number list"""
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
    """# Middle Constant Multiplier RNG
    ## Non linear RNG
    ## Inputs
    seed: int || seed should be greater than 999
    multiplier:int || multiplier should be greater than 999
    seed, multiplier: should have the same number of digits
    n: int || cycle length
    ## Output
    list || n sized random number list"""
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


def AlgorithmLCG(a: int, x: int, c: int, m: int) -> list:
    """# Linear congruential generator 
    ## Linear RNG
    Common algorithm
    ## Inputs
    a:int || multiplier
    x:int || seed
    c:int || increment
    m:int || max cycle length
    ## Output
    list || m sized random number list. 

    LGC RNG could repeat numbers in a cycle acording to parameters"""
    r = []
    for i in range(m):
        x = ((a*x)+c) % m
        r_i = x/(m-1)
        r_i = float('%.6f' % r_i)  # 6 digits of significance
        r.append(r_i)
    return r


def AlgorithmLCG2(a: int, X_0: int, c: int, m: int) -> list:
    """# Linear congruential generator 
    ## Linear RNG
    Alternative algorithm
    ## Inputs
    a:int || multiplier
    x:int || seed
    c:int || increment
    m:int || max cycle length
    ## Output
    list || m sized random number list. 

    LGC RNG could repeat numbers in a cycle acording to parameters"""
    r = []
    for i in range(1, m+1):
        x = (((a**i)*X_0)+c*(a**i-1)/(a-1)) % m
        r_i = x/(m-1)
        r_i = float('%.6f' % r_i)  # 6 digits of significance
        r.append(r_i)
    return r


def SchrageLGC(a: int, x: int, m: int) -> list:
    """# Scharge's linear congruential generator
    ## Linear RNG
    Schrage method's is an alternative way to generate random numbers,

    and its outputs are similar to a LCG where c=0 if m is prime
    ## Inputs
    a:int || multiplier
    x:int || seed
    m:int || max cycle length
    ## Output
    list || m sized random number list. 

    Similar to LGC RNG, could repeat numbers in a cycle acording to parameters"""
    r = []
    Q = m//a
    R = m % a
    for i in range(m):
        g = a*(x % Q)-R*(x//Q)
        h = (x // Q)-((a*x)//m)
        x = g+m*h
        r_i = x/(m-1)
        r_i = float('%.6f' % r_i)  # 6 digits of significance
        r.append(r_i)
    return r
