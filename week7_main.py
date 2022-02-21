import sys

if __name__ == "__main__":
	print('You called me from the command line, with arguments:')
	for argument in sys.argv: # This is the list of arguments
		print(argument)
else:
	print('This file was imported as a module!  __name__ is', __name__)
