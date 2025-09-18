from string import ascii_uppercase as ABC

class Rotor:
    def __init__(self, cableado, muesca, posicion_inicial=0):
        self.abc = ABC
        self.cableado = cableado
        self.muesca = muesca
        self.posicion = posicion_inicial

    def paso(self):
        self.posicion = (self.posicion + 1) % 26
        return self.posicion == self.abc.index(self.muesca)

    def adelante(self, c):
        indice = (self.abc.index(c) + self.posicion) % 26
        letra = self.cableado[indice]
        return self.abc[(self.abc.index(letra) - self.posicion) % 26]

    def atras(self, c):
        indice = (self.abc.index(c) + self.posicion) % 26
        letra = self.abc[self.cableado.index(self.abc[indice])]
        return self.abc[(self.abc.index(letra) - self.posicion) % 26]
