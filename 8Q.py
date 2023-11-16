#(8Q) function that takes a string  and returns true if it is an anagram of another string, false otherwise
def isanagram(string1, string2):
    return set(string1) == set(string2)
print(isanagram('war','raw'))
print(isanagram('win','won'))
