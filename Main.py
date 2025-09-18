class Enigma:
    def __init__(self, rotor_izq, rotor_med, rotor_der, reflector):
        self.rotor_izq = rotor_izq
        self.rotor_med = rotor_med
        self.rotor_der = rotor_der
        self.reflector = reflector

    def cifrar_letra(self, letra):
        avanzar_med = self.rotor_der.paso()
        if avanzar_med:
            avanzar_izq = self.rotor_med.paso()
            if avanzar_izq:
                self.rotor_izq.paso()

        c = self.rotor_der.adelante(letra)
        c = self.rotor_med.adelante(c)
        c = self.rotor_izq.adelante(c)
        c = self.reflector.reflejar(c)
        c = self.rotor_izq.atras(c)
        c = self.rotor_med.atras(c)
        c = self.rotor_der.atras(c)
        return c

    def cifrar_texto(self, texto):
        return ''.join(self.cifrar_letra(c) for c in texto)
