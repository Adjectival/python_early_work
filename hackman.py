# GOALS
# 1. Have a target word the user tries to guess
# 2. Prompt the user for a letter
# 3. Check whether the guess was correct or not
# 4. Display the target word with guessed letters in their correct position, and unguessed letters as underscores
# 5. Display all their incorrect guesses, as well as their remaining guesses

hackman_word = ['g', 'u', 'e', 's', 's']

for i in range(0,8):
	guess = input('Guess a letter: ')
	if i == 8:
		break
	elif guess in hackman_word:
		print('HUZZAH, good guess! keep going!')
	else:
		print('guess again')
# 2nd attempt
# hackman_word = 'hellos'
# until 
#	guess = raw_input('Guess a letter: ')
#	if guess

# first attempt, w/o stepping thru it
#for hackman_letter in range('w''i''t''h''h''e''l''d'):
#	guess = raw_input('Guess a letter: ')
#	if guess