import random
x=5

class Persona:
    def __init__(self, nombre="", edad=0, DNI=0, sexo="", peso=0.0, altura=0.0):
        self.nombre = nombre        
        self.edad = edad
        self.DNI = DNI
        self.sexo = sexo
        self.peso = peso
        self.altura = altura

    def calcular_IMC(self):
        IMC = self.peso / self.altura ** 2
        if IMC <19:
            return "Anorexia"
        elif IMC>= 19 and IMC <25:
            return "Normal"
        else:
            return "Sobrepeso"

    def es_mayor_edad(self):
        return True if self.edad>=18 else False

    def comprobar_sexo(self):
        if self.sexo.upper() != "H" and self.sexo.upper() != "M":
            self.sexo = "H"
    
    def imprimir_informacion(self):
        print("Nombre:" + self.nombre)
        print("Edad:" + str(self.edad))
        print("DNI:" + str(self.DNI))
        print("Sexo:" + self.sexo)
        print("Peso:" + str(self.peso))
        print("Altura:" + str(self.altura))

    def genera_DNI(self):
        self.DNI = random.randint(10000000, 99999999)

    def capturar_informacion(self):
        self.nombre = input("Captura tu nombre:")
        self.edad = int(input("Captura tu edad:"))
        self.sexo = input("Captura tu sexo:")
        self.peso = float(input("Captura tu peso:"))
        self.altura = float(input("Captura tu altura:"))
    
    