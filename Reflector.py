from string import ascii_uppercase as ABC

class Reflector:
    def __init__(self, cableado):
        self.abc = ABC
        self.cableado = cableado

    def reflejar(self, c):
        indice = self.abc.index(c)
        return self.cableado[indice]
