import random
import numpy as np
import matplotlib.pyplot as plt

ListaTirada = []
Media = []
Frecuencia = []
Desviacion = []
DesviacionDeNum= []
Varianza = []
VarianzaDeNum = []

def TirarRuleta():
    global Tiradas
    Tiradas = 37
    global NumAEvaluar
    NumAEvaluar = None
    CantNumeros = 0
    print("Bienvenido a la ruleta de 37 números")
    while not ((isinstance(Tiradas,int)) and (isinstance(NumAEvaluar,int) and NumAEvaluar>=0 and NumAEvaluar<=36)):
        try:
            Tiradas=1500
            NumAEvaluar=np.random.randint(0,37)
            if not(NumAEvaluar>=0 and NumAEvaluar<=36):
                raise Exception()
        except ValueError:
            print("No ingresó un numero entero, intente nuevamente")
        except:
            print("El numero a evaluar debe estar entre 0 y 36")

    for _ in range(Tiradas):
        ListaTirada.append(random.randint(0,36))
        Media.append(np.mean(ListaTirada))
        Desviacion.append(np.std(ListaTirada))
        Varianza.append(np.var(ListaTirada))
        DesviacionDeNum.append(abs(NumAEvaluar - np.mean(ListaTirada)))
        VarianzaDeNum.append(abs(NumAEvaluar - np.mean(ListaTirada)) ** 2)
      

        if ListaTirada[-1] == NumAEvaluar:
            CantNumeros += 1
        Frecuencia.append(CantNumeros/len(ListaTirada))    

def MostarTiradas():
    plt.plot(ListaTirada)
    plt.title("Tiradas Totales")
    plt.xlabel("n (número de tiradas)")
    plt.ylabel("Resultado")
    plt.savefig("tiradas.png")
    plt.show()
   

def MostrarMedia():
    plt.plot(Media, label = "Valor Obtenido")
    plt.title("Valor promedio de las tiradas")
    plt.xlabel("n (número de tiradas)")
    plt.ylabel("vp (valor promedio de las tiradas)")
    MediaEsperada = [18] * Tiradas
    plt.plot(MediaEsperada, label = "Valor Esperado")
    plt.legend(loc = "upper left") 
    plt.savefig("media.png")
    plt.show()

def MostrarFrecRel():
    plt.plot(Frecuencia, label = "Valor Obtenido")
    plt.title(f"Frecuencia relativa del número {NumAEvaluar}")
    plt.xlabel("n (número de tiradas)")
    plt.ylabel("fr (frecuencia relativa)")
    FrecEsperada = []
    for _ in range(len(Frecuencia)):
        FrecEsperada.append(1/37) #Cada nro tiene la misma probabilidad de salir 
    plt.plot(FrecEsperada, label = "Valor Esperado")
    plt.legend(loc = "upper left") 
    plt.savefig("frecRelativa.png")
    plt.show()

def MostrarDesvio():
    plt.plot(Desviacion, label = "Valor Obtenido")
    plt.title("Valor del desvío")
    plt.xlabel("n (número de tiradas)")
    plt.ylabel("vd (valor del desvío)")
    DesvEsperado = []
    for _ in range(len(Desviacion)):
        DesvEsperado.append(np.arange(0, 37).std()) #Desviacion estandar
    plt.plot(DesvEsperado, label = "Valor Esperado")
    plt.legend(loc = "upper left") 
    plt.savefig("desvioEst.png")
    plt.show()    

def MostrarDesvioNum():
    plt.plot(DesviacionDeNum, label = "Valor Obtenido")
    plt.title(f"Valor del Desvio del número {NumAEvaluar}")
    plt.xlabel("n (número de tiradas)")
    plt.ylabel("vd (valor del desvío)")
    DesvEsperado = [abs(NumAEvaluar - 18)] * Tiradas
    plt.plot(DesvEsperado, label = "Valor Esperado")
    plt.legend(loc = "upper left") 
    plt.savefig("desvioNum.png")
    plt.show()

def MostrarVarianza():
    plt.plot(Varianza, label = "Valor Obtenido")
    plt.title("Valor de la varianza")
    plt.xlabel("n (número de tiradas)")
    plt.ylabel("vv (valor de la varianza)")
    VarianzaEsperada = []
    for _ in range(len(Varianza)):
        VarianzaEsperada.append((np.arange(0, 37).std())** 2)
    plt.plot(VarianzaEsperada, label = "Valor Esperado")
    plt.legend(loc = "upper left") 
    plt.savefig("varianza.png")
    plt.show() 

def MostrarVarianzaNum():
    plt.plot(VarianzaDeNum, label = "Valor Obtenido")
    plt.title(f"Valor de la Varianza del número {NumAEvaluar}")
    plt.xlabel("n (número de tiradas)")
    plt.ylabel("vv (valor de la varianza)")
    VarianzaEsperada = [(abs(NumAEvaluar - 18))** 2] * Tiradas
    plt.plot(VarianzaEsperada, label = "Valor Esperado")
    plt.legend(loc = "upper left") 
    plt.savefig("desvioNum.png")
    plt.show()




TirarRuleta()
MostarTiradas()
MostrarMedia()
MostrarFrecRel()
MostrarDesvio()
MostrarDesvioNum()
MostrarVarianza()
MostrarVarianzaNum()