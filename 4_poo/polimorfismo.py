class Deporte:
    def jugar(self):
        pass

class Futbol(Deporte):
    def jugar(self):
        print(f"Jugando fútbol")
        
class Baloncesto(Deporte):
    def jugar(self):
        print(f"Jugando baloncesto")
        
class Tenis(Deporte):
    def jugar(self):
        print(f"Jugando tenis")
        
deporte_1 = Futbol()
deporte_1.jugar()

deporte_2 = Baloncesto()
deporte_2.jugar()

deporte_3 = Tenis()
deporte_3.jugar()