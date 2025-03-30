def custom_islower(text):
    for cue in text:
        if 'A' <= cue <= 'Z':
            return False
    return True

text = input("Enter a string: ")
print(custom_islower(text))
