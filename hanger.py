
words='свобода равенство братство'.split()
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

def getRandomWord(wordList):
    """Функция возвращает строку из переданного списка"""
    wordIndex=randomrandint(0, len(wordList)-1)
    return wordList[wordIndex]

def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print('Ошибочные буквы:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks='_'*len(secretWord)

    for i in range(len(secretWord)):#заменяет пропуски буквами
        if secretWord[i] in correctLetters:
            blanks=blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks: # показывает секретное слово с пробелами между буквами
        print(letter, end=' ')
    print()

def getGuess(alreadyGuessed):
    """Возвращает букву, введенную игроком.
    Эта функция проверяет, что игрок ввел одну буквк и ничего больше
    """
    while True:
        print('Введите букву')
        guess=input()
        guess=guess.lower()
        if len(guess)!=1:
            print("Поожалуйста, введите одну букву")
        elif guess in alreadyGuessed:
            print('Вы уже назвали эту букву. Назовите другую')
        elif guess not in 'абвгдежзийклмнопрстуфхцчшщъыьэюя':
            print("Пожалуйста, введите БУКВУ.")


