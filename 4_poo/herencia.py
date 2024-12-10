class animal:
    
    def __init__(self, nombre):
        self.nombre = nombre
        
    def hablar(self):
        pass
    
class perro(animal):
    def hablar(self):
        print(f"{self.nombre} puede ladrar")
        
class gato(animal):
    def hablar(self):
        print(f"{self.nombre} puede maullar")
        
animal_1 =  perro("Mordelon")
animal_2 = gato("Garfield")

animal_1.hablar()
animal_2.hablar()