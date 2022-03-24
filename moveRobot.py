# My second game in Python
# Developed by Wallacy Pasqualini
# Contact me: wallacypasqualini@gmail.com
# LinkedIn: https://www.linkedin.com/in/wallacypasqualini
# See other projects in my GitHub: https://github.com/WallPasq


from time import sleep
from os import system
from numpy import ones
from numpy import int8


class Grid():
	# Create a class for the wall object

	def __init__(self, height, width):
		# Defines how the object should be initialized. As it's a wall, it needs to receive the height and width parameters.
		self.height = height
		self.width = width
		self.path = []
		self.grid = ones((height, width), dtype = int8)


	def print_grid(self):
		# Prints the wall on the user's screen, with the respective holes.
		for row in self.grid:
			print(' '.join(['O' if i == 1 else 'X' for i in row]))


	def holes(self):
		# Allows the user to insert holes in the wall.
		# Note: Since indexing in Python starts at 0, the method is constructed so that the user can treat indexing as starting at 1.
		decision = 'y'
		while decision == 'y':
			system('cls')
			print('Let\'s add some holes in the following wall:\n')
			self.print_grid()
			x = int_num(input('\nEnter the desired row for the hole: ')) - 1
			y = int_num(input('\nEnter the desired column for the hole: ')) - 1

			while (x == 0 and y == 0) or (x == (self.height - 1) and y == (self.width - 1)) or x >= self.height or y >= self.width:
				system('cls')
				print(f'Any of the following rules were broken:\n\n' \
					  f'1) The coordinates are equal to 1, that is, equal to\n' \
					  f'the origin point (1, 1);\n\n' \
					  f'2) The coordinates are equal to the arrival point,\n' \
					  f'i.e. ({self.height}, {self.width});\n\n' \
					  f'3) The coordinates go beyond the wall boundaries.\n\n' \
					  f'Resetting the coordinate...\n')
				print('Let\'s add some holes in the following wall:\n')
				self.print_grid()
				x = int_num(input('\nEnter the desired row for the hole: ')) - 1
				y = int_num(input('\nEnter the desired column for the hole: ')) - 1

			self.grid[x][y] = 0
			print('\nThis is the new wall:\n')
			self.print_grid()
			decision = input('\nAdd another hole? (y/n) ')
			decision = decision.lower()

			while decision != 'y' and decision != 'n':
				decision = input('\n!!! Please enter y or n !!! ')
				decision = decision.lower()


	def move_robot(self):
		# If it's possible for the robot to move from the origin point to the destination point,
		# an animation will be shown on the user's screen, with this movement.
		# Otherwise, a message will be returned to the user.
		cache = {}
		self.path = []
		self.find_path(self.grid, self.height - 1, \
					   self.width - 1, cache)
		if len(self.path):
			new_grid = []
			replay = 'y'
			for x in range(self.height):
				new_grid.append([])
				for y in range(self.width):
					if self.grid[x][y] == 1:
						new_grid[x].append('O')
					else:
						new_grid[x].append('X')

			while replay == 'y':
				for coordinate in self.path:
					new_grid[coordinate[0]][coordinate[1]] = 'R'
					system('cls')
					for row in new_grid:
						print(' '.join([i for i in row]))
					new_grid[coordinate[0]][coordinate[1]] = 'O'
					sleep(0.5)
				replay = input('\nWant to review the robot\'s movement? (y/n): ')
				replay = replay.lower()

				while replay != 'y' and replay != 'n':
					replay = input('\n!!! Please enter y or n !!! ')
					replay = replay.lower()
		else:
			system('cls')
			self.print_grid()
			print('\nYou\'ve surrounded the robot and it cannot reach the\n' \
				  'destination point :(')


	def find_path(self, grid, row, col, cache):
		# Recursive function to find out if there is a possible path, from the origin point to the destination point,
		# avoiding the holes, and what it is.
		if row < 0 or col < 0 or not grid[row][col]:
			return False
		cell = (row, col)
		if cell in cache:
			return cache[cell]
		cache[cell] = (row == 0 and col == 0 or
					   self.find_path(grid, row, col - 1, cache) or
					   self.find_path(grid, row - 1, col, cache))
		if cache[cell]:
			self.path.append(cell)
		return cache[cell]


def int_num(num):
	# Function to disallow entries other than integers greater than 0.
	while True:
		try:
			num = int(num)
			if num > 0:
				break
			else:
				num = input('\n!!! Enter an integer greater than 0 !!! ')
		except ValueError:
			num = input('\n!!! Enter an integer greater than 0 !!! ')
	return num


