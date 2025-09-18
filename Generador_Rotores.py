import random
import time
from datetime import datetime
from string import ascii_uppercase as ABC

primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

def flujo_hash(semilla):
    valor_semilla = sum((ord(c) - 65) * (i+1) for i, c in enumerate(semilla.upper()))
    random.seed(valor_semilla)
    while True:
        primo = random.choice(primos)
        lista = []
        for _ in range(200):
            ahora = datetime.now()
            micro = ahora.microsecond
            seg = ahora.second
            microf = abs(micro - random.randint(0, 999999))
            numero = (microf * primo + seg * 7) % 10000
            eleccion = numero % 21
            lista.append(eleccion)
        valor = (sum(lista) * primo + valor_semilla) & 0xFFFFFFFF
        yield valor
        time.sleep(random.uniform(0.05, 0.2))

def mezclar(letras, flujo):
    arr = list(letras)
    for i in range(len(arr) - 1, 0, -1):
        j = next(flujo) % (i + 1)
        arr[i], arr[j] = arr[j], arr[i]
    return arr

def crear_rotores(semilla):
    flujo = flujo_hash(semilla)
    rotores = []
    for i in range(3):
        for _ in range(26 * i):
            _ = next(flujo)
        cableado = "".join(mezclar(ABC, flujo))
        muesca = ABC[next(flujo) % 26]
        rotores.append((cableado, muesca))
    return rotores
