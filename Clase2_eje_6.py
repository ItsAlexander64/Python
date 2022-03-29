sexo="f"
edad=55
cotizaciones=800
aniiosServ=26
if aniiosServ>=25 and cotizaciones>=750:
    if(sexo=="m"and edad>=60) or (sexo=="f"and edad>=55):
        print("Usted aplica para jubilarse")
    else:
            print("Usted no aplica para jubilarse")
else:
    print("Usted no aplica para ser jubilado")            