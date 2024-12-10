""" 
Crear una funcion que pida al usuario 2 notas y devuelva la nota mayor de ellas
"""

nota1 = float(input("Ingrese su primera nota: "))
nota2 = float(input("Ingrese su segunda nota: "))

def notaMayor():
    if nota1 > nota2:
        print("Su nota más alta es:", nota1)
    else:
        print("Su nota más alta es:", nota2)
notaMayor()