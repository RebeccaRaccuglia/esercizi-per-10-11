words= input("scrivi una lista con la formula: parola1, parola2,...")
lista1 = words.split (",")
lista2= []
for parola in lista1:
    lunghezza= len (parola)
    lista2.append (lunghezza - 1)
print (" lunghezza delle parole: ", lista2)