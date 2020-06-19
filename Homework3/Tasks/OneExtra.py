'''
Вам передан массив чисел. Известно, что каждое число в этом масиве имеет пару, кроме одного:

[1, 5, 2, 9, 2, 9, 1] => 5

Напишите программу, которая бы максимально быстро находила это число.
'''

class MyClass():

    def myfunc(self, var):

        result = [i for i in var if var.count(i)==1]

        return result # here we retrun result

if __name__ == '__main__':
   # Here we can make console input and check how function works

   var = [1, 5, 2, 9, 2, 9, 1]

   result = MyClass().myfunc(var)

   print(result)
