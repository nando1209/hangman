## imports
import os
import random
from classes import *


#   ****************************
#   *** INDICE DE FUNCIONES  ***
#   ****************************

## limpiar pantalla

## banner de inicio

## opción de jugadores (1, 2 o Ayuda)

## desplegar ayuda

## modo de 1 jugador

## ingreso nombre

## empezar juego

## elegir pelicula





#   ****************************
#   ***  F U N C I O N E S   ***
#   ****************************

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

## banner de juego 1 persona
def banner_juego_1():
    print("""
******************************************************************
****                                                          ****
****             T H E   H A N G M A N   G A M E              ****
****                                                          ****
******************************************************************
      
            A D I V I N E    L A     P E L I C U L A         
           ------------------------------------------        
      """)

## opción de jugadores (1, 2 o Ayuda)
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
            elegir_pelicula(jugador1)
            break
            
## elegir pelicula
def elegir_pelicula(jugador1):
    pelis = ['Black Panther: Wakanda Forever', 'The Menu', 'Black Adam', "Don't Worry Darling", 'Disenchanted', 'Where the Crawdads Sing', 'Smile', 'Falling for Christmas', 'The Wonder', 'Spirited', 'A Christmas Story Christmas', 'Enola Holmes 2', 'Weird: The Al Yankovic Story', 'All Quiet on the Western Front', 'Barbarian', 'Amsterdam', 'Poker Face', 'Black Panther', 'The Whale', 'Bullet Train', 'Terrifier 2', 'The Banshees of Inisherin', 'John Wick: Chapter 4', 'The Fabelmans', 'A Christmas Story', 'Bones and All', 'The Good Nurse', 'Tár', 'Slumberland', 'Glass Onion: A Knives Out Mystery', 'Enola Holmes', 'See How They Run', 'Top Gun: Maverick', 'Monica, O My Darling', 'Avatar: The Way of Water', 'X', 'Enchanted', 'My Policeman', 'R.I.P.D. 2: Rise of the Damned', 'Nope', 'She Said', 'Pearl', 'Ticket to Paradise', 'Elemental', 'The Woman King', 'Everything Everywhere All at Once', 'Babylon', 'Triangle of Sadness', 'Thor: Love and Thunder', 'Kantara', 'Terrifier', "Magic Mike's Last Dance", 'Paradise City', 'Violent Night', 'The School for Good and Evil', 'The People We Hate at the Wedding', 'The Batman', 'The Godfather', 'Causeway', 'The Bad Guys', 'Stutz', 'Top Gun', 'The Northman', 'Strange World', 'Fall', "Guillermo del Toro's Pinocchio", 'Emily', 'Yashoda', 'Home Alone', 'Empire of Light', 'Knives Out', 'Armageddon Time', 'The Shawshank Redemption', 'Lamborghini: The Man Behind the Legend', 'The Stranger', 'Chariots of Fire', 'Medieval', 'One Piece Film: Red', "Harry Potter and the Sorcerer's Stone", 'Avatar', 'Christmas with You', 'Aftersun', 'Elvis', 'Uunchai', "National Lampoon's Christmas Vacation", 'The Santa Clause', 'Spider-Man: No Way Home', 'Midsommar', 'Lost Bullet 2: Back for More', 'Interstellar', 'Call Jane', 'Luckiest Girl Alive', 'On the Line', 'American Psycho', 'Dune', 'Uncharted', 'Rogue One: A Star Wars Story', 'Lost Bullet', 'Once Upon a Time in Hollywood', 'Avengers: Endgame']
    # partida = Partida_un_jugador(pelis[random.randint(0, 99)], jugador1)
    partida = Partida_un_jugador("R.I.P.D. 2: Rise of the Damned", jugador1)
    empezar_juego(partida, jugador1)
    
## empezar juego
def empezar_juego(partida, jugador1):
    cls()
    banner_juego_1()
    partida.presentar_pelicula()
    
    adivinar_letra(partida, jugador1)

## validar letra
def validar_letra(letra):
    if len(letra) > 1:
        return False 
    return True

## adivinar_letra
def adivinar_letra(partida, jugador1):
    while True:
        cls()
        banner_juego_1()
        partida.presentar_pelicula()
        letra = input("\n{}, elegi una letra: ".format(jugador1.nombre))
        validar = validar_letra(letra)
        if validar:
            hubo_acierto = False
            for index in range(len(partida.pelicula_text)):
                if partida.pelicula_text[index].lower() == letra.lower():
                    partida.pelicula_en_blanco = partida.pelicula_en_blanco[:index] + partida.pelicula_text[index] + partida.pelicula_en_blanco[index + 1:]
                    if letra not in partida.letras_acertadas:
                        partida.letras_acertadas.append(letra)
                    hubo_acierto = True
            if hubo_acierto == False:
                if letra not in partida.letras_equivocadas:
                    partida.intentos_restantes -= 1
                    partida.letras_equivocadas.append(letra)
            
            if partida.pelicula_text == partida.pelicula_en_blanco:
                cls()
                banner_juego_1()
                partida.presentar_pelicula()
                print("Ganó!")
                break
            
            if partida.intentos_restantes == 0:
                cls()
                banner_juego_1()
                partida.presentar_pelicula()
                print("\nLo siento {}, perdiste =(\n\nLa película era:\n".format(jugador1.nombre))
                print("{} \n".format(partida.pelicula_text))
                break
            
            
        
        

    

