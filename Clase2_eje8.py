jornada=48
htrabajador=49
pagohora=2
pagoextra=3.5
if htrabajador<=jornada:
    salario=htrabajador*pagohora
else:
    salario =(jornada*pagohora)+((htrabajador-jornada)*pagoextra)
print("Su pago total es de:",salario)