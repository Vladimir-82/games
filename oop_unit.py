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

count_of_members=3
John=Person('John', 100)
Ivan=Person('Ivan', 0)
Nataly=Person('Nataly', 20)

count_of_goods=3
Vodka=Goods('Smirnoff', 100)
Presic=Goods('Durex', 10)
Candy=Goods('Snikers', 10)

#print(Ivan.contribution)
Totall_contribution=John.contribution + Ivan.contribution + Nataly.contribution
print(Totall_contribution)
Summory_from_each_ather=Totall_contribution/count_of_members
print(Summory_from_each_ather)

Totall_goods=Vodka.price + Presic.price + Candy.price

contribution_list=[]

if Totall_contribution==Totall_goods:
    for i in John.contribution, Ivan.contribution, Nataly.contribution:
        contribution_list.append(i)
        if i > Summory_from_each_ather:
            diff=i-Summory_from_each_ather
        elif i < Summory_from_each_ather:
            diff=Summory_from_each_ather-i
        else:
            

else:
    Print('You have a mistake price goods or contributions members')