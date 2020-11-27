import random

def letter_being_allready():
    letter_list = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т',
                   'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ь', 'э', 'ю', 'я']

    current_letter=None
    while current_letter not in letter_list:
        current_letter = input('Введите букву русского алфавита:')
    current_letter=current_letter.lower()
    return current_letter
    '''
    named_letters=[]
    if current_letter not in letter_list:
        print('Введите букву!')
        return -1
    if current_letter not in named_letters:
        named_letters.append(current_letter)
        return current_letter
    else:
        print('Вы называли эту букву!')
        return -1
'''
def display(HANGMAN_PICS, WORDS):

    choes = random.randint(0, len(WORDS) - 1)
    current_word = WORDS[choes]
    show_current_word = '*' * len(current_word)
    print(show_current_word)

    index_hangman = 0

    while '*' in show_current_word:
        #current_letter = input('Введите букву:')
        #current_letter=current_letter.lower()
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
            if index_hangman==len(HANGMAN_PICS)-1:
                print('YOU LOST')
                break
            index_hangman+=1

WORDS = 'кот ёжик собака'.split()
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
display(HANGMAN_PICS, WORDS)

print()
