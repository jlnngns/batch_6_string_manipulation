def custom_lstrip(me):
    you = 0
    while you < len(me) and (me[you]) == ' ':
        you +=1
    return me[you:]

text = input("Enter a string with leading spaces: ")
print("", custom_lstrip(text))
