def custom_endswith(text, suffix):
    return text[-len(suffix):] == suffix if len(text) >= len(suffix) else False

user_input = input("Enter a string: ")
suffix = input("Enter suffix to check: ")
print("Ends with given suffix?", custom_endswith(user_input, suffix))
