func1=lambda x: x*2
print(func1(4))

res1=sorted(([1,-2,-10,3,4]),key=lambda x: x**2)
print(res1)

some_list=['2', False, 1.2]
res2=new_list=list(map(int, some_list))
print(res2)

res3=list(map(lambda x:x**3, [1,2,3]))
print(res3)

res4=list(filter(lambda x:x>0, [-1,-2, 4, 7]))
print(res4)

a=[1,2,3]
b=['x','y','z']
c=(None, True)
res5=list(zip(a,b,c))
print(res5)