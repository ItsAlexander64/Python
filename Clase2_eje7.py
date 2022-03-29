import imp
from random import randint
#randint(x,y) numero aleatorio entre x y y
# random() numero aleatorio entre 0 y 1
# randrange(x,y,p) numero aleatorio entre "x" y "y" con un paso de "p"
# uniform(x,y) numero aleatorio de tipo float entre "x" y "y"
zonausuario= int(input("En que zona desea disparar"))
zonaportero=randint(1,6)
print("La zona cubierta por el portero es:",zonaportero)
if zonausuario==zonaportero:
    print("El portero atajo el gol")
else:
    print("Golaaaaso la concha de la lora")    