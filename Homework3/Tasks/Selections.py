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
        list_of_candidates = []
        votes_list = []
        n = len(var) // 2
        for i in var:
            if i not in list_of_candidates:
                list_of_candidates.append(i)
        candidate_1 = list_of_candidates[0]
        candidate_2 = list_of_candidates[1]
        candidate_3 = list_of_candidates[2]
        votes_1 = var.count(candidate_1)
        votes_list.append(votes_1)
        votes_2 = var.count(candidate_2)
        votes_list.append(votes_2)
        votes_3 = var.count(candidate_3)
        votes_list.append(votes_3)
        dc = dict((zip(list_of_candidates, votes_list)))

        lider = sorted(votes_list)[-1]
        second = sorted(votes_list)[-2]
        if max(votes_list) > n:
            for k, v in dc.items():
                if v == lider:
                    return print('win', k)
        elif lider == second:
            for k, v in dc.items():
                if v == lider == second:
                    return print('во второй тур проходит', k)
        else:
            for k, v in dc.items():
                if v == lider:
                    return print('во второй тур проходит', k)
                if v == second:
                    return print('во второй тур проходит', k)


if __name__ == '__main__':
   # Here we can make console input and check how function works

   var = ["Полуэкт Варфоломеев",
        "Полуэкт Варфоломеев",
        "Тугарин Змей",
        "Тугарин Змей",
        "Давыд Городецкий",
        "Давыд Городецкий",
        "Давыд Городецкий"]

   result = MyClass().myfunc(var)


