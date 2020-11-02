def magic(num):
    res=str(num)
    return res, type(res)

num=(input("Input a number:"))
print(magic(num))