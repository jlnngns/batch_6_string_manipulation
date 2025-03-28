def custom_lower(text):
    return ''.join(chr(ord(c) + 32) if 'A' <= c <= 'Z' else c for c in text)

user_input = input("Enter a string: ")
print("", custom_lower(user_input))
