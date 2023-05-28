from generadores import AlgorithmConstMultiplier, AlgorithmMiddleSquare, AlgorithmMiddleProduct, AlgorithmLCG, AlgorithmLCG2, SchrageLGC
from test import AutocorrelationTest, RunsTest, KolmogorovTest, ChiSquareTest
from scipy.stats import uniform, kstest
from time import perf_counter
import matplotlib.pyplot as plt
from matplotlib.offsetbox import AnchoredText
import random


def SaveHist(rn: list, rn_name: str, params: dict) -> None:
    fig, ax = plt.subplots()
    l = ''
    for key, value in params.items():
        l += f'{key}={value}\n'
    interv, *_ = ax.hist(rn, bins=20, edgecolor="white", linewidth=3)
    # at = AnchoredText(l, prop=dict(size=15), frameon=True, loc='upper right')
    # at.patch.set_boxstyle("Square,pad=0.2")
    # ax.add_artist(at)
    y = max(interv)
    ax.set_ylim(ymax=int(1.2*max(interv)))
    plt.text(1, int(1.1*max(interv)), l, fontsize=10, ha='right', va='top')
    plt.title(f'Histograma -{rn_name}')
    plt.xlabel('Valor del numero generado')
    plt.ylabel('Cantidad de elementos en el intervalo')
    rn_name.replace(' ', '_')
    plt.savefig(f'{rn_name}.png')
    plt.clf()


IC = 0.975
ALPHA = 0.05
DoF = 9
random.seed(53)

start = perf_counter()
RNGPY = [random.random() for i in range(10000)]
end = perf_counter()-start
print(f"Performance RNGPY: t={end} t/n={end/10000}")

# Non LGC Random Number Generators
start = perf_counter()
CM = AlgorithmConstMultiplier(seed=573592, multplier=697613, n=10000)
end = perf_counter()-start
print(f"Performance Const: t={end} t/n={end/10000}")

start = perf_counter()
MS = AlgorithmMiddleSquare(seed=624867, n=10000)
end = perf_counter()-start
print(f"Performance Square: t={end} t/n={end/10000}")

start = perf_counter()
MP = AlgorithmMiddleProduct(seed1=358129, seed2=679452, n=10000)
end = perf_counter()-start
print(f"Performance Prod: t={end} t/n={end/10000}")

# LGC Random Number Generators

# Family 1: c=0, m is prime

mersenne = (2**13)-1  # =8191
start = perf_counter()
LGC1 = AlgorithmLCG(a=7345, x=4698, c=0, m=mersenne)
end = perf_counter()-start
print(f"Performance LGC1: t={end} t/n={end/mersenne}")

start = perf_counter()
SCH = SchrageLGC(a=7345, x=4698, m=mersenne)
end = perf_counter()-start
print(f"Performance Scharge: t={end} t/n={end/mersenne}")

# start = perf_counter()
# LGC1A = AlgorithmLCG2(a=7345, X_0=4698, c=0, m=mersenne) #No soporta la ultima iteracion
# end = perf_counter()-start
# print(f"Performance LGC: {end}")

# print(f"LGC1 == SCH :{LGC1 == SCH}")  # True
# print(f"{LGC1 == LGC1A=}")  # ?

# Family 2: c=0, m is 2**X
start = perf_counter()
LGC2 = AlgorithmLCG(a=3333, x=8011, c=0, m=2**13)
end = perf_counter()-start
print(f"Performance LGC2: t={end} t/n={end/(2**13)}")

# Family 3: c!=0
start = perf_counter()
LGC3 = AlgorithmLCG(a=2**7-1, x=3333, c=3941, m=2**13)
end = perf_counter()-start
print(f"Performance LGC3: t={end} t/n={end/(2**13)}")


print("\nMultiplicador constante\n")
print(f"Test Chicuadrado: {ChiSquareTest(CM,IC,DoF)}")
print(f"Kolmogorov: {KolmogorovTest(CM,ALPHA)}")
s, p = kstest(CM, uniform.cdf)
r = p > s
print(f"Scipy KS: {r}")
print(f"Test de rachas: {RunsTest(CM,ALPHA)}")
print(f"Autocorrelacion: {AutocorrelationTest(CM,ALPHA)}")
SaveHist(CM, 'RNG de multiplicador constante', {
         'Semilla': 573592, 'Multiplicador': 697613, 'N': 10000})

