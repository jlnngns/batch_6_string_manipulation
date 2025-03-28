def custom_center(text, width):
    padding = max(0, width - len(text))
    left_padding = padding // 2
    right_padding = padding - left_padding
    return ' ' * left_padding + text + ' ' * right_padding

user_input = input("Enter a string: ")
width = int(input("Enter total width: "))
print("'"+custom_center(user_input, width)+"'")
