class Persona():
    def __init__(self):
        pass

    def brincar (self):
        print ("Brinco")

    @classmethod
    def correr (cls):
        print ("Nado")

    @staticmethod
    def nadar():
        print ("Nado")


jose = Persona()
jose.nadar()