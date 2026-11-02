#Autor: Angel Pie Santamaria
#Data: 2/11/2026
#Curs: 1r ASIX
#Descripció: Determina si es un numero primer o no
#Especificacions d'entrada: Numero enter i positiu
#--------


numero = int(input("Introdueix un número enter positiu: "))

if numero < 2:
    print("No és un nombre primer")
else:
    es_primer = True

    for i in range(2, numero):
        if numero % i == 0:
            es_primer = False

    if es_primer:
        print("És un nombre primer")
    else:
        print("No és un nombre primer")
