print("Willkommen bei Rechner")

zahl1 = input("Schreiben Sie die erste Zahl rein : ")

zahl2 = input("Schreiben Sie die zweite Zahl rein : ")

operator = input("Was ist der Operator : ")
ergebnis = 0
if(operator == "+"):
    ergebnis = int(zahl1) + int(zahl2)
elif (operator == "/"):
    ergebnis = int(zahl1) / int(zahl2)
elif (operator == "*"):
    ergebnis = int(zahl1) * int(zahl2)
elif (operator == "-"):
    ergebnis = int(zahl1) - int(zahl2)    
print(ergebnis)