print("\nCuadrados medios\n")
print(f"Test Chicuadrado: {ChiSquareTest(MS,IC,DoF)}")
print(f"Kolmogorov: {KolmogorovTest(MS,ALPHA)}")
s, p = kstest(MS, uniform.cdf)
r = p > s
print(f"Scipy KS:{r}")
print(f"Test de rachas: {RunsTest(MS,ALPHA)}")
print(f"Autocorrelacion: {AutocorrelationTest(MS,ALPHA)}")
SaveHist(MS, 'RNG de cuadrados medios', {'Semilla': 624867, 'N': 10000})

print("\nProductos medios\n")
print(f"Test Chicuadrado: {ChiSquareTest(MP,IC,DoF)}")
print(f"Kolmogorov: {KolmogorovTest(MP,ALPHA)}")
s, p = kstest(MP, uniform.cdf)
r = p > s
print(f"Scipy KS:{r}")
print(f"Test de rachas: {RunsTest(MP,ALPHA)}")
print(f"Autocorrelacion: {AutocorrelationTest(MP,ALPHA)}")
SaveHist(MP, 'RNG de productos medios', {
         'Semilla 1': 358129, 'Semilla 2': 679452, 'N': 10000})

print("\nLGC Family 1\n")
print(f"Test Chicuadrado: {ChiSquareTest(LGC1,IC,DoF)}")
print(f"Kolmogorov: {KolmogorovTest(LGC1,ALPHA)}")
s, p = kstest(LGC1, uniform.cdf)
r = p > s
print(f"Scipy KS:{r}")
print(f"Test de rachas: {RunsTest(LGC1,ALPHA)}")
print(f"Autocorrelacion: {AutocorrelationTest(LGC1,ALPHA)}")
SaveHist(LGC1, 'GLC Familia 1', {'a': 7345, 'x': 4698, 'c': 0, 'm': mersenne})

print("\nLGC Family 2\n")
print(f"Test Chicuadrado: {ChiSquareTest(LGC2,IC,DoF)}")
print(f"Kolmogorov: {KolmogorovTest(LGC2,ALPHA)}")
s, p = kstest(LGC2, uniform.cdf)
r = p > s
print(f"Scipy KS: {r}")
print(f"Test de rachas: {RunsTest(LGC2,ALPHA)}")
print(f"Autocorrelacion: {AutocorrelationTest(LGC2,ALPHA)}")
SaveHist(LGC2, 'GLC Familia 2', {'a': 3333, 'x': 8011, 'c': 0, 'm': 2**13})

print("\nLGC Family 3\n")
print(f"Test Chicuadrado: {ChiSquareTest(LGC3,IC,DoF)}")
print(f"Kolmogorov: {KolmogorovTest(LGC3,ALPHA)}")
s, p = kstest(LGC3, uniform.cdf)
r = p > s
print(f"Scipy KS: {r}")
print(f"Test de rachas: {RunsTest(LGC3,ALPHA)}")
print(f"Autocorrelacion: {AutocorrelationTest(LGC3,ALPHA)}")
SaveHist(LGC3, 'GLC Familia 3', {'a': 2**7 -
         1, 'x': 3333, 'c': 3941, 'm': 2**13})

print("\nScharge\n")
print(f"Test Chicuadrado: {ChiSquareTest(SCH,IC,DoF)}")
print(f"Kolmogorov: {KolmogorovTest(SCH,ALPHA)}")
s, p = kstest(SCH, uniform.cdf)
r = p > s
print(f"Scipy KS: {r}")
print(f"Test de rachas: {RunsTest(SCH,ALPHA)}")
print(f"Autocorrelacion: {AutocorrelationTest(SCH,ALPHA)}")

print("\nRandom-PY\n")
print(f"Test Chicuadrado: {ChiSquareTest(RNGPY,IC,DoF)}")
print(f"Kolmogorov: {KolmogorovTest(RNGPY,ALPHA)}")
s, p = kstest(RNGPY, uniform.cdf)
r = p > s
print(f"Scipy KS: {r}")
print(f"Test de rachas: {RunsTest(RNGPY,ALPHA)}")
print(f"Autocorrelacion: {AutocorrelationTest(RNGPY,ALPHA)}")
SaveHist(RNGPY, 'RNG de Python(modulo random)', {'Semilla': 53, })
