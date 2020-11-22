some_list=[str(i) for i in range(1, 1000)]
count=0
for i in some_list:
    if str(3) in i:
        count+=1
print(count)