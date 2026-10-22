#Autor: Angel Pie Santamaria
#Data: 13/10/2026
#Curs: 1r ASIX
#--------


nom = input("Introdueix el nom: ")
cognom = input("Introdueix el cognom: ")
edat = int(input("Introdueix l'edat: "))
ciutat = input("Introdueix la ciutat: ")
cicle = input("Introdueix el cicle formatiu: ")
nom_complet = (nom + " " + cognom).upper()
edat_futura = edat + 1
correu = (nom + "." + cognom + "@alumnes.cat").lower()
print("FITXA DE L'ALUMNE")
print("Nom complet: " + nom_complet)
print("Edat l'any vinent: " + str(edat_futura) + " anys")
print("Ciutat: " + ciutat)
print("Cicle: " + cicle)
print("Correu: " + correu)
