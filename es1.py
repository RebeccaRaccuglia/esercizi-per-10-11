word =input("scrivi la parola:")
word1= word[::-1] #gira la stringa
if word == word1:
    print(word, "è un palindromo")
else:
    print(word, "non è un palindromo")