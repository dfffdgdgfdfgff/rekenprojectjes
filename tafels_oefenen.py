import random

counter = 0
correct = 0
fout = 0 
tafel = int(input("welke tafel wil je oefenene?\n:"))

while counter < 10:
    counter += 1 
    oefennummer = random.randint(1,10)
    antwoord = int(input(f"{tafel} x {oefennummer} = "))
    if antwoord == (tafel*oefennummer):
        correct += 1
    else:
        fout += 1
print(f"{fout} fouten en {correct} goed")