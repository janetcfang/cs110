import random

# here is a default generateSecret, replace with your own...
def generateSecret():
	secret = []	
	colors = ["R","O","Y","G","B","P"]
	for i in range(4):
		color = random.randrange(5)
		secret.append(colors[color])
		i=i+1
	return secret
# add your other Python functions

#exact matches function
def computeExacts(secret, guess):
	correct = 0
	for i in range(4):
		if guess[i] == secret[i]:
			correct += 1
	return correct

#partial matches function 
def computePartials(secret, guess):
	correctPartialMatch = 0
	checkLetters = []
	
	for j in range(4):
		if guess[j] in secret and guess[j] != "X" and guess[j] not in checkLetters:
			if secret.count(guess[j]) > guess.count(guess[j]):
				correctPartialMatch += 	guess.count(guess[j])

			else:
				correctPartialMatch += secret.count(guess[j])
				 
		checkLetters.append(guess[j])
		return correctPartialMatch
