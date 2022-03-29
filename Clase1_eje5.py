correctos=int(input("Ingrese el numero de aciertos: "))
errores=int(input("Ingrese el numero de errores"))
total=correctos+errores
Pcorrecto=(100/total)*correctos
Perrores=(100/total)*errores
print("Su puntaje final es:"+str(correctos)+"/"+str(total))
print("Su porcentaje de aciertos es: %.2f de porcentaje de errores de %.2f " %(Pcorrecto,Perrores))