def smoller(member_number):
    print('My number is smaller than you guess!!!')
    return member_number//2

def bigger(member_number):
    print('My number is bigger than you guess!!!')
    return member_number


import time
number=12
member_number=None
print('i did guessed the number:')
time.sleep(3)
print('Try to guess the number!!')
time.sleep(3)

n=1
print(f'Attempt{n}')
member_number=int(input('Enter a number:'))

if number==member_number:
    print(f'Number is {number} You Win!!!')

else:
    while member_number!=number:
        print(f'Attempt{n+1}')
        member_number = int(input('Enter a number:'))
        if member_number<number:
            smoller(member_number)
        else:
            bigger(member_number)
        n=n+1

