import numpy as np
import random
import pandas as pd
# Random
def random_row():
    return random.randint(0, 9)
def random_col():
    return random.randint(0, 9)
def direction():
    return random.choice([0, 1])
#generacion de tablero
def genera_tablero(x,a):
    dimension_x = x[0]
    dimension_y = x[1]
    barcos = a
    # Crea tablero
    tablero = np.full(fill_value=" ", shape=x)
    for tupla in barcos:
        eslora = tupla[0]
        n_barcos = tupla[1]
        i = 0
        while i != n_barcos:
            #a = tablero
            barco_row = random_row()
            barco_col = random_col()
            axis = direction()
            if axis == 0:
                barco_col_fin = barco_col + eslora
                barco_row_fin = barco_row + 1
                if barco_col_fin <= x[0] and barco_row_fin <= x[1]:
                    pos_total = tablero[barco_row:barco_row_fin, barco_col:barco_col_fin]
                    if np.all(pos_total == " "):
                        tablero[barco_row:barco_row_fin, barco_col:barco_col_fin] = "O"
                        i += 1
            else:
                barco_row_fin = barco_row + eslora
                barco_col_fin = barco_col + 1
                if barco_col_fin <= 10 and barco_row_fin <= 10:
                    pos_total = tablero[barco_row:barco_row_fin, barco_col:barco_col_fin]
                    if np.all(pos_total == " "):
                        tablero[barco_row:barco_row_fin, barco_col:barco_col_fin] = "O"
                        i += 1
    return tablero