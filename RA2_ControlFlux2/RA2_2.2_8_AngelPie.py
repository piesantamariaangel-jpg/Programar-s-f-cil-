#Autor: Angel Pie Santamaria
#Data: 2/11/2026
#Curs: 1r ASIX
#Descripció: Demana al usuari una frase i compta quantes vocals té
#Especificacions d'entrada: Frase
#--------


frase = input("Introdueix una frase: ")

vocals = "a, e, i, o, u"
comptador = 0

for lletra in frase:
    if lletra in vocals:
        comptador = comptador + 1

print("La frase conté", comptador, "vocals.")
