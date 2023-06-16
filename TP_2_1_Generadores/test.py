"""RNG quality tests"""

import numpy as np
from scipy.stats import ksone, norm, chi2
from math import sqrt, trunc
import matplotlib.pyplot as plt

"""Code from following functions are based on(but modified): https://github.com/nicolasf96/practica-simulacion-2022/blob/main/Generators/tests.py
https://github.com/nicolasf96/practica-simulacion-2022/blob/d2826666dce093daf6146f4bc6396f2adb049c21/Generators/tests.py
Authored by: Biscaldi-Iv, nicolasf96"""


def ChiSquareTest(sample: list, q: float, df: int) -> bool:
    """# Chisquare Test
    en: Chisquare Test
    es: Test Chicuadrado
    ## Hypotesis
    Null hypothesis: sample's RNG distribution is uniform
    Alternative hypothesis: sample's RNG distribution is not uniform
    ## Inputs
    sample:array-like
    q:float | confidence interval between 0 and 1
    df:int | Degrees of freedom
    ## output
    True: the sample pass the test, there is no evidence to reject null hypothesis
    False: the sample does not pass the test, there is evidence to reject null hypothesis"""
    # plt.hist() -> Devuelve la frecuencia absoluta de df+1 intervalos
    f_obs, *_ = plt.hist(sample, bins=df+1)
    k = len(f_obs)
    f_esp = len(sample)/k  # Frecuencia esperada en (bins) intervalos

    # Realizo el cálculo y la sumatoria de la fórmula de chi2
    chi2_list = []
    for i in range(df+1):
        num = ((f_obs[i] - f_esp)**2)/f_esp
        chi2_list.append(num)
    chi2_num = sum(chi2_list)  # chi**2

    # Este número lo debo comparar en la tabla de contingencia de chi2
    # Si es mayor al valor establecido en la tabla, dado un intervalo de confianza (q) y grados de libertad (df) -> entonces no cumple

    # Creo la tabla de chi2 dados tales parámetros q y df
    chi2_table = chi2.ppf(q=q, df=df)
    resultado = chi2_num < chi2_table
    return resultado


def KolmogorovTest(sample: list, alpha: float) -> str:
    """# KS Test
    Kolmogorov-Smirnov test compares cdf(critical value) of an uniform distribution with the cdf 
    of a n sized sample according to an alpha significance level
    ## Hypotesis
    Null hypothesis: sample's RNG distribution is uniform
    Alternative hypothesis: sample's RNG distribution is not uniform
    ## Inputs
    sample:array-like
    alpha:float | significance level between 0 and 1.

    Given alpha, confidence interval is 1-alpha
    ## Output
    True: the sample pass the test, there is no evidence to reject null hypothesis
    False: the sample does not pass the test, there is evidence to reject null hypothesis"""

    sample = sorted(sample)  # Ordeno la lista de menor a mayor
    d_positivo = []  # array de los valores calculados para d positivo con la fórmula de KS
    d_negativo = []  # array de los valores calculados para d negativo con la fórmula de KS
    N = len(sample)
    for i in range(N):
        I = i+1
        # Fórmula de KS para d positivo
        d_positivo.append(I / N - sample[i])
        # Fórmula de KS para d negativo
        d_negativo.append(sample[i] - (I - 1) / N)

    # Calculo el máximo entre los d
    dmaximo = max(max(d_positivo), max(d_negativo))
    # Tomo el valor crítico d de la tabla de KS
    k_tabla = ksone.ppf(1 - alpha / 2, N)
    return dmaximo < k_tabla


def AutocorrelationTest(sample: list) -> float:
    """# Autocorrelation Test
    en: Autocorrelation test
    es: Test de autocorrelacion
    Autocorrelation test searchs for correlation betwen numbers in the sample
    ## Hypotesis
    Null hypothesis: sample's RNG elements are independent
    Alternative hypothesis: sample's RNG elements are not independent
    ## Inputs
    sample: array-like
    ## Output
    float: autocorrelation coeficient"""
    N = len(sample)  # tamaño de la muestra
    Y = np.mean(sample)
    # se evalua la autocorrelacion cuando el lag es 1
    k = 1
    denom = sum([(sample[i]-Y)**2 for i in range(0, N)])
    numerator = sum([(sample[i]-Y)*(sample[i+k]-Y) for i in range(0, N-k)])
    autocorrelation = numerator/denom
    # en forma alternativa puede evaluarse autocorrelacion para todos los lags
    # a = []
    # for k in range(1, N):
    #     numerator = sum([(sample[i]-Y)*(sample[i+k]-Y) for i in range(0, N-k)])
    #     correlation = numerator/denom
    #     if correlation > 0.9:
    #         a.append([k, correlation])
    # return a
    return autocorrelation


def RunsTest(pseudo: list, alpha: float = .05) -> str:
    """# Runs test
    en: Runs test
    es: Test de rachas
    Runs test search for runs above or below median, if there are so numbers are not independent
    ## Hypotesis
    Null hypothesis: sample's RNG elements are independent
    Alternative hypothesis: sample's RNG elements are not independent
    ## Inputs
    sample: array-like
    alpha: float | significance level between 0 and 1.

    Given alpha, confidence interval is 1-alpha
    ## Output
    True: the sample pass the test, there is no evidence to reject null hypothesis
    False: the sample does not pass the test, there is evidence to reject null hypothesis"""
    media_est = np.mean(pseudo)
    sec = [1 if r > media_est else 0 for r in pseudo]
    c = 0
    for i in range(1, len(sec)-1):
        if sec[i-1] != sec[i]:
            c += 1
    n_0 = sec.count(0)
    n_1 = sec.count(1)
    nn2 = 2*n_0*n_1
    n = len(sec)
    mean_c = .5+(nn2/n)
    if n_1 == 0 or n_0 == 0:
        return False
    var_c = (nn2*(nn2-n))/((n**2)*(n-1))
    z = (c-mean_c)/sqrt(var_c)
    return abs(z) < norm.ppf(1-alpha/2)
