#
#
# GENERADOR DE MEDIA DE CUADRADOS
#
#


def MediaCuadrados(seed: int, n: int) -> list:
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
        if (int(str_X_n) == 0):
            break
    return r_i


print(MediaCuadrados(57359, 100), sep="\t")
