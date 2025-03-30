def custom_zfill(text, width):
    return '0' * (width - len(text)) + text if len(text) < width else text

text = input("Enter a string: ")
width = int(input("Enter total width: "))
print("'" + custom_zfill(text, width) + "'")
