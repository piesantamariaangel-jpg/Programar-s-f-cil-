#Autor: Angel Pie Santamaria
#Data: 26/10/2026
#Curs: 1r ASIX
#Descripció: el programa calcula si ets major o menor d'edat
#Especificacions d'entrada: La teva data de naixement completa
#--------


#Autor: Angel Pie Santamaria
#Data: 26/10/2026
#Curs: 1r ASIX
#Descripció: el programa calcula si ets major o menor d'edat
#Especificacions d'entrada: La teva data de naixement completa
#--------

from datetime import date

dia = int(input("Introdueix el teu dia de naixement"))
mes = int(input("Introdueix el teu mes de naixement"))
any = int(input("Introdueix el teu any de naixement"))

data_avui = date.today()
anys = data_avui.year - any

if (anys > 18):
    print("Ets major")
if (anys < 18):
    print("Ets menor")
if (anys == 18):
    if (data_avui.month < mes):
        print("Ets menor")
    if (data_avui.month > mes):
        print("Ets major")
    if (data_avui.month == mes):
        if (data_avui.day < dia):
            print("Ets menor")
        if (data_avui.day > dia):
            print("Ets major")
        if (data_avui.day == dia):
            print("Avui fas 18 anys")