def main():
	# Main function, which calls the Grid's methods.
	system('cls')
	print('*************************************************************\n' \
      	  '*****             Welcome to the ROBOT GAME             *****\n' \
      	  '*****          Developed by Wallacy Pasqualini          *****\n' \
      	  '*************************************************************\n\n' \
      	  '*************************************************************\n' \
      	  '*****              This is my first project             *****\n' \
      	  '*****              using recursive function             *****\n' \
      	  '*************************************************************\n\n' \
      	  '*************************************************************\n' \
      	  '*****              Hope you like! Enjoy it              *****\n' \
      	  '*************************************************************\n')
	print('Main menu:\n\n' \
		  '1 - Rules\n' \
		  '2 - Start game\n' \
		  '3 - Exit game\n')
	option = int_num(input('Enter an option: '))

	while option > 3:
		system('cls')
		print('*************************************************************\n' \
	      	  '*****             Welcome to the ROBOT GAME             *****\n' \
	      	  '*****          Developed by Wallacy Pasqualini          *****\n' \
	      	  '*************************************************************\n\n' \
	      	  '*************************************************************\n' \
	      	  '*****              This is my first project             *****\n' \
	      	  '*****              using recursive function             *****\n' \
	      	  '*************************************************************\n\n' \
	      	  '*************************************************************\n' \
	      	  '*****              Hope you like! Enjoy it              *****\n' \
	      	  '*************************************************************\n')
		print('Main menu:\n\n' \
			  '1 - Rules\n' \
			  '2 - Start game\n' \
			  '3 - Exit game\n')
		option = int_num(input('Please enter a valid option (1, 2 or 3): '))

	if option == 1:
		example = Grid(5, 5)
		system('cls')
		print('The game consists of creating a wall with holes:\n')
		print('5 high and 5 wide wall without holes:\n')
		example.print_grid()
		example.grid[0][3] = 0
		example.grid[1][0] = 0
		example.grid[1][1] = 0
		example.grid[1][4] = 0
		example.grid[2][3] = 0
		example.grid[4][2] = 0
		print('\n5 high and 5 wide wall with holes in the coordinates\n' \
			  '(1, 4), (2, 1), (2, 2), (2, 5), (3, 4) and (5, 3):\n')
		example.print_grid()
		input('\nPress enter to continue ')
		system('cls')
		print('After creating the wall and filling it with holes, the robot\n' \
			  'will try to find a path to move from the origin point (O.P)\n' \
			  'to the destination point (D.P), without going through\n' \
			  'the holes:\n')
		print('O.P   O   O   X    O\n' \
			  ' X    X   O   O    X\n' \
			  ' O    O   O   X    O\n' \
			  ' O    O   O   O    O\n' \
			  ' O    O   X   O   D.P\n')
		print('In the example, we\'ll have the following movement:\n')
		input('Press enter to continue ')
		example.move_robot()
		print('\nNote that the robot can only move down or to the right.\n' \
			  'Therefore, it\'s possible to block your path.\n' \
			  'For example, let\'s add a hole at coordinate (4, 4)\n')
		example.grid[3][3] = 0
		example.print_grid()
		print('\nAs there is no possible path, the system will return the following:\n')
		input('Press enter to continue ')
		example.move_robot()
		print('\nAnd that\'s all! Now let\'s play?\n')
		input('Press enter to continue ')
		del example
		main()


	elif option == 2:
		fixTheWall = 'y'
		while fixTheWall == 'y':
			system('cls')
			print('Let\'s create a wall for the robot to pass from the\n' \
				  'origin point to the destination point.\n')
			h = int_num(input('Enter the desired height for the wall: '))
			w = int_num(input('\nEnter the desired width for the wall: '))

			while h < 2 or w < 2:
				system('cls')
				print('Height and width must be greater than 1.\n\n' \
					  'Resetting the values...\n')
				print('Let\'s create a wall for the robot to pass from the\n' \
					  'origin point to the destination point.\n')
				h = int_num(input('Enter the desired height for the wall: '))
				w = int_num(input('\nEnter the desired width for the wall: '))

			base = Grid(h, w)
			system('cls')
			print('This is the wall you created:\n')
			base.print_grid()
			fixTheWall = input('\nDo you want to modify the wall? (y/n): ')
			fixTheWall = fixTheWall.lower()

			while fixTheWall != 'y' and fixTheWall != 'n':
				fixTheWall = input('\n!!! Please enter y or n !!! ')
				fixTheWall = fixTheWall.lower()

		base.holes()
		system('cls')
		print('The robot is checking which best path to go')
		for number in range(h):
			print('.')
			sleep(0.5)
		base.move_robot()
		restart = input('\nPlay again? (y/n): ')
		restart = restart.lower()

		while restart != 'y' and restart != 'n':
			restart = input('\n!!! Please enter y or n !!! ')
			restart = restart.lower()

		if restart == 'y':
			main()
		else:
			print('\n' \
				  'Thanks for visiting my game! See you later.')

	else:
		print('\n' \
			  'Thanks for visiting my game! See you later.')

if __name__ == '__main__':
	main()
