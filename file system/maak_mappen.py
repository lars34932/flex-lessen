import os

bestand = open("klasgenoten.txt")

for x in range(10): 
    regel = bestand.readline()
    regel = regel.strip()
    os.mkdir(regel)