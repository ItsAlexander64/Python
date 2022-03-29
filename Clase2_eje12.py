altura=5
espacio=altura
carac= 1
for i in range(altura):
    for j in range(espacio):
        print("  ",end="") 
    for k in range((i*2+1)):
        print("* ",end="")
    espacio-=1
    print()