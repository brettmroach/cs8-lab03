# Student: Brett Roach 6907380
# CS8 (F19)

# This file contains several incomplete function definitions with stub
# values. Lab03_tests.py have tests to check if the functions are correct.
# Your assignment is to complete each function according to the
# functions' descriptions.
#
# Once you complete a function, use pytest on the test functions
# in lab03_tests.py to see if your functions are working correctly

def notStringContainingR(word):
    '''
    - Return True when word is a string that contains no letter 'r' (or 'R')
    - It should work both for lower and upper case.
    - When word isn't a string or is an empty string (""), return True
    (because it is not a string contaning an R).
    - You can check if the word value is a string with type(word) == str 
    '''
    if type(word)!=str:
        return True
    else:
        if "r" in word or "R" in word:
            return False
        #elif "R" in word:
        #    return False
        else:
            return True


def hasVowel(word):
    '''
    - Return True when word is a string that contains a vowel
    (a,e,i,o,u,A,E,I,O,U).
    - It should work for both lower and upper case vowels.
    - When word doesn't have a vowel, return False. Return True otherwise.
    - If word isn't a string, return False (because it is not a string
    containing a vowel).
    - Hint: recall the boolean operator "in" and use that when
    checking if a character is a vowel.
    '''
    vowels = ['a', 'e', 'i', 'o', 'u', "A", "E", "I", "O", "U"]
    if type(word)!=str:
        return False
    else:
        for letter in vowels:
            while letter in word:
                return True
        else:
            return False
        '''
        an alternate method using tertiary list, tally, created from
        the length of the primary list, word, which, through comparison
        of the primary and secondary lists (word & vowels) generates a list
        of True/False options, outputting "True" if "True" is in the list
        '''
    #else
        #tally=list(range(len(word)))
        #for x in range(len(word)):
        #    letter=word[x]
        #    if letter in vowels:
        #        tally[x]=True
        #    else:
        #        tally[x]=False
        ##print(tally)
        #if True in tally:
        #    return True
        #else:
        #    return False
            

def isNumber(item):
    '''
    - Return True if item is of type int or type float, otherwise return
    False.
    - You can check if item is an int with type(item) == int, and a float
    with type(item) == float
    '''
    if type(item)!=int and type(item)!=float:
        return False
    else:
        return True


def onlyContainsStrings(theList):
    '''
    - Returns True if theList is a list containing only strings.
    - The parameter theList can be anything.
    - An empty list should return False since it doesn't contain a string.
    - If theList is not a list type, return False since theList is not a list
    containing only strings.
    - Note: you can check if theList is a list with type(theList) == list
    '''
    if type(theList)!=list:
        return False
    elif len(theList)==0:
        return False
    else:
        for x in range(len(theList)):
            while type(theList[x])!=str:
                return False
        else:
            return True
                
                    




