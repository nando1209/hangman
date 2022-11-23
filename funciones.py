## imports
import os
from classes import *


## etapa de ingreso de jugadores

## limpiar pantalla
def cls():
    os.system('clear')
    
## banner de inicio
def banner_inicio():
    print("""
      ******************************************************************
      ****                                                          ****
      ****  W E L C O M E   T O   T H E   H A N G M A N   G A M E   ****
      ****                                                          ****
      ******************************************************************
      """)

## function para opción de jugadores
def opcion_inicio():
    while True:
        opcion = input("\nCuántos jugadores van a jugar?\nIngrese (1) para un jugador, (2) para dos jugadores o (a) por ayuda, y luego presione \"Enter\"\n")
        if opcion == "1":
            un_jugador()
            break
        elif opcion == "2":
            print(2)
            break
        elif opcion == "a" or opcion == "A":
            desplegar_ayuda()
            break
        else:
            cls()
            banner_inicio()
            print("Debe elegir una opción entre (1), (2) y (a).\n")
            opcion_inicio()

## desplegar ayuda
def desplegar_ayuda():
    cls()
    banner_inicio()
    print("""
        HANGMAN => v1.0
        
        REGLAS DEL JUEGO:
        =================  
        
        Idioma de los títulos de las películas:
        ---------------------------------------
        Recuerda que para evitar confunsión en los títulos de las películas por diferentes traducciones al español en cada país, 
        el juego tiene los títulos originales de las películas.
        
        
        MODOS DE JUEGO:
        ===============
        
        1 Jugador:
        ----------
        En modo de un jugador tenes 7 oportunidades de equivocarte al elegir una letra.
        (Cabeza, Cuerpo, Brazo Izquierdo, Brazo Derecho, Pierna Izquierda, Pierna Derecha y ahorcado.)
        No hay límite de tiempo.
        
        Para ganar, debe lograr ingresar todas las letras del título de la película.
        Mucha suerte!
        
        2 Jugadores:
        ------------
        
        En el modo de dos jugadores hay una batalla directa de uno contra otro.
        Empieza el Jugador 1 y sigue adivinando letras hasta equivocarse en la letra elegida.
        Si se equivoca, empieza el turno del Jugador 2, quien podrá adivinar letras hasta equivocarse.
        
        Quien termine de adivinar el título de la película es quien gana, no quien más letras haya adivinado.
        Para ganar, debe lograr ingresar todas las letras del título de la película.
        Mucha suerte a ambos!
        
        Presione <Enter> para continuar.
        """)
    input()
    cls()
    banner_inicio()
    opcion_inicio()

## modo de 1 jugador
def un_jugador():
    cls()
    banner_inicio()
    print("""
    **********************************************************************
    *** B I E N V E N I D O   A L   M O D O   DE   UN   J U G A D O R  ***
    **********************************************************************
          
          """)
    
    ## ingreso de nombre de jugador 1
    ingreso_nombre()

## ingreso nombre
def ingreso_nombre():
    while True:
        nombre = input("Ingrese su nombre: ")
        if nombre == "":
            continue
        else:
            jugador1 = Jugador(nombre)
            empezar_juego(1, jugador1)
            
## empezar juego
def empezar_juego(num, jugador1):
    print(jugador1.nombre)