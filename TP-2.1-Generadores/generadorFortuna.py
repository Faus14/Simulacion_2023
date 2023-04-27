import os
import time
import hashlib
import random

# Configuración del generador Fortuna
POOL_SIZE = 32
KEY_SIZE = 16
BLOCK_SIZE = 64

# Función para recopilar entropía del sistema
def gather_entropy():
    # Recopilar entropía del temporizador del sistema
    entropy = str(time.time()).encode()

    # Recopilar entropía del generador de números aleatorios
    entropy += str(random.random()).encode()

    # Recopilar entropía de los datos de os.urandom()
    entropy += os.urandom(POOL_SIZE)

    # Calcular el hash SHA-256 de la entropía recolectada
    digest = hashlib.sha256(entropy).digest()

    # Devolver los primeros 16 bytes del hash como clave de entropía
    return digest[:KEY_SIZE]

# Función para generar una secuencia de bytes aleatoria utilizando Fortuna
def fortuna_bytes(n):
    # Inicializar la clave de entropía y el contador de bloques
    key = b'\x00' * KEY_SIZE
    counter = 0

    # Generar una secuencia de bytes aleatoria de longitud n
    result = b''
    while len(result) < n:
        # Generar una nueva clave de cifrado utilizando Fortuna
        if counter == 0:
            key = gather_entropy()
            counter = BLOCK_SIZE // KEY_SIZE

        # Cifrar el contador actual utilizando la clave actual
        counter_bytes = counter.to_bytes(KEY_SIZE, 'big')
        cipher = hashlib.new('AES', key + counter_bytes)
        block = cipher.encrypt(counter_bytes)

        # Actualizar el contador y la clave de cifrado
        counter -= 1
        if counter == 0:
            key = cipher.digest()

        # Agregar el bloque cifrado al resultado
        result += block

    # Devolver los primeros n bytes del resultado
    return result[:n]


fortuna_bytes(123456)