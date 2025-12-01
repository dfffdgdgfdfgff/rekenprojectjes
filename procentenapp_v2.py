herhalend = True

while herhalend == True:
    keuze = input(f"Wat voor soort wil je maken?\n1: hoeveel % is X van Y\n2: hoeveel is X% van Y\n3: hoeveel % is X groter dan Y\n4: hoeveel is 100% als X% Y is\nSoort: ")
    waarde_x = float(input("X: "))
    waarde_y = float(input("Y: "))

    match keuze:
        case "1":
            print(f"{round((waarde_x/waarde_y)*100, 1)}%")
        case "2":
            print(round((waarde_x/100)*waarde_y, 1))
        case "3":
            print(f"{round(((waarde_x-waarde_y)/waarde_y)*100, 1)}%")
        case "4":
            print(round((waarde_y/waarde_x)*100, 1))

''' ---SETUP VOOR HERHAALFUNCTIE---
    herhaalkeuze = (input("Wil je nog een berekening maken? (Y/N) \n: "))
    if herhaalkeuze == "N" or "n":
        herhalend = False
        print("vijne dag")
    elif herhaalkeuze == "Y" or "y":
        herhalend = True
'''