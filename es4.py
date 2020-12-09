print("a ciascun possibile calcolo corrisponde un valore numerico:")
print("- Area Quadrato: 1") 
print("- Area Rettangolo: 2")
print("- Area Triangolo: 3")
print("- Area Cerchio: 4")

print("Dunque. Di quale figura geometrica desideri calcolare l area?")
scelta = int(input(">>> "))
if scelta == 1:
    print("Hai scelto: Area Quadrato")
    lato = float(input("Inserisci il valore del lato del quadrato "))
    area_quadrato = lato * lato
    print("L'Area del Quadrato e:" , area_quadrato)
elif scelta == 2:
    print("Hai scelto: Area Rettangolo")
    base = float(input("Inserisci il valore della base "))
    altezza = float(input("Inserisci il valore dell altezza "))
    area_rettangolo = base * altezza
    print("L'Area del Rettangolo e: " , area_rettangolo)
elif scelta == 3:
    print("Hai scelto: Area Triangolo")
    base = float(input('Inserisci il valore della base '))
    altezza = float(input('Inserisci il valore dell altezza '))
    area_triangolo = (base * altezza) /2
    print("L'Area del Triangolo e: " , area_triangolo)
elif scelta == 4:
    print("Hai scelto: Area Cerchio")
    r = float(input('Inserisci il valore del raggio '))
    area_cerchio = (r * r) * 3.14
    print("L'Area del Cerchio e:" , area_cerchio)
else:
    print ('Nessun calcolo disponibile per la scelta effettuata!')