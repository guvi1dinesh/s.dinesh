# function that takes a string and returns number of unique characters in it
def count_unique_characters(string):
    unique_chars = set(string)
    count = len(unique_chars)
    return count

input_string =input("enter a  char string:")
unique_count = count_unique_characters(input_string)
print("Number of unique characters:", unique_count)




