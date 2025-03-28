def custom_removesuffix(text, suffix):
    if text.endswith(suffix):
        return text[:-len(suffix)]
    return text

text = input("Enter a string: ")
suffix = input("Enter suffix to remove: ")
print("", custom_removesuffix(text, suffix))
