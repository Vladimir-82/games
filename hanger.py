
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

    blanks='*'*len(secretWord)

    for i in range(len(secretWord)):#заменяет пропуски буквами
        if secretWord[i] in correctLetters:
            blanks=blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks: # показывает секретное слово с пробелами между буквами
        print(letter, end=' ')
    print()

def getGuess(alreadyGuessed):
    """Возвращает букву, введенную игроком.
    Эта функция проверяет, что игрок ввел одну букву и ничего больше
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
        else:
            return guess

def playAgain():
    """эта функция возвращает значение True, если игрок сиграть заново
    В противном случае False"""
    print('Хотите сыграть ещё? (Да или Нет')
    return input().lower().startswith('д')


print('В И С И Л И Ц А')
missedLetters=''
correctLetters=''
secretWord=getRandomWord(words)
gameIsDone=False

while True:
    displayBoard(missedLetters, correctLetters, secretWord)

    guess=getGuess(missedLetters+correctLetters)#позволяет ввести букву
    if guess in secretWord:
        correctLetters=correctLetters+guess

        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters=False
                break
        if foundAllLetters:
            print('Да Секретное слово - "' + secretWord + '" Вы угадали!')
            gameIsDone=True

    else:
        missedLetters=missedLetters+guess

        if len(missedLetters) == len(HANGMAN_PICS)-1:
            displayBoard(missedLetters, correctLetters, secretWord)

        print('Вы исчерпали все попытки!')
    gameIsDone=True

    if gameIsDone:
        if playAgain():
            missedLetters=''
            correctLetters=''
            gameIsDone = False
            secretWord = getRandomWord(words)
        else:
            break