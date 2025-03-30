def custom_upper(text):
    return ''.join(chr(ord(c) - 32) if 'a' <= c <= 'z' else c for c in text)

text = input("Enter a string: ")
print("", custom_upper(text))
