dias=int(input("Ingrese los dias "))
anios=dias//365
meses=(dias%365)//30
semanas=(dias-(anios*365+meses*30))//7
diasrest=dias-(anios*365+meses*30+semanas*7)
print(dias,"equivale a: ",anios,"años ",meses,"meses",semanas,"semanas",diasrest,"dias")