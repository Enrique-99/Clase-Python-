continuar="S"
lista=[]
x=5
while continuar.upper()=="S":
    nombre= input("captura el nombre de la persona: ")
    peso= float(input("captura el peso: "))
    altura= float(input("captura la altura: "))

    lista.append([nombre, peso,altura])
    
    continuar=input("Quieres agregar mas personas S/N?")

for elemento in lista:

    imc= round(elemento[1]/elemento[2]**2,2)

    print(elemento[0], "Tu indice de masa corporal es de ", str(imc))

    if imc<16:
        print("Criterio de ingreso a hospital")
    elif imc>=16 and imc<=17: 
        print("Infrapeso")
    elif imc>17 and imc<=18:
        print("Bajo peso")
    elif imc>18 and imc<=25:
        print("Normal")
    elif imc>25 and imc<=30:
        print("Sobrepeso")
    elif imc>30 and imc<=35:
        print("Sobrepeso Crónico")
    elif imc>35 and imc<=40:
        print("Obesidad premórbida")
    elif imc>40:
        print("Obesidad mórbida")