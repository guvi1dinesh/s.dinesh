#(7Q) function that takes a string and returns the most  frequent charcter in it
def frequentCharacter(stringValue):
    count = {}

    for char in stringValue:
        if char in count:
            count[char] +=1
        else:
            count[char] =1

    repeatedchar = ""
    maxcount = 0

    for char in count:
        if count[char] > maxcount:
            repeatedchar = char
            maxcount = count[char]
    return repeatedchar
print(frequentCharacter("Dinesh Kumar"))


