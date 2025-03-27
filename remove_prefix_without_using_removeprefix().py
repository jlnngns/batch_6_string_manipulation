def custom_removeprefix(me, prefix):
    if me.startswith(prefix):
         return me[len(prefix):]
    return me

