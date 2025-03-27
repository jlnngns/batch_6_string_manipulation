def custom_lower(me):
    result = ""
    for char in me:
        if 'A' <= char <= 'Z':
            result += chr(ord(char) + 32)
        else:
            result += char
    return result

text = input("Enter a string: ")
print("", custom_lower(text))
