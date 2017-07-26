# python_early_work
##foundational Py3 scripts and codelets
### Alexander Jacks : Adjectival

> 3rd week of Hack University, July 2017: Portland, Oregon

> The following exercises helped me tackle the larger goal of figuring out how to implement a Hangman game using built-in python functions.

> They were all worked out in the same session, and the Hangman terminal game was glued together as the 3 learning apps were created.


## mad_libs.py : Write a game to ask the user for a series of words.
### v2, I added a list 'user_words'to save the inputs, a requirement of Hangman gameplay.
### Using the insert() method with len(user_inputs) is just a flourish. Amend() does it more easily 
```python
user_words = []
for mad_libs_categories in ['adjective', 'adverb', 'proper noun', 'color', 'part of the body', 'plural noun', 'verb']:
	user_words.insert(len(user_words),input('Give us a word that\'s a ' + mad_libs_categories + ' --> '))
print(user_words)
```

## input_checker.py
### something simple, a bucket that prints a happy message if user input is in a list
### whipped this up in order to discover the python script to fulfill a major Hangman game mechanic
#### turned out that the index() method reports back the position of the list item, that's super handy & re-used
```python
hackman_word = ['t', 'r', 'i', 'a', 'l']
inputted_guess = input('Guess a letter in the mystery word: ')

if inputted_guess in hackman_word:
	print("GOOD GUESS! That's letter #" + str(hackman_word.index(inputted_guess)))
```

## last in our hearts and in this list, fizzbuzz! in order to build a basic classifier based on a few conditions
### this code was then (did you see it coming?) tweaked into the Game Over logic for Hangman
#### the buried input('?') as param was actually first built out somewhere else, but I captured it here for re-use
```python
#fizzbuzz
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

def fizzbuzz():
  for i in range(1, int((input('How far to fizz?: ')))):
		output = fizzbuzz_logic(i)
		print(output)

fizzbuzz()
```

## OKay, finally, the Hangman game built at Hack University by yours truly, late July 2017
```python
hackman_word = ['d', 'u', 'v', 'e', 't']
hackman_display = ['_','_','_','_','_']
bad_guesses = []

for i in range(0,10):
	guess = input('Guess a letter: ')
	if i == 10:
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
			print('HUZZAH, good guess! That\'s letter #' + str(hackman_word.index(guess)+1)+ ' You have '+ str(9 - i) +' guesses left. Keep going!')
		# writes in correct guess over underscore
			print(hackman_display)
	# incorrect guess
	else:
		bad_guesses.append(guess)
		print('Not in this word: guess again! You have '+ str(9 - i) +' guesses left.')
		print('Bad guesses: '+ str(bad_guesses) + '\n Hackman word:' + str(hackman_display))
```
