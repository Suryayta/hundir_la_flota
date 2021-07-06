import funciones as ft
import numpy as np
import time
#class hundir_flota:
#    tablero = (10,10)
#    barcos = [(1,4), (2,3), (3,2), (4,1)]
tablero = np.full(fill_value = " ", shape = (10, 10))
#Definición de variables
#Tupla con eslora y número de barcos
barcos = [(1,4), (2,3), (3,2), (4,1)]
#Creacion de tableros
#tablero_jugador = ft.genera_tablero(tablero.shape,barcos)
tablero_jugador = ft.genera_tablero(tablero.shape,barcos)
tablero_pc = ft.genera_tablero(tablero.shape,barcos)
disparos_jugador = np.full(fill_value = " ", shape = (10, 10))
disparos_pc = np.full(fill_value = " ", shape = (10, 10))
turno_pc = True
turno_jugador = True
lista_disparos_pc = []
# Inicio de juego
print('Inicia juego','\n')
aciertos_jugador = len(disparos_jugador[disparos_jugador == "X"])
aciertos_pc = len(disparos_pc[disparos_pc == "X"])
vidas = len(tablero_jugador[tablero_jugador=="O"])
vidas_jugador = vidas
vidas_pc = vidas
#agregrar un apend con el numero de columnas y filas
while vidas_jugador != 0 and vidas_pc !=0:
    while turno_jugador == True:
        print("Hora de disparar:","\n\n\n", "Mira dónde has disparado", "\n", disparos_jugador)
        try:
            disparo_jug = [int(input("Introduzca fila de disparo: ")),int(input("introduzca columna de disparo: "))]
            if tablero_pc[disparo_jug[0],disparo_jug[1]] == "O":
                disparos_jugador[disparo_jug[0], disparo_jug[1]] = "X"
                aciertos_jugador = len(disparos_jugador[disparos_jugador == "X"])
                vidas_pc = vidas - aciertos_jugador
                if vidas_pc == 0:
                    turno_jugador = False
                    turno_pc = False
                    break
        except IndexError:
            print("Disparo fuera del tablero, apunta mejor la próxima vez.")
            print("¡Fueeeeego!")

        else:
            print("¡Aguaaaa!")
            disparos_jugador[disparo_jug[0], disparo_jug[1]] = "~"
            turno_jugador = False
    turno_jugador = True
    while turno_pc == True:
        print("Ahora es mi turno, prepárate: ""\n\n")
        time.sleep(1)
        aciertos_pc = len(disparos_pc[disparos_pc == "X"])
        vidas_jugador = vidas - aciertos_pc
        disparo_pc_x = ft.random_row()
        disparo_pc_y = ft.random_col()
        disparo_pc=[disparo_pc_x,disparo_pc_y]
        if disparo_pc in lista_disparos_pc:
            pass
        elif tablero_jugador[disparo_pc[0],disparo_pc[1]] == "O":
            disparos_pc[disparo_pc[0],disparo_pc[1]] = "X"
            #Lleva el conteo de los aciertos
            tablero_jugador[disparo_pc[0], disparo_pc[1]] ="X"
            # acomoda la visual para el jugador
            aciertos_pc = len(disparos_pc[disparos_pc == "X"])
            vidas_jugador = vidas - aciertos_pc
            print(disparo_pc, ".... fuego!!", "\n\n")
            print("Aquí te ha disparado la pc:",  "\n", disparos_pc)
            if vidas_jugador == 0:
                turno_pc = False
                break
        else:
            tablero_jugador[disparo_pc[0],disparo_pc[1]] = "~"
            turno_pc = False
            print("Agua, ¡he fallado!", "\n\n", "Así está mi tablero:",  "\n", tablero_jugador)
        lista_disparos_pc.append(disparo_pc)
    turno_pc = True

    aciertos_pc = len(disparos_pc[disparos_pc == "X"])

    vidas_jugador = vidas-aciertos_pc
    print("Tienes %i vidas y la pc tiene %i vidas" % (vidas_jugador,vidas_pc),"\n\n","Siguiente ronda","\n\n")
if aciertos_jugador == vidas :
    print("Ganaste!")
else:
    print("Perdiste :/ ")