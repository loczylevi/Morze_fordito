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
    if bekeres == "Grrr":
        folytkov = False
        print(">>> Program vége <<<")
        break
    bekeres = bekeres.split(" ")
    for szo in bekeres:
        print(thisdict.get(szo,"Nincs ilyen szó a szótárban!"),end=" ")
    print("")
