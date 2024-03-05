# Solicitar datos de entrada al usuario
P = float(input("Ingrese el precio de suscripción: "))
Unormal = int(input("Ingrese el número de usuarios normales: "))
Upremium = int(input("Ingrese el número de usuarios premium: "))
GT = float(input("Ingrese los gastos totales: "))

# Calcular las utilidades del proyecto considerando usuarios premium
utilidades = (P * Unormal + P * 1.5 * Upremium) - GT

# Mostrar el resultado
print("Las utilidades del proyecto son:", utilidades)
