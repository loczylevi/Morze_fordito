folytkov = True
import winsound
frequency = 2500  
rovid = 500  
hossz = 1000
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
 "'" : ".----.",
 "1" : ".----",
 "2" : "..---",
 "3" : "...--",
 "4" : "....-",
 "5" : ".....",
 "6" : "-....",
 "7" : "--...",
 "8" : "---..",
 "9" : "----.",
 "0" : "-----"
}
# maga a program (ne piszkálj bele) _________________________________
print("A betüket spacel (\" \") válaszd el különben nem működik a\nprogram! Példa: \"a l m a\"\n")
while folytkov:
    print("")
    bekeres = input("Kérem a lefordítandó mondatot!\t")
    b = bekeres.upper()
    if b == "GRRR":
        folytkov = False
        print(">>> Program vége <<<")
        break
    b = b.split(" ")
    for szo in b:
        print(thisdict.get(szo,f"Nincs ilyen szó a szótárban! --> \"{b[0]}\""),end=" ")
        szamlalo = len(thisdict[szo])
        tarolo = thisdict[szo]
        a = 0
        while a < szamlalo:
            if tarolo[a] == ".":
                a = a + 1
                winsound.Beep(frequency, rovid)
            elif tarolo[a] == "-":
                winsound.Beep(frequency,hossz)
                a = a + 1
                
    

    
