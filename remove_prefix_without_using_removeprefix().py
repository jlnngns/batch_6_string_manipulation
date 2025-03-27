def custom_removeprefix(me, prefix):
    if me.startswith(prefix):
         return me[len(prefix):]
    return me

text = input("Enter a string: ")
prefix = input("Enter prefix to remove: ")
print("", custom_removeprefix(text, prefix))
