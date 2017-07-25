hackman_word = ['t', 'r', 'i', 'a', 'l']
inputted_guess = input('Guess a letter in the mystery word: ')

if inputted_guess in hackman_word:
	print("GOOD GUESS! That's letter #" + str(hackman_word.index(inputted_guess)))
