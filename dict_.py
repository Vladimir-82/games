dc={'key1':88,'key2':5,'key3':6}
values=[]
for y in dc.values():
    values.append(y)#находим максимум значения

for u,y in dc.items():#находим какому максимальному
    if y==max(values):#значению соответсветствуе:
        print(u)#ключ
        print(y)  #значение

print(sorted(dc.values()))#сортировка по значению
