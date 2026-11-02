#Autor: Angel Pie Santamaria
#Data: 2/11/2026
#Curs: 1r ASIX
#Descripció: Demana al usuari que endivini el numero fin que l'acerti i va donant pistes
#Especificacions d'entrada: Endevina el numero
#--------


import random

numero_secret = random.randint(1, 100)

intent = int(input("Endevina el número entre 1 i 100: "))

while intent != numero_secret:
    if intent > numero_secret:
        print("Massa alt!")
    else:
        print("Massa baix!")

    intent = int(input("Torna-ho a intentar: "))

print("Felicitats! Has encertat el número!")
