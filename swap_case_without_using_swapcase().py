def swap_case(text):
    return ''.join(chr(ord(c) - 32) if 'a' <= c <= 'z' else chr(ord(c) + 32) if 'A' <= c <= 'Z' else c for c in text)

user_input = input("Enter a string: ")
print("", swap_case(user_input))
