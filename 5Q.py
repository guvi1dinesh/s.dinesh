# function that takes a string and returns true if its palindrome ,false otherwise
def Palindrome(string):
 return string == string[::-1]

string = "python"
result = Palindrome(string)
if result:
    print("True")
else:
    print("False")
