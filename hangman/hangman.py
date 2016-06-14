import random

phrases = ["hello, it's me.", "hello world", "life is good", "you're one in a million", "your smile is contagious.", "it's raining cats and dogs", "are you hungry?", "thank you", "authentic italian cuisine", "a pat on the back", "best of luck", "cat got your tongue?", "quick recovery"] 
punctuation = [" ", ".", ",", "!", "?", "'"]

#randomPhrase -- returns a single phrase randomly chosen from a list
def randomPhrase(phrases):
	return random.choice(phrases)

#gameWon -- checks if the user has completely guessed the phrase
def gameWon(secretWord, lettersGuessed):
    counter = 0
    for letter in secretWord:
        for char in lettersGuessed:
            if letter == char:
                counter+=1
    if counter >= len(secretWord):
        return True
    else:
        return False
    
#generateHiddenPhrase -- returns the initial partially hidden phrase
def generateHiddenPhrase(secretWord, lettersGuessed):
    lettersAndUnders = ""
    for char in secretWord:
        if char in lettersGuessed or char in punctuation:
            lettersAndUnders+=char
        else:
            lettersAndUnders+="-"
    return lettersAndUnders

def getAvailableLetters(lettersGuessed):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    notGuessed = ""
    for char in alphabet:
        if char not in lettersGuessed:
            notGuessed+=char
    return notGuessed
    
#processGuess -- returns whether a letter matches and modifies the partially hidden phrase
def processGuess(secretWord, lettersGuessed, letter_guess):
	if letter_guess not in lettersGuessed and letter_guess in secretWord:
		lettersGuessed.append(letter_guess)
		return True
	else:
		return False

#listAsString -- returns a string representation of a list
def listAsString(list):
	s = ", ".join(list)
	return s

def hangman(secretWord):
    lettersGuessed = punctuation
    s = listAsString(phrases)
    guess_count = 8
    endGame = False
    print "Welcome to the game, Hangman!"
    print "I am thinking of a phrase that is " ,len(secretWord) ," letters long\n"
    while guess_count > 0:
        print "You have" ,guess_count ,"guesses left"
        print "Available letters: ", getAvailableLetters(lettersGuessed)
        letter_guess = raw_input("Please enter one letter at a time: ")
        letter_guess = letter_guess.lower()
        if processGuess(secretWord, lettersGuessed, letter_guess):
            print "Good guess: " ,generateHiddenPhrase(secretWord, lettersGuessed),"\n"
        else:
        	if letter_guess in lettersGuessed:
        		print "Sorry, you've already guessed that letter: " ,generateHiddenPhrase(secretWord,lettersGuessed),"\n"
        	elif letter_guess not in secretWord:
				guess_count-=1  
				print "Oops! That letter is not in my phrase: " ,generateHiddenPhrase(secretWord,lettersGuessed),"\n"
        endGame = gameWon(secretWord,lettersGuessed)
        if endGame == True:
            print "Congratulations, you won!"
            guess_count = -1
        elif guess_count == 0:
            print "Sorry, you ran out of guesses. The phrase was ", secretWord

secretWord = random.choice(phrases) 
hangman(secretWord)
