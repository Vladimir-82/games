def poly(string):
    lst=list(string)
    if ' ' in lst:
        lst.remove(' ')

    if lst==lst[::-1]:
        return 'True'
    else:
        return 'False'


string=str(input('enter a string:'))
print(poly(string))