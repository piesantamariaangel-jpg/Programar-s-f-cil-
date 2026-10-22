#Autor: Angel Pie Santamaria
#Data: 13/10/2026
#Curs: 1r ASIX
#--------

IVA = 0.21

producte_sense_IVA = float(input("Introdueix el preu del producte sense IVA: "))
unitats = int(input("Introdueix el nombre d'unitats: "))

preu_amb_IVA = (producte_sense_IVA * IVA) + producte_sense_IVA
preu_total = preu_amb_IVA * unitats

print("Preu per unitat amb IVA:", preu_amb_IVA, "€")
print("Preu total amb IVA:", preu_total, "€")