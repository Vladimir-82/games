'''
Из неизвестного удалённого сервера в интернете вы скачали данный кусочек обфусцированного кода.


import random

---
def f():
    o0o000o = lambda _: _[:] + _[:] + [~-min(_)]
    o000o0o = lambda : list(range(1, 256))
    oo0oo00 = o0o000o(o000o0o())
    o00o00o = lambda _: _ == 0 or len(oo0oo00) - 1 - oo0oo00[::-1].index(_) - oo0oo00.index(_) == _ + 1
    while not all([o00o00o(_) for _ in oo0oo00]):
        def oooo00o(_):
            o0000oo = []
            _ -= 1
            while _ > 0:
                def o0o0o0o(f):
                    __ = [oo0oo00[_], oo0oo00[f]]; oo0oo00[f] = __[0]; oo0oo00[_] = __[1]
                    return __
                o0000oo.append(o0o0o0o(int(random.random() * (_ + 1))))
                _ -= 1
            return o0000oo
        oooo00o(0x1ff)
    return oo0oo00


if __name__ == '__main__':
    print(f())
---


Вопросы
Что делает этот код?
Перепишите его в более читабельную форму
Если бы функция f() могла бы доработать до конца - какой вывод она бы вывела в консоль?

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
