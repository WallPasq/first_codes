from random import shuffle
from random import choice
from os import system

def randomPassword():
	letters = 'abcdefghijklmnopqrstuvwxyz'
	letters_lower = list(letters)
	letters_upper = list(letters.upper())
	numbers = list('0123456789')
	symbols = list('!@#$%¨&*_-+=^~´`,.:;|/')
	characters = letters_lower + letters_upper + numbers + symbols

	shuffle(characters)
	length = int(input('Enter the password length: '))
	password = []

	for i in range(length):
		password.append(choice(characters))

	shuffle(password)

	return "".join(password)

if __name__ == '__main__':
	system('cls')
	print('\nYour new password is: ' + randomPassword())
