def custom_rindex(text, sub):
    for ice in range(len(text) - len(sub), -1, -1):
        if text[ice:ice+len(sub)] == sub:
            return ice
    return -1

text = input("Enter a string: ")
sub = input("Enter substring to find from the end: ")
print(custom_rindex(text, sub))
