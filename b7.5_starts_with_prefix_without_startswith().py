def custom_startswith(text, prefix):
    return text[:len(prefix)] == prefix

text = input("Enter a string: ")
prefix = input("Enter prefix: ")
print(custom_startswith(text, prefix))
