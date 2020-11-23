from random import randint
mass=[[randint(1,10) for i in range(3)] for j in range(3)]
print(mass)
index_list=[]
number_list=[]
for i in mass:
    for j in i:
        if j==3:
            number_list.append(j)

print(number_list)
