def custom_isupper(sea):
    for char in sea:
        if 'a' <= 'z':
            return False
    return True

text = input("Enter a string: ")
print("", custom_isupper(text))
