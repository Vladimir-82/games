'''
Вам дан список голосов за кандидатов на выборы.

Кандидат побеждает в выборах, если он собрал больше половины всех голосов. Если такого кандидата нет, то в следующий тур выходят два участника с максимальными количествами голосов.

Ваша задача написать функцию, принивающую список голосов и возвращающая победителя либо победителей этого тура.

Пример
selection(
    [
        "Полуэкт Варфоломеев",
        "Варфоломей Полуэктов",
        "Полуэкт Варфоломеев",
    ]
) #=> "Полуэкт Варфоломеев"
selection(
    [
        "Полуэкт Варфоломеев",
        "Варфоломей Виссарионов",
        "Виссарион Полуэктов",
        "Варфоломей Виссарионов",
        "Варфоломей Виссарионов",
        "Полуэкт Варфоломеев",
    ]
) #=> ("Варфоломей Виссарионов", "Полуэкт Варфоломеев")
'''

class MyClass():

    def myfunc(self, var):
        N = len(var) // 2
        list_of_candidates = []
        votes_list = []
        for i in var:
            if i not in list_of_candidates:
                list_of_candidates.append(i)
        for i in list_of_candidates:
            votes_list.append(var.count(i))

        list_of_candidates = tuple(list_of_candidates)

        lider = sorted(votes_list)[-1]
        second = sorted(votes_list)[-2]

        dc = dict((zip(list_of_candidates, votes_list)))

        for k, v in dc.items():
            if v == lider and v > N:
                print('win', k)
            elif v == lider == second:
                print('во второй тур проходит:', k)
                continue
                if v == second:
                    print('во второй тур проходит:', k)
            else:
                if v == lider:
                    print('во второй тур проходит:', k)

                if v == second:
                    print('во второй тур проходит:', k)

if __name__ == '__main__':
   # Here we can make console input and check how function works

   var = ["Полуэкт Варфоломеев",
        "Полуэкт Варфоломеев",
        "Тугарин Змей",
        "Давыд Городецкий",
        "Давыд Городецкий"]

   result = MyClass().myfunc(var)


