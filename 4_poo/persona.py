class Persona:
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def saludar(self):
        return(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años") 
    
persona_1 = Persona("Mizael", 20)
print(persona_1.nombre)
print(persona_1.edad)
print(persona_1.saludar())

persona_2 = Persona("Maria", 20)
print(persona_2.nombre)
print(persona_2.edad)
print(persona_2.saludar())