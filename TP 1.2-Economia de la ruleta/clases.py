from random import randint, random, shuffle
from tkinter import N

global apuesta_minima
apuesta_minima = 0

global negros
global rojos
negros = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
rojos = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]


class Jugador:
    _last_id = 0

    @classmethod
    def gen_id(cls) -> int:
        cls._last_id += 1
        return cls._last_id

    def __init__(self, capital: float = 0, apuesta_ini: float = apuesta_minima, cap_acotado: bool = False) -> None:
        self.id = self.gen_id()
        self.capital = capital
        self.apuesta_0 = apuesta_ini
        self.victorias = 0
        self.cap_acotado = cap_acotado

    def apostar(self) -> None:
        """Se selecciona una tipo de apuesta entre par/impar, rojo/negro o primeros 18/ultimos 18"""
        selector = randint(1, 3)
        selector2 = randint(1, 36)
        if selector == 1:
            """Se apuesta por par o impar"""
            self.prox_apuesta = "impar"
            if selector2 % 2 == 0:
                self.prox_apuesta = "par"

        elif selector == 2:
            """Se apuesta por [1-18] o [19-36]"""
            self.prox_apuesta = "[1-18]"
            if selector2 in range(19, 37):
                self.prox_apuesta = "[19-36]"

        else:
            """Se apuesta por negro o rojo"""
            self.prox_apuesta = "rojo"
            if selector2 in negros:
                self.prox_apuesta = "negro"

    def gana_apuesta(self, num: int) -> bool:
        result = (num % 2 == 0 and self.prox_apuesta == "par") or (num % 2 != 0 and self.prox_apuesta == "impar") or (
            num in negros and self.prox_apuesta == "negro") or (num in rojos and self.prox_apuesta == "rojo") or (
            num in range(1, 19) and self.prox_apuesta == "[1-18]") or (num in range(19, 37) and self.prox_apuesta == "[19-36]")
        if result:
            self.victorias += 1
        return result


class JugadorMG(Jugador):
    """Jugadores que siguen metodo martingala. 
    Cada apuesta seguira aleatoriamente negro/rojo o [1-18]/[19-36] o par/impar"""

    def __init__(self, capital: float = 0, apuesta_ini: float = apuesta_minima, cap_acotado: bool = False) -> None:
        """La apuesta inicial es por defecto la minima"""
        super().__init__(capital, apuesta_ini, cap_acotado)
        self.juegos_perdidos = 0
        self.apostar()  # se mantiene la apuesta hasta ganar

    def preparar_apuesta(self) -> None:
        """Se selecciona el monto a apostar"""
        apuesta = self.apuesta_0*(2**self.juegos_perdidos)
        if not (self.cap_acotado and apuesta > self.capital):
            # capital no acotado o apuesta preestablecida menor o igual a capital
            self.monto_prox_apuesta = apuesta
        elif self.capital >= apuesta_minima:
            # se abandona temporalmente el sistema cuando ya no se posee el monto indicado por martingala
            self.monto_prox_apuesta = self.capital  # y se apuesta lo que se tiene
        else:
            self.monto_prox_apuesta = 0   # se deja de apostar cuando el capital se termina

    def jugar(self, num: int) -> None:
        self.preparar_apuesta()
        if self.monto_prox_apuesta != 0:
            if self.gana_apuesta(num):
                self.capital += self.monto_prox_apuesta
                self.juegos_perdidos = 0  # se reinicia el martingala
                self.apostar()  # se cambia el elemento a apostar
            else:
                self.capital -= self.monto_prox_apuesta
                self.juegos_perdidos += 1


