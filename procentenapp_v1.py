keuze = input(f"Wat voor soort wil je maken?\n1: hoeveel % is X van Y\n2: hoeveel is X% van Y\n3: hoeveel % is X groter dan Y\n4: hoeveel is 100% als X% Y is\nSoort: ")
waarde_x = int(input("X: "))
waarde_y = int(input("Y: "))

match keuze:
    case "1":
        print(f"{round((waarde_x/waarde_y)*100, 1)}%")
    case "2":
        print(round((waarde_x/100)*waarde_y, 1))
    case "3":
        print(f"{round(((waarde_x-waarde_y)/waarde_y)*100, 1)}%")
    case "4":
        print(round((waarde_y/waarde_x)*100, 1))
