'''
В классическом варианте игра рассчитана на двух игроков. Каждый из игроков задумывает и записывает тайное 4-значное
число с неповторяющимися цифрами. Игрок, который начинает игру по жребию, делает первую попытку отгадать число. Попытка — это 4-значное число с неповторяющимися цифрами, сообщаемое противнику. Противник сообщает в ответ, сколько цифр угадано без совпадения с их позициями в тайном числе (то есть количество коров) и сколько угадано вплоть до позиции в тайном числе (то есть количество быков).

При игре против компьютера игрок вводит комбинации одну за другой, пока не отгадает всю последовательность.

Ваша задача реализовать программу, против которой можно сыграть в "Быки и коровы"

Пример
Загадано число 3219

>>> 2310
Две коровы, один бык
>>> 3219
Вы выиграли!
'''

class MyClass():

    def myfunc(self, n):
        my_number='1234'
        for i in my_number:
            if i in n:
        result = None

        return result # here we retrun result

if __name__ == '__main__':
   # Here we can make console input and check how function works

   # var = input('Input VAR: ')

   result = MyClass().myfunc('3219')

   print(result)

