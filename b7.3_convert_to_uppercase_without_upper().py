def custom_upper(text):
    return ''.join(chr(ord(cue) - 32) if 'a' <= cue <= 'z' else cue for cue in text)

text = input("Enter a string: ")
print("", custom_upper(text))
