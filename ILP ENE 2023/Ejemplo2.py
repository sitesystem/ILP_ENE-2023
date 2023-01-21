# Operaciones Matemáticas

# ENTRADA DE DATOS
# DECLARAR O CREAR DOS VARIABLES
número_1 = 10
número_2 = 2

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

# raíz_cuadrada_1 = sqrt()
# raíz_cuadrada_2 = 
# raíz_cúbica = 

# módulo_residuo = 

# SALIDA DE DATOS
print("REDONDEAR LA SUMA DE CONSTANTES = ", round(GRAVEDAD_TIERRA + PI, 2))
print("😊😁")
print("La suma es igual a", suma)
print("La resta es igual a", resta)

print('La suma es igual a ' + str(suma)) # CONCATENAR (Unión de 2 o más textos)
# CASTEO: Conversión de un tipo de dato en otro tipo de dato

print(f"La suma es igual a {suma}") # d: formateo de interpolación de texto

print("La potencia 1 =", potencia_1)
print("La potencia 2 =", potencia_2)
