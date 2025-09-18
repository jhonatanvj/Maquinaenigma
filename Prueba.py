from Rotor import Rotor
from Reflector import Reflector
from Main import Enigma
from Generador_Rotores import crear_rotores

if __name__ == "__main__":
    semilla = input("Ingrese la semilla de 4 letras: ").upper()
    rotores = crear_rotores(semilla)

    rotor_izq = Rotor(rotores[0][0], rotores[0][1])
    rotor_med = Rotor(rotores[1][0], rotores[1][1])
    rotor_der = Rotor(rotores[2][0], rotores[2][1])

    reflector = Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")

    maquina = Enigma(rotor_izq, rotor_med, rotor_der, reflector)

    texto = input("Ingrese el texto en mayúsculas sin espacios: ").upper()
    cifrado = maquina.cifrar_texto(texto)
    print("Texto cifrado:", cifrado)
