def left_justify(text, width):
    return text + ' ' * (width - len(text)) if len(text) < width else text

user_input = input("Enter a string: ")
width = int(input("Enter total width: "))
print("Left justified:", left_justify(user_input, width))
