def add(object_1, object_2):
    """складывает или конкотинирует числа или строки(наоборот)"""
    if type(object_1)==int and type(object_2)==int:
        return str(object_1) + str(object_2)
    elif type(object_1)==str and type(object_2)==str:
        return int(object_1) + int(object_2)
    else:
        return None

obj1=2
obj2='3'
print(add(obj1, obj2))