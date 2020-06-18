'''
Загадочная функция
Загадочная функция mystery работает следующим образом: Принимает число n и возвращает число на позиции n в массиве T - T[n].
Таблица T определяется рекурсивно следующим образом:

T(1) = [0, 1]
T(n + 1) получается следующим образом - берётся две копии T(n). В начале каждого элемента первой копии добавляется 0.
Вторая копия переворачивается и в начале каждого элемента дописывается 1. После две копии конкатенируются.

T(2) = [ 00, 01, 11, 10 ]
и

T(3) = [ 000, 001, 011, 010, 110, 111, 101, 100 ]
Помимо функции mystery реализуйте функцию mystery_inv, которая находит число в массиве T и возвращает его позицию.

Примеры
mystery(1) => 1
mystery(6) => 5
mystery_inv(6) => 7
'''

class MyClass():

    def myfunc(self, ):
        '''
        Here we write all the logic and return result

        :return:
        '''
        result = None

        return result # here we retrun result

if __name__ == '__main__':
   # Here we can make console input and check how function works

   # var = input('Input VAR: ')

   result = MyClass().myfunc()

   print(result)
