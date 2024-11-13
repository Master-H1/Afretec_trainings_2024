
# This fuction will return dictionary where keys are unique words and values are list of indices
def return_dict(string):
    # Create an empty dictionary to store the result.
    result = {}
    # turn the string into lower case and split it into words
    words = string.lower().split()
    
    for i, word in enumerate(words):
        if word in result:
            result[word].append(i)
        else:
            result[word] = [i]
    return result


#This will prompt user to enter any string 
string = input("Enter any string name you want: ")

# Call fucntion and pass string inside of it to store the result
res = return_dict(string)

# Print the result
print(res)