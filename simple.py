def simple(number):
    '''Определяет простое число или нет'''
    counter=0
    for i in range(1, number+1):
        if number%i==0:
            counter+=1
    return "The number is simple" if counter==2 else "The number is not simple"

num=int(input("Enter a number:"))
print(simple(num))