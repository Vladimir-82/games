from random import shuffle

CARD_VALUES = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
CARD_SCORE = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, (11, 1)]
CARD_SUITS = ['\u2665', '\u2666', '\u2663', '\u2660']


class Card:
    def __init__(self, number):
        self.suit, self.value = divmod(number, 13)
        self.score = CARD_SCORE[self.value]

    def __str__(self):
        return '{}{}'.format(self.suit, self.value)

    def __repr__(self):
        return str(self)


class Deck:
    def __init__(self):
        self.cards = [Card(i) for i in range(52)]
        self.shuffle_deck()
        self.used_cards = []

    def __repr__(self):
        return str(self)

    def __str__(self):
        return 'Cards'

    def __len__(self):
        len(self.draw_cards())

    def shuffle_deck(self):
        shuffle(self.cards)

    def draw_card(self):
        card = self.cards.pop()
        self.used_cards.append(card)
        return card

    def get_card_scores(self, cards):
        res = sum(cards)
        return res


class Table:
    def __init__(self, gamers_count):
        self.gamers_count = gamers_count


def game():
    deck = Deck()
    dealer_cards = [deck.draw_card()]
    gamers_card = [deck.draw_card(), deck.draw_card()]
    gamers_scores = deck.get_card_scores(gamers_card)
    print(gamers_scores)

    gamers_cards=[]
    while True:
        choise = str(input('Another card?(Y/N)'))
        if choise == 'Y':
            gamers_cards = gamers_card.append(deck.draw_card())
            gamers_scores = deck.get_card_scores(gamers_cards)
            print(gamers_scores)
        print('OK')


result=game()
print(result)