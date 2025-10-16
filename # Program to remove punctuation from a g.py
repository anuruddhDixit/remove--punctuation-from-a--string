# Program to remove punctuation from a given string

# Define the punctuation characters
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

# Take input from the user
text = input("Enter a string: ")

# Initialize an empty string to store the result
no_punct = ""

# Iterate through each character in the string
for char in text:
    if char not in punctuations:
        no_punct += char

print("String without punctuation:", no_punct)
