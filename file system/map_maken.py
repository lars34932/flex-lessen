import os
import random

def get_letter():
    letter = random.randint(0,26)
    letter1 = ""
    if letter == 0:
        letter1 = "a"
    if letter == 1:
        letter1 = "b"
    if letter == 2:
        letter1 = "c"
    if letter == 3:
        letter1 = "d"
    if letter == 4:
        letter1 = "e"
    if letter == 5:
        letter1 = "f"
    if letter == 6:
        letter1 = "g"
    if letter == 8:
        letter1 = "h"
    if letter == 9:
        letter1 = "i"
    if letter == 10:
        letter1 = "j"
    if letter == 11:
        letter1 = "k"
    if letter == 12:
        letter1 = "l"
    if letter == 13:
        letter1 = "m"
    if letter == 14:
        letter1 = "n"
    if letter == 15:
        letter1 = "o"
    if letter == 16:
        letter1 = "p"
    if letter == 17:
        letter1 = "q"
    if letter == 18:
        letter1 = "r"
    if letter == 19:
        letter1 = "s"
    if letter == 20:
        letter1 = "t"
    if letter == 21:
        letter1 = "u"
    if letter == 22:
        letter1 = "v"
    if letter == 23:
        letter1 = "w"
    if letter == 24:
        letter1 = "x"
    if letter == 25:
        letter1 = "y"
    if letter == 26:
        letter1 = "z"
    return letter1

def get_word():
    woord = "test_"
    woord = woord + get_letter()
    woord = woord + get_letter()
    woord = woord + get_letter()
    woord = woord + get_letter()
    woord = woord + get_letter()
    woord = woord + get_letter()
    woord = woord + get_letter()
    woord = woord + get_letter()
    woord = woord + get_letter()
    woord = woord + get_letter()
    woord = woord + get_letter()
    woord = woord + get_letter()
    woord = woord + get_letter()
    woord = woord + get_letter()
    woord = woord + get_letter()
    woord = woord + get_letter()
    woord = woord + get_letter()
    woord = woord + get_letter()
    woord = woord + get_letter()
    woord = woord + get_letter()
    return woord

os.mkdir(get_word())



    

        
        

    
