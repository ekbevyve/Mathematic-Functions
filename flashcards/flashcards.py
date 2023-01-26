#tm112 glossary python flashcard program
"""
this code uses a dictionary made up of exported definitions and keys,
showing to user the key and upon pressing enter the definition is displayed as well.
"""

from random import *
def showflash(flashcards):
    """
    function to show a random flashcard, on a random side
    """
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

def makeadict(filename):
    """
    fuction makes a dictionary from a csv file.
    """
    import csv
    #initializing variables, opening files
    file = open(filename, 'r')
    table ={}
    reader = csv.reader(file)
    for row in reader:
        #append dictionary with the key and data
        table[row[0]]=row[1]
    return table
#testing function

glossary=makeadict('TM112_Glossary.txt')
contin='y'
while contin=='y':
    showflash(glossary)
    contin=input('\nShow a new card? y for yes, n for no')
    if contin!='y' and contin!='n':
        while contin!='y' and contin!='n':
            contin=input('please enter y or n: ')
