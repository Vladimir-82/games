'''
Проверить номер карты
Ваша задача написать программу, принимающее 16-значное число - номер кредитной карты. И проверяющей может ли такая
картa существовать.

Примечания
Алгоритм Луна: https://ru.wikipedia.org/wiki/%D0%90%D0%BB%D0%B3%D0%BE%D1%80%D0%B8%D1%82%D0%BC_%D0%9B%D1%83%D0%BD%D0%B0
'''

class MyClass():

    def myfunc(self, var):
        lst_1 = var[1::2]
        lst_2 = var[::2]
        for i in lst_2:
            if i * 2 > 9:
                lst_1.append(i * 2 - 9)
            else:
                lst_1.append(i * 2)
        if sum(lst_1)%10==0:
            result='card may exist'
        else:
            result = 'such a card does not exist'

        return result # here we retrun result

if __name__ == '__main__':
   # Here we can make console input and check how function works

   N=16
   var=[0]*N
   for i in range(N):
       var[i] = int(input('Enter numbers:'))

   result = MyClass().myfunc(var)

   print(result)
