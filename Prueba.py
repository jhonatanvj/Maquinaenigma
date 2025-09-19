from Rotor import Rotor
from Reflector import Reflector
from Main import Enigma
from Generador_Rotores import generar_rotores

def crear_maquina(semilla):
    rotores = generar_rotores(semilla)
    rotor_izq = Rotor(rotores[0][0], rotores[0][1])
    rotor_med = Rotor(rotores[1][0], rotores[1][1])
    rotor_der = Rotor(rotores[2][0], rotores[2][1])
    reflector = Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")
    return Enigma(rotor_izq, rotor_med, rotor_der, reflector)

if __name__ == "__main__":
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Cifrar texto")
        print("2. Descifrar texto")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            semilla = input("Ingrese la semilla de 4 letras: ").upper()
            texto = input("Ingrese el texto a cifrar: ").upper()
            maquina = crear_maquina(semilla)
            resultado = maquina.cifrar_texto(texto)
            print("Texto cifrado:", resultado)

        elif opcion == "2":
            semilla = input("Ingrese la semilla de 4 letras usada en el cifrado: ").upper()
            texto = input("Ingrese el texto a descifrar en mayúsculas sin espacios: ").upper()
            maquina = crear_maquina(semilla)
            resultado = maquina.cifrar_texto(texto)
            print("Texto descifrado:", resultado)

        elif opcion == "3":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

