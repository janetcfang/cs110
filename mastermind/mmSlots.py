import random

#display the instructions and options
print ('Mastermind Game\n')
print ('Objective of the game: You have to guess the secret colors using as few tries as possible.\n')
print ('The 6 colors you can choose from are: Red (R), Orange (O), Yellow (Y), Green (G), Blue (B), Purple (P).\n')
print ('Please guess the sequence of the colors in the correct order.')

#user input slots 
slots = input("Please enter the number of slots you'd like to guess:")

#user input guess
def userInput():
    guess = raw_input('Please enter your guess as letters (e.g. ROYGB):') 
    
    while True:
        if len(guess)!= slots: #if user doesn't input enough letters...
           guess = raw_input('Please enter your guess as', slots, 'letters (e.g. ROYGB):') 
        else:
            lettersList = list(guess.upper())

            wrongLetters = False
            for letter in lettersList:
                if letter not in ['R','O','Y','G','B','P']:
                    wrongLetters = True 

            if wrongLetters == True: #gives option to user to re-input correct letters
                print 'The possible colors are R, O, Y, G, B, P'
                guess = raw_input('Please enter your guess as', slots, 'letters (e.g. ROYGB):') 


            else:
                return lettersList
                

#loop variables               
guessNum = 0 #the amount of guesses
secretCode = [] 
userGuess = []
colors = ['R','O','Y','G','B','P']
correctPosition = 0
correctColor = 0

	
#generate secret code
for i in range(slots):
	color = random.randrange(6)
	secretCode.append(colors[color])
	i=i+1


while guessNum >= 0:

    correctPlace = 0
    correctColor = 0
    checkLetters = []

    userGuess = userInput()
    guessNum = guessNum + 1

    checkGuess = list(userGuess)
    checkCode = list(secretCode)

#checking matches 
    for i in range(slots):
        if userGuess[i] == secretCode[i]:
            correctPlace += 1
            checkGuess[i] = "X"
            checkCode[i] = "X"

    for j in range(slots):

        if checkGuess[j] in checkCode and checkGuess[j] != "X" and checkGuess[j] not in checkLetters:

            if checkCode.count(userGuess[j]) > checkGuess.count(checkGuess[j]):
                correctColor += checkGuess.count(checkGuess[j])

            else:
                correctColor += checkCode.count(checkGuess[j])

            checkLetters.append(checkGuess[j])
#exact matches
    if correctPlace > 0:
        print "You have",correctPlace,"exact matches."

#partial matches
    if correctColor > 0:
        print "You have",correctColor,"partial matches."

#no matches
    if correctPlace == 0 and correctColor == 0:
        print "No matches."
 
#all correct 
    if correctPlace == slots:
        print "Congratulations, you won in", guessNum, "guesses!"
        guessNum = -1

print "Thanks for playing!"
