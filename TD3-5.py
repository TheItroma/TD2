letter = None
while True:
    letter = input("Entrer une lettre : ")
    if len(letter) == 1: break
    print("Ceci n'est pas une lettre individuelle, réssayer")
if ord(letter) >= 65 and ord(letter) <= 90: letter = chr(ord(letter) + 32)
if ord(letter) >= 97 and ord(letter) <= 122:
    voyel = [97, 101, 105, 111, 117]
    for i in voyel:
        if ord(letter) == i:
            print("Voyelle!")
            exit()
    print("Consonne!")
else: print("Autre!")