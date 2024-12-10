# Ejercicios
"""
1. Crear un ejercicio que me permita saber si una persona es mayor de edad
"""
# Mi solucion
edad = int(input("Ingresar edad:"))
mayor_edad = (edad >= 18) == True
print(mayor_edad)

# Solucion del profesor
anio_nacimiento = int(input("Cual es su año de nacimiento? (AAAA):"))
anio_actual = 2024
edad = anio_actual -anio_nacimiento
print("Eres mayor de edad." * (edad >= 18) + "Eres menor de edad." * (edad < 18))

# Mi solución mejorada
edad = int(input("Ingresar edad:"))
mayor_edad = "Eres mayor de edad." * (edad >= 18) + "Eres menor de edad." * (edad < 18)
print(mayor_edad)
