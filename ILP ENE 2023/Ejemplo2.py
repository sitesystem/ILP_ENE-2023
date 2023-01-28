# Operaciones Matemáticas

# Importar una librería o biblioteca de Funciones Matemáticas
import math as m

# ENTRADA DE DATOS
# DECLARAR O CREAR DOS VARIABLES
número_1 = float(input('Escribe un número: '))
número_2 = float(input("Escribe otro número: "))

# CONSTANTE
GRAVEDAD_TIERRA = 9.8
PI = 3.1416

# PROCESOS (Operaciones o Cálculos Matemáticos y/o Lógicos)
suma = número_1 + número_2
resta = número_1 - número_2

potencia_1 = número_1 ** número_2
potencia_2 = pow(número_1, número_2)
cuadrado = número_1	** 2
cubo = pow(número_2, 3)

raíz_cuadrada_1 = m.sqrt(9)
raíz_cuadrada_2 = pow(9, 1/2)
raíz_cúbica = pow(27, 1/3)

módulo_residuo1 = 9 % 2
módulo_residuo2 = 20 % 6

# SALIDA DE DATOS
print("REDONDEAR LA SUMA DE CONSTANTES = ", round(GRAVEDAD_TIERRA + PI, 2))
print("😊😁")
print("La suma es igual a", suma)
print("La resta es igual a", resta)

print('La suma es igual a ' + str(suma)) # CONCATENAR (Unión de 2 o más textos)
# CASTEO: Conversión de un tipo de dato en otro tipo de dato

print(f"La suma es igual a {suma}") # d: formateo de interpolación de texto

print("La potencia 1 =", round(potencia_1, 2))
print("La potencia 2 =", round(potencia_2, 4))

print("El módulo o residuo =", módulo_residuo1)
print("El módulo o residuo =", módulo_residuo2)
