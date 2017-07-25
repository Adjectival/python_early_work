# GOALS
# 1. Have a target word the user tries to guess
# 2. Prompt the user for a letter
# 3. Check whether the guess was correct or not
# 4. Display the target word with guessed letters in their correct position, and unguessed letters as underscores
# 5. Display all their incorrect guesses, as well as their remaining guesses


def is_divisible(number, divisor):
	return number % divisor == 0

def fizzbuzz_logic(num):
	if is_divisible(num, 15):
		return 'FizzBuzz!'
	elif is_divisible(num, 5):
		return 'Buzz'
	elif is_divisible(num, 3):
		return 'Fizz'
	else:
		return num

def fizzbuzz(i):
	i = int(input('How far to fizz?'))
	for j in range(1, i):
		output = fizzbuzz(j)
		print(output)

fizzbuzz()
 
# 2nd attempt
# hackman_word = 'hellos'
# until 
#	guess = raw_input('Guess a letter: ')
#	if guess

# first attempt, w/o stepping thru it
#for hackman_letter in range('w''i''t''h''h''e''l''d'):
#	guess = raw_input('Guess a letter: ')
#	if guess