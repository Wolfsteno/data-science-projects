# Python Cheat Sheet

# 1. Variables y Tipos de Datos
# Python determina automáticamente el tipo de una variable según el valor asignado.

# Entero
edad = 30

# Flotante
precio = 19.99

# Cadena de texto
nombre = "Juan"

# Booleano
es_activo = True

# Lista (como los arreglos en otros lenguajes)
frutas = ["manzana", "banana", "cereza"]

# Diccionario (pares clave-valor)
persona = {"nombre": "Juan", "edad": 30, "ciudad": "Nueva York"}

print(edad, precio, nombre, es_activo, frutas, persona)

# 2. Condicionales
# Python usa indentación (4 espacios o una tabulación) en lugar de llaves.

edad = 18
if edad >= 18:
    print("Eres un adulto.")
else:
    print("Eres un menor de edad.")

# 3. Bucles
# Bucle For

# Recorrer una lista
frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print(fruta)

# Bucle While
i = 1
while i <= 5:
    print(i)
    i += 1

# 4. Funciones
# Python define funciones usando la palabra clave def.

def saludar(nombre):
    return f"¡Hola, {nombre}!"

print(saludar("Alicia"))

# 5. Clases y Objetos
# Python soporta Programación Orientada a Objetos (POO).

class Perro:
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza
    
    def ladrar(self):
        return f"{self.nombre} dice ¡Guau!"

perro1 = Perro("Buddy", "Golden Retriever")
print(perro1.ladrar())

# 6. Comprensión de Listas
# Una forma concisa de crear listas.

# Crear una lista con los cuadrados de los números del 1 al 5
cuadrados = [x**2 for x in range(1, 6)]
print(cuadrados)

# 7. Manejo de Excepciones
# Manejo de errores usando try y except.

try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("No se puede dividir por cero.")

# 8. Manejo de Archivos
# Abrir, leer, escribir y cerrar archivos.

# Escribir en un archivo
with open("ejemplo.txt", "w") as archivo:
    archivo.write("¡Hola, Mundo!")

# Leer de un archivo
with open("ejemplo.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)

# 9. Importar Bibliotecas
# Puedes importar bibliotecas integradas de Python o externas.

import math

# Usar funciones de la biblioteca math
print(math.sqrt(16))  # Salida: 4.0
