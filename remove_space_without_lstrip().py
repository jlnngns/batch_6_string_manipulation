def custom_lstrip(text):
    index = 0
    while index < len(text) and text[index] == ' ':
        index +=1
    return text[index:]

user_input = input("Enter a string with leading spaces: ")
print("", custom_lstrip(user_input))
