import random

class Persona:
    def __init__(self, nombre="",edad=0,DNI=0,sexo="",peso=0,altura=0):
        self.nombre=nombre
        self.edad=edad
        self.DNI=DNI
        self.sexo=sexo
        self.peso=peso
        self.altura=altura

    def calcular_IMC(self):
        IMC= self.peso/self.altura**2
        if IMC<19:
            return-1
        elif IMC>19 and IMC<25:
            return 0
        else:
            return 1

    def es_mayor_edad(self):
        return  true if self.edad>18 else False

    def comprobar_sexo(self):
        if self.sexo=="H":
            return "H"
        elif self.sexo=="M":
            return "M"
        else:
            return"H"

    def Imprimir_informacion(self):
        print("Su nombre es: ",self.Nombre)
        print("Su edad es: ", str(self.edad))
        print("Su DNI es: ", str(self.DNI))
        print("El sexo es: ", self.sexo)
        print("Su peso es: ", str(self.peso))
        print("Su altura es: ",str(self.altura ))

    def genera_DNI():
        self.DNI =random.randint(10000000, 9999999)

    def capturar_informacion(self):
        self.nombre= input("Capture su nombre: ")
        self.edad= int(input("Capture su edad: "))
        self.sexo= input("Capture su sexo: ")
        self.peso= float(input("Capture su peso: "))
        self.altura= float(input("Capture su altura"))