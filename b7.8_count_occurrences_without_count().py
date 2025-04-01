def custom_count(text, sub):
    count, index = 0, 0
    while index <= len(text) - len(sub):
        if text[index:index+len(sub)] == sub:
            count += 1
        index += 1
    return count

text = input("Enter a string: ")
sub = input("Enter substring to count: ")
print(custom_count(text, sub))
