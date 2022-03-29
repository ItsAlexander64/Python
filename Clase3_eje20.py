lista=["hola3","hol1a","hola3","hola4"]
print(lista)

for i in range((len(lista)-1),-1,-1):
    if lista[i] in lista[:i]:
        del (lista[i])
print(lista) 