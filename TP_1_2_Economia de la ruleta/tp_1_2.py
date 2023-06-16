from clases import Jugador, randint, JugadorMG, JugadorParoli, JugadorColumnas, JugadorDalembert, negros, rojos, JugadorDalembert2

from matplotlib import pyplot as plt
plt.style.use('ggplot')


def graficoDineroUnicaTirada(resultados: list, capAcotado: float, metodo: str) -> None:
    plt.title(
        f"Flujo de dinero de una corrida en 'n' tiradas \n - {metodo}")
    plt.axhline(capAcotado, color='k', ls="solid")
    plt.plot(resultados, linewidth=1.2)
    plt.xlabel("Número de tiradas 'n'")
    plt.ylabel("Capital en 'n' tiradas")
    # Me ajustan los x e y
    ax = plt.gca()
    ax.relim()
    ax.autoscale_view()
    # Linea invisible para agregar legend
    plt.axhline(50, color='w', ls="solid", visible=False)
    dineroIni = 'Capital inicial: ' + str(capAcotado)
    dineroFin = (f'Capital Final: {resultados[-1]}')
    plt.legend((dineroIni, dineroFin), loc="best")
    plt.xticks()
    plt.yticks()
    plt.ioff()
    plt.savefig(f"Flujo-{metodo}.png")
    plt.clf()


def graficoDineroTiradasMultiples(resultados: list, capAcotado: float, corridas: int, metodo: str) -> None:
    for i in range(corridas):
        plt.title(
            f"Flujo de dinero de {corridas} corridas respecto a 'n' tiradas - \n {metodo}")
        plt.axhline(capAcotado, color='k', ls="solid")
        plt.axhline(capAcotado * 1.5, color='c', ls="-", linewidth=0.8)
        plt.axhline(capAcotado * 0.5, color='r', ls="-")
        plt.plot(resultados[i], linewidth=1.3)
        plt.xlabel("Número de tiradas 'n'")
        plt.ylabel("Capital en 'n' tiradas")
        # Me ajustan los x e y
        ax = plt.gca()
        ax.relim()
        ax.autoscale_view()
        # Linea invisible para agregar legend
        plt.axhline(capAcotado, color='w', ls="solid", visible=False)
        dineroIni = 'Capital inicial: ' + str(capAcotado)
        cincuentamas = ('Ganancia del 50%')
        cincuentamenos = ('Pérdida del 50%:')
        plt.legend((dineroIni, cincuentamas, cincuentamenos),
                   loc="best")
        plt.xticks()
        plt.yticks()
        # plt.legend((dineroIni,), loc="best")
        plt.ioff()
        plt.savefig(f"FlujoMultiple-{metodo}.png")
    plt.clf()


def graficaFrecFavorable(frecuencias: list, title1: str) -> None:
    plt.title(
        f"Frecuencia relativa de obtener \n  una apuesta favorable segun 'n'\n  {title1}")
    plt.bar(range(0, len(frecuencias)), frecuencias,
            width=1, edgecolor="white", linewidth=1, align='edge')
    plt.ylabel('Frecuencia relativa')
    plt.ylim(0, 0.3)
    plt.xlim(xmin=0, xmax=18)
    plt.xlabel('Cantidad de tiradas "n"')
    plt.xticks()
    plt.yticks()
    plt.savefig(f"FrecFav-{title1}.png")
    plt.clf()


def tirada() -> int:
    return randint(0, 36)


valorApuesta = 5  # Valor de la apuesta
capAcotado = 100  # Capital acotado

t = 255  # número de tiradas
c = 10  # número de corridas


def ejecutar(clase: Jugador, metodo: str, capital_acotado: bool = False):
    """Genera todas las graficas
    Se puede indicar si el capital es acotado o no, por defecto no es acotado
    lo que significa que el jugador puede asumir perdidas"""
    apuesta_minima = 1

    j1 = clase(capital=capAcotado, apuesta_ini=valorApuesta,
               cap_acotado=capital_acotado)
    listado_jugadores = []

    for i in range(c):
        listado_jugadores.append(
            clase(capital=capAcotado, apuesta_ini=valorApuesta, cap_acotado=capital_acotado))
    vic = [0 for i in range(t)]
    resultadosj1 = [j1.capital, ]
    ultima_vic = 0
    for i in range(t):
        n = tirada()
        j1.jugar(n)
        resultadosj1.append(j1.capital)
    resultados = []

    for jugador in listado_jugadores:
        lista = []
        ultima_victoria = 0
        for i in range(t):
            n = tirada()
            victorias_antes = jugador.victorias
            jugador.jugar(n)
            victoria_n = jugador.victorias - victorias_antes
            if victoria_n >= 1:
                vic[i-ultima_victoria] += 1
                ultima_victoria = i+1
            lista.append(jugador.capital)
        resultados.append(lista)
    for i in range(t):
        vic[i] /= (t*c)

    graficaFrecFavorable(vic, metodo)
    graficoDineroUnicaTirada(resultadosj1, capAcotado, metodo)
    graficoDineroTiradasMultiples(resultados, capAcotado, c, metodo)


ejecutar(clase=JugadorMG, metodo="Martingala - Sin restricciones de capital",
         capital_acotado=False)
ejecutar(clase=JugadorMG, metodo="Martingala - Con capital acotado",
         capital_acotado=True)

""" ejecutar(clase=JugadorParoli,
         metodo="Paroli - Sin restricciones de capital", capital_acotado=False)
ejecutar(clase=JugadorParoli,
         metodo="Paroli - Con capital acotado", capital_acotado=True)
 """
# ejecutar(clase=JugadorColumnas,
#          metodo="Columnas - Sin restricciones de capital", capital_acotado=False)
# ejecutar(clase=JugadorColumnas,
#          metodo="Columnas - Con capital acotado", capital_acotado=True)

# ejecutar(clase=JugadorDalembert,
#          metodo="Dalembert - Sin restricciones de capital", capital_acotado=False)
# ejecutar(clase=JugadorDalembert,
#          metodo="Dalembert - Con capital acotado", capital_acotado=True)

# ejecutar(clase=JugadorDalembert2,
#          metodo="Dalembert(columnas) - Sin restricciones de capital", capital_acotado=False)
# ejecutar(clase=JugadorDalembert2,
#          metodo="Dalembert(columnas) - Con capital acotado", capital_acotado=True)
