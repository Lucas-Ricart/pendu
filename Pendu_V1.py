import random
import string

def hangman() :
    #var
    letters = []
    fail = 0
    find = False
    #Select a word to find
    words = []
    with open("words.txt") as fl :
        for l in fl :
            words.append(l.rstrip('\n'))
    word = random.choice(words)
    print(word)
    while not find :
        find = True
        for l in word :
            if l in letters :
                print(l,end=' ')
            else :
                find = False
                print('_', end=' ')
        if fail > 40 :
            print('You Lose !')
            break
        if find :
            print('You Win !')
            break
        letter = input('Select a letter : ').lower()
        letters.append(letter)
        if letter not in word :
            fail +=1


hangman()