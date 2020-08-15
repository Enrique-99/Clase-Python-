Horas= int(input("Cuantas horas trabajo: "))

if Horas<40:
    salario= Horas*16
    print("Usted trabajo por",Horas,"horas y su salario es de",salario,"pesos")
else:
    horas_extra= Horas-40
    salario= (40*16)+(horas_extra*20)
    print("Usted trabajo por",Horas,"horas y su salario es de",salario,"pesos")