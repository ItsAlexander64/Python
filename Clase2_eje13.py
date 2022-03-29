frase="djf fefef"
letra = "k"
cont=0
for carac in frase:
  if carac==letra:
      cont+=1
if cont>0:
    print("La letra se encontro "+str(cont)+" vez en la frase")  
else:
      print("No se encontro ninguna "+letra+ " en la frase")    