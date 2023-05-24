from generadores import AlgorithmConstMultiplier, AlgorithmMiddleSquare, AlgorithmMiddleProduct, AlgorithmLGC, SchrageLGC
from test import test_autocorrelacion, test_rachas, KolmogorovTest, KolmogorovTest2
from scipy.stats import uniform
import random

RNGPY = [random.random() for i in range(10000)]

# Non LGC Random Number Generators
CM = AlgorithmConstMultiplier(573592, 697613, 10000)
MS = AlgorithmMiddleSquare(624867, 10000)
MP = AlgorithmMiddleProduct(358129, 679452, 10000)

# LGC Random Number Generators

# Family 1: c=0, m is prime

mersenne = (2**13)-1  # =8191
LGC1 = AlgorithmLGC(a=7345, x=4698, c=0, m=mersenne)
SCH = SchrageLGC(a=7345, x=4698, m=mersenne)

# Family 2: c=0, m is 2**X
LGC2 = AlgorithmLGC(a=6348, x=3481, c=0, m=2**13)

# Family 3: c!=0
LGC3 = AlgorithmLGC(a=3942, x=2653, c=346, m=2**13)


print("\nMultiplicador constante\n")
print(f"Autocorrelacion: {test_autocorrelacion(CM,0.05)}")
print(f"Test de rachas: {test_rachas(CM,0.05)}")
print(f"Kolmogorov: {KolmogorovTest(CM,0.05)}")
print(f"Kolmogorov(2): {KolmogorovTest2(CM,0.05,uniform)}")

print("\nCuadrados medios\n")
print(f"Autocorrelacion: {test_autocorrelacion(MS,0.05)}")
print(f"Test de rachas: {test_rachas(MS,0.05)}")
print(f"Kolmogorov: {KolmogorovTest(MS,0.05)}")
print(f"Kolmogorov(2): {KolmogorovTest2(MS,0.05,uniform)}")

print("\nProductos medios\n")
print(f"Autocorrelacion: {test_autocorrelacion(MP,0.05)}")
print(f"Test de rachas: {test_rachas(MP,0.05)}")
print(f"Kolmogorov: {KolmogorovTest(MP,0.05)}")
print(f"Kolmogorov(2): {KolmogorovTest2(MP,0.05,uniform)}")

print("\nLGC Family 1\n")
print(f"Autocorrelacion: {test_autocorrelacion(LGC1,0.05)}")
print(f"Test de rachas: {test_rachas(LGC1,0.05)}")
print(f"Kolmogorov: {KolmogorovTest(LGC1,0.05)}")
print(f"Kolmogorov(2): {KolmogorovTest2(LGC1,0.05,uniform)}")

print("\nLGC Family 2\n")
print(f"Autocorrelacion: {test_autocorrelacion(LGC2,0.05)}")
print(f"Test de rachas: {test_rachas(LGC2,0.05)}")
print(f"Kolmogorov: {KolmogorovTest(LGC2,0.05)}")
print(f"Kolmogorov(2): {KolmogorovTest2(LGC2,0.05,uniform)}")

print("\nLGC Family 3\n")
print(f"Autocorrelacion: {test_autocorrelacion(LGC3,0.05)}")
print(f"Test de rachas: {test_rachas(LGC3,0.05)}")
print(f"Kolmogorov: {KolmogorovTest(LGC3,0.05)}")
print(f"Kolmogorov(2): {KolmogorovTest2(LGC3,0.05,uniform)}")

print("\nScharge\n")
print(f"Autocorrelacion: {test_autocorrelacion(SCH,0.05)}")
print(f"Test de rachas: {test_rachas(SCH,0.05)}")
print(f"Kolmogorov: {KolmogorovTest(SCH,0.05)}")
print(f"Kolmogorov(2): {KolmogorovTest2(SCH,0.05,uniform)}")

print("\nRandom-PY\n")
print(f"Autocorrelacion: {test_autocorrelacion(RNGPY,0.05)}")
print(f"Test de rachas: {test_rachas(RNGPY,0.05)}")
print(f"Kolmogorov: {KolmogorovTest(RNGPY,0.05)}")
print(f"Kolmogorov(2): {KolmogorovTest2(RNGPY,0.05,uniform)}")
