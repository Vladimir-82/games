names_list=[]
contributions_list=[]
count_of_members=int(input('Введите количество участников:'))
for i in range(1, count_of_members+1):
    member=input('Введите имя участника:')
    contribution=float(input('Введите взнос участник:'))
    names_list.append(member)
    contributions_list.append(contribution)
dic_members=dict(zip(names_list, contributions_list))
print(dic_members)

goods_list=[]
price_list=[]
count_of_goods=int(input('Введите количество товаров:'))
for i in range(1, count_of_goods+1):
    good=input('Введите название товара:')
    price=float(input('Введите цену товара:'))
    goods_list.append(good)
    price_list.append(price)
dic_goods=dict(zip(goods_list, price_list))
print(dic_goods)

contribution_from_other=float(sum(contributions_list))/count_of_members
print(contributions_list)

#тут должен быть код алгоритма распределения средств
if sum(contributions_list)==sum(price_list):

    for i, j in dic_members.items():
        difference=abs(contribution_from_other-i)
        if i> contribution_from_other:

        elif i!=contribution_from_other:

else:
    print('You entered a false data')