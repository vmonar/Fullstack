Temperatura = float(input("Cual es la temperatura?"))
escala = input("Fahrenheit(F) o Celsius(C) =")

if escala == "C":
    Fahrenheit = str((Temperatura * 9/5) - 32)
    print(f"La temperatura es de: " + Fahrenheit + "F°")
elif escala == "F":
    Celsius = str((Temperatura - 32) * 5/9)
    print(f"La temperatura es de: " + Celsius + "C°")
else:
    print("La escala es incorrecta")