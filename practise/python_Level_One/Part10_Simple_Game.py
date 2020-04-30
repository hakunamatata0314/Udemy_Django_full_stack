###########################
## PART 10: Simple Game ###
### --- CODEBREAKER --- ###
## --Nope--Close--Match--  ##
###########################

# It's time to actually make a simple command line game so put together everything
# you've learned so far about Python. The game goes like this:

# 1. The computer will think of 3 digit number that has no repeating digits.
# 2. You will then guess a 3 digit number
# 3. The computer will then give back clues, the possible clues are:
#
#     Close: You've guessed a correct number but in the wrong position
#     Match: You've guessed a correct number in the correct position
#     Nope: You haven't guess any of the numbers correctly
#
# 4. Based on these clues you will guess again until you break the code with a
#    perfect match!

# There are a few things you will have to discover for yourself for this game!
# Here are some useful hints:

# Try to figure out what this code is doing and how it might be useful to you
import random

def get_guess():
	 # guess = list(input("What is your guess? "))
	 # print("guess is", guess)
	 # return guess
	 return list(input("What is your guess? "))
	 # guess is ['1', '7', '8'], so the code should be str(number) in a list

def generate_code():
	# range() in str() will not generate numbers!!
	# digits = list(str(range(10)))
	digits = [str(num) for num in range(10)]
	random.shuffle(digits)
	t = digits[:3]
	print("code is ",t)
	return t

# Think about how you will compare the input to the random number, what format
# should they be in? Maybe some sort of sequence? Watch the Lecture video for more hints!
def generate_clues(code, userGuess):
	if userGuess == code:
		return "CODE CRACKED"

	clues = []

	# compare guess to code
	for idx, num in enumerate(userGuess):
		if num == code[idx]:
			clues.append("Match")
		elif num in code:
			clues.append("Close")
	if clues == []:
		return ['Nope']
	else:
		return clues

print("Welcome to the code cracker game!")

secretCode = generate_code()
print("Code has been generated, pls guess a 3 digit number")

clueReport = []

# keep asking until the user has gotten it right!
while clueReport != "CODE CRACKED":

	# ask for guess
	guess = get_guess()

	# give the clues
	clueReport = generate_clues(guess, secretCode)
	print("Here is the result of your guess:")
	for clue in clueReport:
		print(clue)

