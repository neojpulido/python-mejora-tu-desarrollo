class Persona():
    edad = 18
    def __init__(self, nombre, nacionalidad):
        self.nombre=nombre
        self.nacionalidad=nacionalidad

    def nadar(self):
        print("Estoy nadando")


persona1 = Persona("Juan", "Peruano")

persona1.nadar()