class JugadorParoli(Jugador):
    """Jugadores que siguen metodo Paroli
    Cada apuesta seguira aleatoriamente negro/rojo o [1-18]/[19-36] o par/impar"""

    def __init__(self, capital: float = 0, apuesta_ini: float = apuesta_minima, cap_acotado: bool = False) -> None:
        """La apuesta inicial es por defecto la minima"""
        super().__init__(capital, apuesta_ini, cap_acotado)
        self.racha_positiva = 0

    def preparar_apuesta(self) -> None:
        # se selecciona el monto a apostar
        if self.racha_positiva == 3:
            self.racha_positiva = 0
        apuesta = self.apuesta_0*(2**self.racha_positiva)
        if not (self.cap_acotado and apuesta > self.capital):
            self.monto_prox_apuesta = apuesta
        elif self.capital >= apuesta_minima:
            # se abandona temporalmente el sistema cuando ya no se posee el monto indicado por Paroli
            self.monto_prox_apuesta = self.capital  # y se apuesta lo que se tiene
        else:
            self.monto_prox_apuesta = 0   # se deja de apostar cuando el capital se termina
        # se selecciona la forma de apuesta
        self.apostar()

    def jugar(self, num: int) -> None:
        self.preparar_apuesta()
        if self.monto_prox_apuesta != 0:
            if self.gana_apuesta(num):

                self.capital += self.monto_prox_apuesta
                self.racha_positiva += 1
            else:
                self.capital -= self.monto_prox_apuesta
                self.racha_positiva = 0


class JugadorColumnas(Jugador):
    """Jugadores que apuestan a todas las columnas"""
    cols = ([1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34],
            [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35],
            [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36])

    def __init__(self, capital: float = 0, apuesta_ini: float = apuesta_minima, cap_acotado: bool = False) -> None:
        super().__init__(capital, apuesta_ini, cap_acotado)
        self.minima = apuesta_ini
        self.media = self.minima*2
        self.maxima = self.media*2

    def jugar(self, num: int) -> None:
        """Establece a que columna se apuesta el minimo, a cual el doble(medio),
        y a cual el cuadruple(maxima) y varia el capital de acuerdo a los resultados.
        Al final de cada apuesta se duplican los montos a apostar en la proxima"""
        indices = [0, 1, 2]
        shuffle(indices)
        idxmin, idxmed, idxmax = indices  # montos a apostar por col seleccionados
        if self.cap_acotado:
            if (self.maxima+self.media+self.minima) > self.capital:
                # cuando no se pueden cubrir todas las columnas no se apuesta
                return
        if num in JugadorColumnas.cols[idxmax]:
            self.capital += self.maxima*3

        else:
            self.capital -= self.maxima

        if num in JugadorColumnas.cols[idxmed]:
            self.capital += self.media*3
        else:
            self.capital -= self.media

        if num in JugadorColumnas.cols[idxmin]:
            self.capital += self.minima*3
        else:
            self.capital -= self.minima

        # finalmente se duplican los montos para la prox apuesta
        """self.minima *= 2
        self.media *= 2
        self.maxima *= 2"""


class JugadorDalembert(Jugador):
    """Jugadores que siguen metodo martingala. 
    Cada apuesta seguira aleatoriamente negro/rojo o [1-18]/[19-36] o par/impar"""

    def __init__(self, capital: float = 0, apuesta_ini: float = apuesta_minima, cap_acotado: bool = False) -> None:
        """La apuesta inicial es por defecto la minima"""
        super().__init__(capital, apuesta_ini, cap_acotado)
        self.monto_prox_apuesta = apuesta_minima
        self.apostar()

    def jugar(self, num: int) -> None:
        if (self.cap_acotado):
            if (self.monto_prox_apuesta <= self.capital):
                # se apuesta el metodo establecido por el metodo cuando hay capital
                apuesta = self.monto_prox_apuesta
            else:
                # se apuesta el capital restante cuando no se posee lo suficiente para respetar el metodo
                apuesta = self.capital
        else:
            # el capital es infinito y se puede apostar segun el metodo
            apuesta = self.monto_prox_apuesta

        if (self.gana_apuesta(num)):
            self.capital -= apuesta
            if (self.monto_prox_apuesta > apuesta_minima):
                # se reduce el monto a apostar la siguiente ronda siempre que no sea menor que la minima
                self.monto_prox_apuesta -= 1
            self.apostar()  # se cambia el elemento a apostar
        else:
            self.capital -= apuesta
            self.monto_prox_apuesta += 1
