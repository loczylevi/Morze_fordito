folytkov = True
# szótár:
thisdict = {
  ".-" : "a",
  ".--.-" : "á",
  "-..." : "b",
  "-.-." : "c",       
  "-.." : "d",       
  "." : "e",     
  "..-.." : "é",  
  "..-." : "f", 
  "--." : "g",
  "...." : "h",
  ".." : "i",
  ".---" : "j",
  "-.-" : "k",
  ".-.." : "l",
  "--" : "m",
  "-." : "n",
  "---" : "o",
  "---." : "ö",
  ".--." : "p",
  "--.-" : "q",
  ".-." : "r",
  "..." : "s",
  "-" : "t",
  "..-" : "u",
  "..--" : "ü",
  "...-" : "v",
  ".--" : "w",
  "-..-" : "x",
  "-..-" : "y",
  "--.." : "z",
  "--.--" : "!",
  "-.--.-" : ")",
  "-.--." : "(",
  "--..--" : ",",
  "-....-" : "-",
  ".-.-." : "+",
  ".-.-.-" : ".",
  "-..-." : "/",
  "---..." : ":",
  "..--.." : "?",
  ".-..-." : "\"",
  ".----." : "'",
  ".----" : "1",
  "..---" : "2",
  "...--" : "3",
  "....-" : "4",
  "....." : "5",
  "-...." : "6",
  "--..." : "7",
  "---.." : "8",
  "----." : "9",
  "-----" : "0"
}
# maga a program (ne piszkálj bele) _________________________________
print("A araktereket spacel (\" \") válaszd el különben nem működik a\nprogram! Példa: \".- .-.. -- .-"\n")
while folytkov:
    bekeres = input("Kérem a lefordítandó mondatot!\t")
    if bekeres == "Grrr":
        folytkov = False
        print(">>> Program vége <<<")
        break
    bekeres = bekeres.split(" ")
    for szo in bekeres:
        print(thisdict.get(szo,f"Nincs ilyen szó a szótárban! --> \"{b[0]}\""),end=" ")
    print("")
