
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
w=[i for i in a if i<5]
print(w)

print(list(filter(lambda i:i<5,a)))

for i in a:
    if i<5:
        print(i)