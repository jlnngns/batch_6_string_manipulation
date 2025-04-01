def custom_index(text, sub):
    for ice in range(len(text) - len(sub) + 1):
        if text[ice:ice+len(sub)] == sub:
            return ice
    return -1

text = input("Enter a string: ")
sub = input("Enter substring to find: ")
print(custom_index(text, sub))
