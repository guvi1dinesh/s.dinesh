#(1Q) python program to calculate total no of vowels and count of each individual vowel AEIOU in the string
stringValue = "Guvi Geeks Network Private limited"
vowels = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}
total = 0
for char in stringValue.lower():
    if char in "aeiou":
        vowels[char] += 1

for key in vowels:
    print(f"number of {key} is {vowels[key]}")
    total += vowels[key]
    print(f"total number of vowels {total}")





