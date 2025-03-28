def custom_rsplit(text):
    index = len(text) - 1
    while index >= 0 and text[index] == ' ':
        index -= 1
    return text[:index+1]

text = input("Enter a string with trailing spaces: ")
print("'" + custom_rsplit(text) + "'")
