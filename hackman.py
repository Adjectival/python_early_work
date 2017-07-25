# GOALS
# 1. Have a target word the user tries to guess
# 2. Prompt the user for a letter
# 3. Check whether the guess was correct or not
# 4. Display the target word with guessed letters in their correct position, and unguessed letters as underscores
# 5. Display all their incorrect guesses, as well as their remaining guesses

hackman_word = ['q', 'u', 'e', 's', 't']
hackman_display = ['_','_','_','_','_']
bad_guesses = []

for i in range(0,8):
	guess = input('Guess a letter: ')
	if i == 8:
		break
	# correct guess
	elif guess in hackman_word:
		hackman_display[hackman_word.index(guess)] = guess
		# when word fully revealed, end game
		if '_' not in hackman_display:
			print('You are a Winner! You guessed it: '+str(hackman_display))
			break
		# game continues
		else:
			print('HUZZAH, good guess! That\'s letter #' + str(hackman_word.index(guess)+1)+ ' You have '+ str(7 - i) +' guesses left. Keep going!')
		# writes in correct guess over underscore
			print(hackman_display)
	# incorrect guess
	else:
		bad_guesses.append(guess)
		print('Not in this word: guess again! You have '+ str(7 - i) +' guesses left.')
		print('Bad guesses: '+ str(bad_guesses) + '\n Hackman word:' + str(hackman_display))




# 2nd attempt
# hackman_word = 'hellos'
# until 
#	guess = raw_input('Guess a letter: ')
#	if guess

# first attempt, w/o stepping thru it
#for hackman_letter in range('w''i''t''h''h''e''l''d'):
#	guess = raw_input('Guess a letter: ')
#	if guess