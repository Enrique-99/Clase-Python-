import random 

intento= 1
intentos_deljugador=6
guess=0
techo= 50
piso= 1
secret= random.randint(piso, techo)

print(" El numero esta entre 1 a 50")

while secret != guess and intento!=intentos_deljugador:

    guess= int(input("intento " + str(intento) + ": "))

    if guess==secret:
        break
    elif guess<secret:
           piso= guess
    else:
        guess>secret
        techo= guess
    print ("el numero esta entre "+ str(piso) + " y "+ str(techo))
    intento+=1

if guess==secret:
    print("Felicidades adivinaste el numero ", str(secret))
else:
    print("Se acabaron los intentos, el numero era ", str(secret))