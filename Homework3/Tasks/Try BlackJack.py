def your_cars_give(Koloda):
    your_card = Koloda.pop()
    print('Ваша карта', your_card)
    you_cards.append(your_card)

def diller_cars_give(Koloda):
    diller_card = Koloda.pop()
    print('Карта диллера', diller_card)
    diller_cards.append(diller_card)

from random import shuffle as shuf
Koloda=[2,3,4,5,6,7,8,9,10,10,10,10,11]*4
shuf(Koloda)
print('Начнем игру!')
your_money=1000
you_cards=[]
diller_cards=[]

while True:
    if your_money <= 0:
        print('Ты потерял всё, мальчик')
        break
    you_cards.clear()
    diller_cards.clear()
    print('Введите ставку:')
    current=float(input())
    if current>your_money:
        print('У тебя нет столько денег, мальчик')
        break
    print('Начинаю раздачу')
    your_cars_give(Koloda)
    your_cars_give(Koloda)
    diller_cars_give(Koloda)

    if sum(you_cards)==21:
        print('Вы выиграли!')
        win=current*1.5
        your_money=your_money+win
        print('ваш банк', your_money)


    elif sum(you_cards)==22:
        print('Вы проиграли!')
        your_money = your_money - current
        print('ваш банк', your_money)



    while True:
        chouse=str(input('Хотите еще карту? (да/нет)'))
        if chouse=='да':
            your_cars_give(Koloda)
            print('сумма ваших очков', sum(you_cards))
            if sum(you_cards)>21:
                print('Вы прогорели!')
                your_money = your_money - current
                break
            elif sum(you_cards)==21:
                break
        else:
            print('сумма ваших очков', sum(you_cards))
            break

    while True:
        if sum(diller_cards) <= sum(you_cards):
            diller_cars_give(Koloda)

            if sum(diller_cards) > sum(you_cards) and sum(diller_cards)<=21:
                print('Вы проиграли!')
                your_money = your_money - current
                break
            elif sum(diller_cards)>21:
                print('Вы выиграли!')
                win = current * 1.5
                your_money = your_money + win
                break
            elif sum(diller_cards)==sum(you_cards):
                print('Переигровка')
                break
        else:
            print('сумма очков диллера', sum(diller_cards))
            break
        print('сумма очков диллера', sum(diller_cards))

    #print('сумма очков диллера', sum(diller_cards))

    print('ваш банк', your_money)

