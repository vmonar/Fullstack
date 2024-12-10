"""
Crear la clase Persona, con los atributos: nombre, edad, profesión
Crear 2 metodos: saludar, despedirse
Crear 2 instancias de la clase persona y mostrar el nombre y el metodo saludar   
"""

class Persona:
    
    def __init__(self, nombre, edad, profesion):
        self.nombre = nombre
        self.edad = edad
        self.profesion = profesion
        
    def saludar(self):
        return(f"Hola mi nombre es {self.nombre}, tengo {self.edad} años y soy {self.profesion}")
    
    def despedirse(self):
        return(f"Adios {self.nombre}")
    
persona_01 = Persona("Mizael", 20, "Contador")
print(persona_01.nombre)
print(persona_01.edad)
print(persona_01.profesion)
print(persona_01.saludar())
print(persona_01.despedirse())

persona_02 = Persona("Maria", 20, "Medica")
print(persona_02.nombre)
print(persona_02.edad)
print(persona_02.profesion)
print(persona_02.saludar())
print(persona_02.despedirse())