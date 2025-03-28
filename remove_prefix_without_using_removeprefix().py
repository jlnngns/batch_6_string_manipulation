def custom_removeprefix(text, prefix):
    if text.startswith(prefix):
         return text[len(prefix):]
    return text

user_input = input("Enter a string: ")
prefix = input("Enter prefix to remove: ")
print("", custom_removeprefix(user_input, prefix))
