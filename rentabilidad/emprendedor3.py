# Solicitar datos de entrada al usuario
P = float(input("Ingrese el precio de suscripción: "))
U = int(input("Ingrese el número de usuarios: "))
GT = float(input("Ingrese los gastos totales: "))
Uanterior = float(input("Ingrese las utilidades del año anterior: "))

# Calcular las utilidades del proyecto y la razón entre utilidades actuales y del año anterior
utilidades_actuales = P * U - GT
razon_utilidades = utilidades_actuales / Uanterior

# Mostrar el resultado
print("Las utilidades del proyecto son:", utilidades_actuales)
print("La razón entre las utilidades actuales y las del año anterior es:", "{:.2f}".format(razon_utilidades))
