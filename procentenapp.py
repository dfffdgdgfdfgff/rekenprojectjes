def mainloop():
    print("Wat voor soort wil je maken?")
    print("1: hoeveel is X% van Y")
    print("2: hoeveel % is X van Y")
    print("3: X neemt toe met Y%")
    print("4: X neemt af met Y%")
    print("5: X is toegenomen naar Y, met hoeveel % is dat?")
    print("6: Z neemt toe met X% en is nu Y")
    keuze = input("Soort: ")
    waarde_x = float(input("X: "))
    waarde_y = float(input("Y: "))

    match keuze:
        case "1":
            print(round((waarde_x/100)*waarde_y, 1))
        case "2":
            print(f"{round((waarde_x/waarde_y)*100, 1)}%")
        case "3":
            print(f"{round(waarde_x+(waarde_x*(waarde_y/100)), 1)}")
        case "4":
            print(f"{round(waarde_x-(waarde_x*(waarde_y/100)), 1)}")
        case "5":
            print(f"{round((waarde_y-waarde_x)/waarde_x)*100, 1}%")
        case "6":
            print(f"Z = {round(waarde_y/(1+waarde_x/100), 2)}")

    herhaalkeuze = (input("Wil je nog een berekening maken? (Y/N) \n: "))
    if herhaalkeuze.lower() in ("n"):
        print("fijne dag")
    elif herhaalkeuze.lower() in ("y"):
        mainloop()

mainloop()
