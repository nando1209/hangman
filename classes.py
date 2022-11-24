## class para el Jugador
class Jugador:
    def __init__(self, input_nombre):
        self.nombre = input_nombre

## class para una partida
class Partida_un_jugador:
    def __init__(self, input_pelicula, input_jugador):
        self.pelicula = input_pelicula
        self.pelicula_text = ""
        self.pelicula_en_blanco = ""
        self.jugador = input_jugador
        self.letras_acertadas = []
        self.letras_equivocadas = []
        self.intentos_restantes = 7
        self.pelicula_cargada = False
        self.pelicula_list = []
    
    def presentar_pelicula(self):
        if not self.pelicula_cargada:
            for letra in self.pelicula:
                self.pelicula_list.append(letra)
            self.pelicula_cargada = True
        
            self.pelicula_en_blanco = ""
            self.pelicula_text = ""
            for letra in self.pelicula_list:
                if letra == " ":
                    letra_text = " / "
                    letra_blanco = " / "
                elif letra == "'":
                    letra_text = " {} ". format(letra)
                    letra_blanco = " ' "
                elif letra == "." or letra == ":":
                    continue
                else:
                    letra_text = " {} ". format(letra)
                    letra_blanco = " _ "
                    
                self.pelicula_text += letra_text    
                self.pelicula_en_blanco += letra_blanco
            
            
        
        print(self.pelicula_en_blanco)
        print("\nLetras adivinadas: {}".format(self.letras_acertadas))
        print("\nLetras equivocadas: {}".format(self.letras_equivocadas))
        print("Errores restantes: {}".format(self.intentos_restantes))
        
        # for index in range(1, len(pelicula_text), 3):
        #     print(pelicula_text[index])
        