#Autor: Angel Pie Santamaria
#Data: 2/11/2026
#Curs: 1r ASIX
#Descripció: Calcula la suma dels primers 100 nombres enters positius de 1 a 100 i mostra el resultat.
#Especificacions d'entrada: ---
#--------

numero = 1
resultado = numero

while numero <= 100:
    resultado = numero + resultado
    numero += 1

print(resultado) 