print("Diagnóstico de Indice de masa comporal")
peso= float(input("Capture su peso en Kg: "))
altura= float(input("Capture su altura en metros: "))

imc= round(peso/altura ** 2,2)
print("Su indice de masa corporal es de", str(imc))

if imc<16:
    print("Su diagnóstico es de criterio de ingreso a hospital")
elif 16<imc<17:
     print("Su diagnóstico es de Infrapeso")
elif 17<imc<18:
     print("Su diagnóstico es de bajo peso")
elif 18<imc<25:
     print("Su diagnóstico es de peso normal (saludable)-")    
elif 25<imc<30:
    print("Su diagnóstico es de sobrepeso")
elif 30<imc<35:
     print("Su diagnóstico es de sobrepeso cronico")
elif 35<imc<40:
     print("Su diagnóstico es de obesidad premórbida")
elif imc>40:
     print("Su diagnóstico es de obesidad morbida")
