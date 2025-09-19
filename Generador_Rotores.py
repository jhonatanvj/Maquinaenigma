import random
import string

def hash_personalizado(palabra):
    alfabeto = string.ascii_lowercase
    cifrada = ""
    for letra in palabra.lower():
        if letra in alfabeto:
            pos = (alfabeto.index(letra) + 2) % 26
            cifrada += alfabeto[pos]
        else:
            cifrada += letra
    
    valor = 0
    for i, letra in enumerate(cifrada):
        asc = ord(letra) % 256
        mult = ord("contra"[i % len("contra")])
        parcial = (asc * mult) % 256
        parcial = (parcial ** 2) % 256
        parcial ^= len(palabra)
        valor = (valor + parcial) % (2**32)
    
    return valor

def generar_rotores(semilla):
    semilla_hash = hash_personalizado(semilla)
    random.seed(semilla_hash)
    alfabeto = list(string.ascii_uppercase)
    rotores = []
    for _ in range(3):
        copia = alfabeto[:]
        random.shuffle(copia)
        cableado = "".join(copia)
        muesca = random.choice(alfabeto)
        rotores.append((cableado, muesca))
    return rotores
