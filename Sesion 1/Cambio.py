print("Ingrese las monedas que tenga")
#Guardamos la cantidad de monedas que tenga el usuario
moneda_10= int(input("monedas de 10: "))
moneda_5= int (input("monedas de 5: "))
moneda_2= int (input("monedas de 2: "))
moneda_1=  int(input("monedas de 1: "))
moneda_50c=  float (input("monedas de .50: "))
moneda_20c= float(input("monedas de .20: "))
moneda_10c=     float (input("monedas de .10: "))
#Contamos las monedas que nos dio el usuario
M10= moneda_10*10
M5= moneda_5*5
M2= moneda_2*2
M1= moneda_1
M50c= (moneda_50c*.50)
M20c= (moneda_20c*.20)
M10c= (moneda_10c*.10)

Total= M10+M5+M2+M1+M50c+M20c+M10c

print("Usted tiene en total", str(Total), "pesos")