class Person:
    def __init__(self, name, contribution:float):
        self.name=name
        self.contribution=contribution

    def get_info_person(self):
        return self.name, self.contribution

class Goods:
    def __init__(self, good, price:float):
        self.good=good
        self.price=price

    def get_info_good(self):
        return self.good, self.price

count_of_members=int(input('Введите количество участников:'))

#for i in range(1, count_of_members+1):
member_1=Person('John', 100)
member_2=Person('Ivan', 0)
member_3=Person('Natalia', 20)
dict_members={}

#dict_members.update('member_1.name': member_1.contribution)

