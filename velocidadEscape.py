import math

def calcular_velocidad_escape():
    print("Ingrese el radio en Kilómetros:")
    radio_km = float(input())
    radio_m = radio_km * 1000  # Convertir a metros
    print("Ingrese la constante g:")
    constante_g = float(input())
    
    velocidad_escape = math.sqrt(2 * constante_g * radio_m)
    
    print(f"La velocidad de Escape es {velocidad_escape:.1f} [m/s]")

# Llamada a la función para probar
calcular_velocidad_escape()
