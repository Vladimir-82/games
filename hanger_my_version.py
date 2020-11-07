import random
words='свобода равенство братство'.split()

def word(words):
    current_word=random(words)
    return current_word

def display(word, HANGMAN_PICS):
    show_word='*'*len(word)
    print(show_word)
    i=0
    while '*' not in


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

print('Введите букву:')
current_letter=input()
