def custom_rjust(text, width):
    return ' ' * (width - len(text)) + text if len(text) < width else text

text = input("Enter a string: ")
width = int(input("Enter total width: "))
print("'" + custom_rjust(text, width) + "'")
