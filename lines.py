def line(a_1,a_2,b_1,b_2):
    if a_1/b_1==a_2/b_2:
        return "Corners of lines are times"
    else:
        return "Corners of lines are NOT times"

a_1=int(input("Enter a_1:"))
a_2=int(input("Enter a_2:"))
b_1=int(input("Enter b_1:"))
b_2=int(input("Enter b_2:"))

print(line(a_1,a_2,b_1,b_2))