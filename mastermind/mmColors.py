import random

#display the instructions and options
print ('Mastermind Game\n')
print ('Objective of the game: You have to guess the 4 secret colors using as few tries as possible.\n')
print ('The 10 colors you can choose from are: Red (R), Orange (O), Yellow (Y), Green (G), Blue (B), Purple (P), White (W), Magenta (M), Indigo (I), Violet (V). \n')
print ('Please guess the sequence of the 4 colors in the correct order.')


#10 color options
colors = ['R','O','Y','G','B','P','W','M','I','V']

#colors
numOfColors = input('Please enter the number of colors you want (up to 10):')	
newColors = []
for c in range(numOfColors):
	newColors.append(colors[c])
colorList = ", ".join(newColors)
print colorList


#user input guess
def userInput():
    guess = raw_input("Please enter your guess as 4 letters (e.g. ROYG):") 

    while True:
        if len(guess)!= 4: #if user doesn't input 4 letters...
           guess = raw_input("Please enter your guess as 4 letters (e.g. ROYG):") 
        else:
            lettersList = list(guess.upper())

            wrongLetters = False
            for letter in lettersList:
                if letter not in newColors:
                    wrongLetters = True 

            if wrongLetters == True: #gives option to user to re-input correct letters
                print "The possible colors are ", colorList
                guess = raw_input("Please enter your guess as 4 letters (e.g. ROYG):") 


            else:
                return lettersList
                

#loop variables               
guessNum = 0 #the amount of guesses
secretCode = [] 
userGuess = []
correctPosition = 0
correctColor = 0

#generate secret code
for i in range(4):
	color = random.randrange(numOfColors)
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
    for i in range(4):
        if userGuess[i] == secretCode[i]:
            correctPlace += 1
            checkGuess[i] = "X"
            checkCode[i] = "X"

    for j in range(4):

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
    if correctPlace == 4:
        print "Congratulations, you won in", guessNum, "guesses!"
        guessNum = -1

print "Thanks for playing!"
