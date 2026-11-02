#Autor: Angel Pie Santamaria
#Data: 2/11/2026
#Curs: 1r ASIX
#Descripció: Mostra els 10 primers termes de la seqüència de Fibonnaci
#Especificacions d'entrada: ---
#--------


a = 0
b = 1

for i in range(10):
    print(a)
    suma = a + b
    a = b
    b = suma
