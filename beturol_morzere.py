folytkov = True
thisdict = {
 "A" : ".-",
 "Á" : ".--.-",
 "Ä" :".-.-",
 "B" :"-...",
 "C" : "-.-.",
 "D" : "-..",
 "E" : ".",
 "É" : "..-..",
 "F" : "..-.",
 "G" : "--.",
 "H" : "....",
 "I" : "..",
 "J" : ".---",
 "K" : "-.-",
 "L" : ".-..",
 "M" : "--",
 "N" : "-.",
 "O" : "---",
 "P" : ".--.",
 "Q" : "--.-",
 "R" : ".-.",
 "S" : "...",
 "T" : "-",
 "U" : "..-",
 "Ü" : "..--",
 "V" : "...-",
 "W" : ".--",
 "X" : "-..-",
 "Y" : "-.--",
 "Z" : "--..",
 "!" : "--.--",
 ")" : "-.--.-",
 "(" : "-.--.",
 "," : "--..--",
 "-" : "-....-",
 "+" : ".-.-.",
 "." : ".-.-.-",
 "/" : "-..-.",
 ":" : "---...",
 "?" : "..--..",
 "\"" : ".-..-.",
 "'" : ".----."
}
# maga a program (ne piszkálj bele) _________________________________

while folytkov:
    bekeres = input("Kérem a lefordítandó mondatot!\t")
    b = bekeres.upper()
    if b == "GRRR":
        folytkov = False
        print(">>> Program vége <<<")
        break
    b = b.split(" ")
    for szo in b:
        print(thisdict.get(szo,"Nincs ilyen szó a szótárban!"),end=" ")
    print("")
