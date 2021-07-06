# Juego "Hundir la flota" en Python
![imagen](./hundir-la-flota-juego-de-mesa.jpg)
## Descripción del proyecto:  
Para elaborar este proyecto hemos realizados dos archivos: uno para las funciones y otro principal.  
##### En `funciones` hay cuatro funciones:
* Dos para poner una coordenada random (una para fila y otra para columna).  
* Una para la dirección (horizontal o vertical).
* Una para crear el tablero y colocar los barcos.
##### En `main`:
* Definimos la cantidad y tamaños de los barcos con una lista de tuplas.
* Generamos cuatro tableros: dos para el jugador (una con los barcos y otra con los disparos) y lo mismo para la pc.
* El flujo de juego se desarrolla dentro de un bucle `while` que se ejecuta mientras uno de los dos tenga vidas.  
* Si el jugador introduce una coordenada inválida, puede introducir una nueva.
* Si el disparo da en un barco, se actualiza el mapa y ese jugador vuelve a disparar.
## Autores:
* Gustavo Hernando  
* Eva Rodrigo  
## Librerías utilizadas  
* [Numpy](https://numpy.org/doc/)  
* [Time](https://docs.python.org/3/library/time.html)


## Recursos empleados
* [PyCharm](https://www.jetbrains.com/pycharm/)
* [Jupyter-lab](https://jupyter.org/)