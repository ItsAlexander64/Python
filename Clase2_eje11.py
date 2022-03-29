anioini=1500
aniofin=2022
r="Los anios bisiestos entre "+str(anioini)+" y "+str(aniofin)+" son: "
for i in range(anioini,aniofin):
    if(i%4==0 and i%100!=0) or i%400==0:
        r=r+str(i)+","
print(r)