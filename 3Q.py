#Function that takes a string and returns a new string with all vowels removed
stringValue = "Dinesh Kumar S"
Anotherstring = " "

for char in stringValue.lower():
    if char not in "aeiou":
        Anotherstring += char
print(Anotherstring)

