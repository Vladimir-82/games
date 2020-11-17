from random import randint
mass=[[randint(1,10) for i in range(1,4)] for j in range(1,4)]
print(mass)
for i in mass:
    for j in i:
        if j==3:
            print(mass.index(j))

