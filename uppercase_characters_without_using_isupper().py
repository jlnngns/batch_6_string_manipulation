def custom_isupper(input_string):
    return any('A' <= c <= 'Z' for c in input_string) and not any('a' <= c <= 'z' for c in input_string)

user_input = input("Enter a string: ")
print("Is the string uppercase?", custom_isupper(user_input))
