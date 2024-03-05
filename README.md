### Desafío 1: Velocidad de escape

En este desafío, vamos a calcular la velocidad de escape de un planeta, que es la velocidad mínima necesaria para salir de su superficie venciendo la gravedad.

#### Descripción

La velocidad de escape se calcula utilizando la siguiente fórmula:

\[ V_e = \sqrt{2 \cdot g \cdot r} \]

Donde:

- \( V_e \): Velocidad de escape en [m/s].
- \( g \): Constante gravitacional en [m/s²].
- \( r \): Radio del planeta en [m].

#### Requerimientos

1. Crear un script llamado `escape.py` que permita calcular la velocidad de escape ingresando como datos de entrada el radio \( r \) y la constante \( g \). Los datos de entrada deben ingresarse de manera interactiva utilizando la función `input()`.

   **Puntuación:** 2.5 puntos.

2. Especificar claramente el formato en el que se deben entregar los datos de entrada con instrucciones apropiadas.

   **Puntuación:** 2.5 puntos.

#### Ejemplo

```
Ingrese el radio en Kilómetros: 6371
Ingrese la constante g: 9.8
La velocidad de Escape es 11174.6 [m/s]
```

#### Verificación

Para verificar el correcto funcionamiento del programa, se puede utilizar:

- \( g = 9.8 \, \text{m/s}^2 \)
- \( r = 6371 \) [Km]

**Resultado esperado:** Velocidad de Escape = 11174.6 [m/s]


****************

### Desafío 2: Rentabilidad

En esta actividad, vamos a desarrollar un programa en Python para calcular las utilidades de un proyecto emprendedor que ofrece un servicio de entrega de comida para mascotas. Este cálculo se realizará en tres versiones diferentes, cada una con sus propias características.

## emprendedor1.py

Este programa utiliza la fórmula básica para calcular las utilidades del proyecto. Solicita como datos de entrada el precio de suscripción (P), el número de usuarios (U) y los gastos totales (GT).

## emprendedor2.py

En esta versión, se consideran dos tipos de usuarios: normales y premium. Los usuarios premium pagan un 50% más que los usuarios normales. El programa solicita los precios de suscripción para cada tipo de usuario, así como el número de usuarios normales (Unormal), el número de usuarios premium (Upremium) y los gastos totales (GT).

## emprendedor3.py

Esta versión utiliza la fórmula original de utilidades pero también solicita las utilidades del año anterior (Uanterior). Calcula las utilidades actuales y muestra la razón entre las utilidades actuales y las del año anterior con dos decimales.

### Autor [GabrielRecabarren](https://github.com/GabrielRecabarren) 