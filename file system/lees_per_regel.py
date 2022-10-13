from os import read

bestand = open("klasgenoten.txt")

for x in range(10): 
    regel = bestand.readline()
    regel = regel.strip()
    print(regel)