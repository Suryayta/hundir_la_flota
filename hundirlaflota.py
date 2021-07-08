import funciones as ft
import numpy as np
import time

#Inicialmente la idea era trabajar con clases, pero al final lo dejamos, el tablero esta parametrizado, a para poder modificar las dimensiones del tablero y los barcos


#1. Definición de variables
tablero = np.full(fill_value = " ", shape = (10, 10))
#barcos = [(1,4), (2,3), (3,2), (4,1)]  #Tupla con eslora y número de barcos
barcos = [(1,1)]

#2. Creacion de tableros con funcion tablero
tablero_jugador = ft.genera_tablero(tablero.shape,barcos)
tablero_pc = ft.genera_tablero(tablero.shape,barcos)

disparos_jugador = np.full(fill_value = " ", shape = (10, 10))
disparos_pc = np.full(fill_value = " ", shape = (10, 10))


turno_pc = True        #Variable para turno de juego
turno_jugador = True   #Variable para turno de juego
lista_disparos_pc = [] #Lista de disparos, para hacer que la maquina dispare en lugares diferentes cada turno


#3.juego
    #3.1 Declaro variables para iniciar juego
print('Inicia juego','\n')
aciertos_jugador = len(disparos_jugador[disparos_jugador == "X"]) #Contador de  disparos aciertos jugador
aciertos_pc = len(disparos_pc[disparos_pc == "X"])                #Contador de  disparos aciertos PC
vidas = len(tablero_jugador[tablero_jugador=="O"])                #Contador de vidas [Barcos] * [slora]
vidas_jugador = vidas
vidas_pc = vidas

while vidas_jugador != 0 and vidas_pc !=0:

    #3.2 Inicia turno de jugador
    while turno_jugador == True:
        print("Tu turno:","\n", "Mira donde has disparado","\n",disparos_jugador,"\n","Recuerda ""x"" es fuego y ""~"" es agua")

        #3.2.1 Colocamos protección por si se indica numero superior al largo del tablero
        try:
            disparo_jug = [int(input("Introduzca fila de disparo: ")),int(input("introduzca columna de disparo: "))]

            #3.2.2 Evaluo la posicion del  disparo del jugador en el tablero de la PC y actualizo variables de juego
            if tablero_pc[disparo_jug[0],disparo_jug[1]] == "O":
                disparos_jugador[disparo_jug[0], disparo_jug[1]] = "X"
                aciertos_jugador = len(disparos_jugador[disparos_jugador == "X"])
                vidas_pc = vidas - aciertos_jugador
                print("¡Fueeeeego!")
                time.sleep(2)

                #Evaluo si le quedan vidas al PC
                if vidas_pc == 0:
                    turno_jugador = False #Finalizo turno de jugador porque ganó.
                    turno_pc = False      #Elimino turno de PC ya que perdió.
                    break
            else:
                print("¡Aguaaaa!")
                time.sleep(2)
                disparos_jugador[disparo_jug[0], disparo_jug[1]] = "~"
                turno_jugador = False

        except IndexError:
            print("Disparo fuera del tablero, apunta mejor la próxima vez.")

    turno_jugador = True

    # 3.2 Inicia turno de PC
    while turno_pc == True:
        print("\n\n","Ahora es mi turno, prepárate: ")

        aciertos_pc = len(disparos_pc[disparos_pc == "X"])
        vidas_jugador = vidas - aciertos_pc
        disparo_pc_x = ft.random_row()
        disparo_pc_y = ft.random_col()
        disparo_pc = [disparo_pc_x,disparo_pc_y]

        # 3.2.1 Evaluo que el disparo no sea repetido
        if disparo_pc in lista_disparos_pc:
            pass

        # 3.2.3 Evaluo la posicion del  disparo del PC en el tablero del jugador y actualizo variables de juego
        elif tablero_jugador[disparo_pc[0],disparo_pc[1]] == "O":
            disparos_pc[disparo_pc[0],disparo_pc[1]] = "X"

            # acomoda la visual para el jugador de forma que sepa cuantos barcos tiene vivos
            tablero_jugador[disparo_pc[0], disparo_pc[1]] = "X"

            print(disparo_pc, ".... fuego!!","\n","Así tienes tus barcos","\n",tablero_jugador)
            time.sleep(4)

            # Actualiza vidas
            aciertos_pc = len(disparos_pc[disparos_pc == "X"])
            vidas_jugador = vidas - aciertos_pc

            # Evaluamos si le quedan vidas al Jugador
            if vidas_jugador == 0:
                turno_pc = False
                break

        else:
            tablero_jugador[disparo_pc[0],disparo_pc[1]] = "~"
            turno_pc = False
            print(disparo_pc," Agua, ¡he fallado!", "\n","Así tienes tus barcos","\n", tablero_jugador)
            time.sleep(4)
        lista_disparos_pc.append(disparo_pc) # guardo el disparo de la pc en la lista

    turno_pc = True

    # 3.3 Fin de turno
    print("\n\n","Fin de ronda tienes %i vidas y la pc tiene %i vidas" % (vidas_jugador,vidas_pc),"\n\n")

    #3.1 Fin de Juego indicamos Ganador
if aciertos_jugador == vidas :
    print("Ganaste!")
else:
    print("Perdiste :/")