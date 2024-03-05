# Solicitar datos de entrada al usuario
P = float(input("Ingrese el precio de suscripción: "))
U = int(input("Ingrese el número de usuarios: "))
GT = float(input("Ingrese los gastos totales: "))

# Calcular las utilidades del proyecto
utilidades = P * U - GT

# Mostrar el resultado
print("Las utilidades del proyecto son:", utilidades)
