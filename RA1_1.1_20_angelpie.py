# Autor: Angel
# Data: 24/09/2026
# Descripció: Programa que calcula els minuts sobrants
# --------

print = ("introdueix el numero de minuts")
minuts = input ()
hores = minuts//60
minuts_sobrants = minuts % 60
print ("tens", hores, "hores", "i", minuts_sobrants, "minuts")