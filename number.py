def elem(some_list):
    another_list=[]
    for i in some_list:
        if some_list.count(i)==1:
            another_list.append(i)
    return another_list

some_list=[1, 9, 8, 8, 7, 6, 1, 6]
print(elem((some_list)))