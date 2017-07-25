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