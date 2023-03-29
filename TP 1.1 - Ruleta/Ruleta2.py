import random
import statistics
from matplotlib import pyplot
import numpy as np

desv_esp=10.67707825

#funciones lineales de los valores esperados

def promEsperado(x):
    return 18

def desvEsperado(x):
    return desv_esp

def varianzaEsperado(x):
    return desv_esp**2

def frEsperado(x):
    return 1/37


print("Ingrese cantidad de veces que desea tirar la ruleta")
n=int(input())

for i in range(0,8):
  co=0
  y=[]
  prom=[]
  desv=[]
  var=[]
  fr=[]
  v=1 #acá se establece el valor para el cual queremos que se calcule la frecuencia relativa


  for a in range(0,n):
    y.insert(a, random.randint(0, 36))
    prom.insert(a, statistics.mean(y))
    desv.insert(a, statistics.pstdev(y))
    var.insert(a, statistics.pvariance(y))
    if(y[a]==v):
      co=co+1
    fr.insert(a,co/(a+1))

  x=np.arange(0,n,1)

  #frecuencia relativa
  pyplot.figure('Frecuencia Relativa')
  pyplot.plot(x,fr)
  pyplot.grid()
  pyplot.xlim(0, n)
  pyplot.xlabel('n (número de tiradas)')
  pyplot.ylabel('fr (frecuencia relativa)')
  pyplot.title('frn (frecuencia relativa del valor x=1 con respecto a n)')

  #promedio
  pyplot.figure('Promedio')
  pyplot.plot(x,prom)
  pyplot.grid()
  pyplot.xlim(0, n)
  pyplot.ylim(0, 36)
  pyplot.xlabel('n (número de tiradas)')
  pyplot.ylabel('vp (valor promedio de las tiradas)')
  pyplot.title('vpn (valor promedio de las tiradas con respecto a n)')

  #desvío
  pyplot.figure('Desvio')
  pyplot.plot(x,desv)
  pyplot.grid()
  pyplot.xlim(0, n)
  pyplot.ylim(0, 36)
  pyplot.xlabel('n (número de tiradas)')
  pyplot.ylabel('vd (valor del desvío)')
  pyplot.title('vdn (valor del desvío de las tiradas con respecto a n)')


  #varianza
  pyplot.figure('Varianza')
  pyplot.plot(x,var)
  pyplot.grid()
  pyplot.xlim(0, n)
  pyplot.ylim(0, 200)
  pyplot.xlabel('n (número de tiradas)')
  pyplot.ylabel('vv (valor de la varianza')
  pyplot.title('vvn (valor de la varianza de las tiradas con respecto a n)')


pyplot.figure('Frecuencia Relativa')
pyplot.plot(x, [frEsperado(i) for i in x], color='b', label='frecuencia relativa esperada')
pyplot.legend(loc='upper left')
pyplot.figure('Promedio')
pyplot.plot(x, [promEsperado(i) for i in x], color='b', label='promedio esperado')
pyplot.legend(loc='upper left')
pyplot.figure('Desvio')
pyplot.plot(x, [desvEsperado(i) for i in x], color='b', label='desvío esperado')
pyplot.legend(loc='upper left')
pyplot.figure('Varianza')
pyplot.plot(x, [varianzaEsperado(i) for i in x], color='b', label='varianza esperada')
pyplot.legend(loc='upper left')
pyplot.show()