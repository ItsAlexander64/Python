seg=59
min=59
hora=23
#Incrementar un minuto: 
print("La hora sin incrementar un min es: ",hora," : ",min," : ",seg)
if hora<=23 and min==seg<=59:
    seg+=1
    if seg==60:
        min+=1
        seg=0
    if min==60:
        hora+=1
        min=0
    if hora==24:
        hora=0
        print("La hora incrementado un min es: ",hora," : ",min," : ",seg)
else:
    print("Ingrese una hora valida")    

   