import matplotlib.pyplot as plt
import numpy as np
RUTA = 'TP 1.1 - Ruleta'
plt.style.use('Solarize_Light2')

# TP 1.1 Simulación de Una Ruleta
# Datos


def frecuenciaR(nro, valores):
    frecuenciaA = 0
    for n in valores:
        if n == nro:
            frecuenciaA += 1
    freqRel = frecuenciaA/len(valores)
    return freqRel


frecuencia = 1/37
esperanza = np.arange(0, 37).mean()  # Media aritmética
desvio = np.arange(0, 37).std()  # Desviación Estándar
varianza = np.arange(0, 37).var()  # Varianza

t = 560  # número de tiradas
c = 37  # número de corridas
nroEvaluar = 7  # np.random.randint(0,37)

x_e = (555/37)**2


frecuencias = [[0 for x in range(t)] for y in range(c)]
medias = [[0 for x in range(t)] for y in range(c)]
desvios = [[0 for x in range(t)] for y in range(c)]
varianzas = [[0 for x in range(t)] for y in range(c)]


for i in range(0, c):
    numeros = np.random.randint(0, 37, t)
    print(numeros)
    for n in range(0, t):
        lista = numeros[:n+1]
        frecuencias[i][n] = frecuenciaR(nroEvaluar, lista)
        medias[i][n] = lista.mean()
        desvios[i][n] = lista.std()
        varianzas[i][n] = lista.var()

# Graficos

# Frecuencia Relativa - Grafico
fig, axs = plt.subplots()
axs.set_title('Frecuencia Relativa (fr)')
axs.set(xlabel='Tiradas', ylabel='Frecuencia Relativa (fr)')
axs.set_ylim(bottom=0, top=max(np.amax(frecuencias), frecuencia)+0.05)
for i in range(0, c):
    axs.plot(range(1, t+1), frecuencias[i])
axs.axhline(y=frecuencia, color='red', linestyle='-',
            label='fre: '+str(round(frecuencia, 3)))
axs.axvline(x=x_e, color='b', linestyle='dashed')
fig.savefig(f'{RUTA}/FRelativa-C{c}-T{t}.png')
plt.clf()

# Valor promedio - Grafico
fig, axs = plt.subplots()
axs.set_title('Valor Promedio (vp)')
axs.set(xlabel='Tiradas', ylabel='Valor Promedio (vp)')
axs.set_ylim(bottom=0, top=max(np.amax(medias), esperanza)+1)
for i in range(0, c):
    # , label='corrida '+str(i+1)+'°')
    axs.plot(range(1, t+1), medias[i])
axs.axhline(y=esperanza, color='red', linestyle='-',
            label='vpe: '+str(round(esperanza, 3)))
axs.axvline(x=x_e, color='b', linestyle='dashed')
fig.savefig(f'{RUTA}/VPromedio-C{c}-T{t}.png')
plt.clf()


# Valor del desvio - Grafico
fig, axs = plt.subplots()
axs.set_title(f'Valor del Desvío (vd)')
axs.set(xlabel='Tiradas', ylabel='Valor del Desvío (vd)')
axs.set_ylim(bottom=0, top=max(np.amax(desvios), desvio)+1)
for i in range(0, c):
    # , label='corrida '+str(i+1)+'°')
    axs.plot(range(1, t+1), desvios[i])
axs.axhline(y=desvio, color='red', linestyle='-',
            label='vde: '+str(round(desvio, 3)))
axs.axvline(x=x_e, color='b', linestyle='dashed')
fig.savefig(f'{RUTA}/Desvio-C{c}-T{t}.png')
plt.clf()

# Varianza
fig, axs = plt.subplots()
axs.set_title(f'Valor de la Varianza (vve)')
axs.set(xlabel='Tiradas', ylabel='Valor de la Varianza (vv)')
axs.set_ylim(bottom=0, top=max(np.amax(varianzas), varianza)+10)
for i in range(0, c):
    # , label='corrida '+str(i+1)+'°')
    axs.plot(range(1, t+1), varianzas[i])
axs.axhline(y=varianza, color='red', linestyle='-',
            label='vve: '+str(round(varianza, 3)))
axs.axvline(x=x_e, color='b', linestyle='dashed')
fig.savefig(f'{RUTA}/Varianza-C{c}-T{t}.png')
plt.clf()
