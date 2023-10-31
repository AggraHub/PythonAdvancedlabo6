from enum import Enum
import sys 
from time import sleep
optie1 = "server"
optie2 = "server verwijderen"
optie3 = "server lijst"


#Keuze = input("kies uit de volgende opties: \n 'server toevoegen','server verwijderen','server lijst' \n")

if len(sys.argv) > 1:
    sys.argv[1] == optie1 or sys.argv[1] == optie2 or sys.argv[1] == optie3
    Keuze = sys.argv[1]
    print(Keuze + " is een geldige optie")
    sleep(5)
else:
    Keuze = input("kies uit de volgende opties: \n 'server toevoegen','server verwijderen','server lijst' \n")
    if Keuze == optie1:
        pass
    elif Keuze == optie2:
        pass
    elif Keuze == optie3:
        pass
    else:
        print("geen geldige optie")
        exit()

