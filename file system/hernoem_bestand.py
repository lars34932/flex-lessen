import os

nieuwe_naam = input("Nieuwe bestandsnaam: ")
bestandsnaam = "test"
huidige_map = os.getcwd()
volledige_pad = os.path.join(huidige_map, bestandsnaam)

if len(nieuwe_naam) > 0:
    nieuwe_volledige_pad = os.path.join(huidige_map, nieuwe_naam)
    print("Bestand wordt hernoemd naar: " + nieuwe_naam)
    os.rename(volledige_pad, nieuwe_volledige_pad)
    print("Bestand hernoemd")
else:
    print("Sorry, geen geldige invoer, einde programma")