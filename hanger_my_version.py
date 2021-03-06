import random

def letter_being_allready():
    named_letters = []
    letter_list = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т',
                   'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ь', 'э', 'ю', 'я']

    while True:
        current_letter=input('Введите букву:')
        if current_letter not in named_letters or current_letter not in letter_list:

            if current_letter not in named_letters:
                named_letters.append(current_letter)
            else:
                print('Вы уже называли эту букву!')

            if current_letter not in letter_list:
                print('Введите букву русского алфавита:')


        return current_letter


def display(HANGMAN_PICS, WORDS):

    choes = random.randint(0, len(WORDS) - 1)
    current_word = WORDS[choes]
    show_current_word = '*' * len(current_word)
    print((HANGMAN_PICS[0]))
    print(show_current_word)

    index_hangman = 1

    while '*' in show_current_word:
        current_letter=letter_being_allready()

        if current_letter in current_word:

            for index_letter in range(len(current_word)):
                if current_word[index_letter]==current_letter:
                    show_current_word = show_current_word[0:index_letter:] + current_letter + show_current_word[index_letter + 1::]
                    print(show_current_word)
                    if '*' not in show_current_word:
                        print('YOU WON')

        else:
            print((HANGMAN_PICS[index_hangman]))
            print(show_current_word)
            if index_hangman==len(HANGMAN_PICS)-1:
                print('YOU LOST')
                break
            index_hangman+=1

WORDS = 'кот ёжик собака корова лошадь тигр лев шакал пантера слон жираф носорог бегемот броненосец медведь лиса волк заяц кролик кобан рысь'.split()
HANGMAN_PICS=["""
 +---+
     |
     |
     |
    ===""", """
 +---+
 o   |
     |
     |
    ===""", """
 +---+
 o   |
 |   |
     |
    ===""", """
 +---+
 o   |
/|   |
     |
    ===""", """
 +---+
 o   |
/|\  |
     |
    ===""", """
 +---+
 o   |
/|\  |
/    |
    ===""", """
 +---+
 o   |
/|\  |
/ \  |
    ==="""]



print('Начнем!')
print()
print('Попробуйте отгадать животное, или будете повешаны!!!')
while True:
    display(HANGMAN_PICS, WORDS)
    game=input('Поиграем еще? (Да, Нет):').lower()
    if game=='y' or game=='yes' or game=='д' or game=='да':
        print('Ok!')
    else:
        print('Goodbuy!')
        break