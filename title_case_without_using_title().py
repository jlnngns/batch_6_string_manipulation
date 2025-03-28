def custom_capitalize(text):
    return (chr(ord(text[0]) - 32) if 'a' <= text[0] <= 'z' else text[0]) + text[1:].lower()

def custom_title(text):
    words = text.split()
    return ' '.join(custom_capitalize(word) for word in words)

user_input = input("Enter a string: ")
print("", custom_title(user_input))
