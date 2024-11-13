# This function will takes a list of string and returns a list of tuple
def find_palindromes(strings):
    palindromes = []
    for string in strings:
        # check if the string is a palindrome
        if string == string[::-1]:
            palindromes.append((string, True))
        else:
            palindromes.append((string, False))
    return palindromes


# Let create a sample list of mixed strings
strings = ["racecar", "hello", "level", "madam", "noon", "radar", "civic", "sail","plan","panama","Was","cat","saw"]

# Call the function and print the result
print(find_palindromes(strings))