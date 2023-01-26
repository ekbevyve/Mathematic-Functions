"""
function to show a random flashcard, on a random side
"""
flashcards= {'word1':'definition1','word2':'definition2','word3':'definition3'}
from random import *

def showflash(dictionary): 
    coin=[1,2]
#pick a random key
    words=list(flashcards)
    word=choice(words)
#pick 1 or 2 to show a definition
    toss=choice(coin)
#if 1, show definition first.
    if toss==1:
    #wait for user to hit enter
        print('\nWhat is the keyword for: \n',flashcards[word])
        input()
    #print the keyword
        print('The correct keyword was: ',word)
    if toss==2:
    #wait for user to hit enter
        print('\nWhat is the definition for: ',word)
        input()
    #print the keyword
        print('The correct definition was: \n',flashcards[word])

#testing:
for i in range(1,10):
    showflash(flashcards)


