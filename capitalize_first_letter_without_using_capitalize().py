def custom_capitalize(text):
    return (chr(ord(text[0]) - 32) if 'a' <= text[0] <= 'z' else text[0]) + ''.join(chr(ord(c) + 32) if 'A' <= c <= 'Z' else c for c in text[1:])

user_input = input("Enter a string: ")
print("", custom_capitalize(user_input))
