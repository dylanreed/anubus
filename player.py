from sys import exit
from inventory import *

def player():
	print "What would you like to do?"
	player_choice = raw_input("> ").lower()

	if player_choice in ['i','inventory']:
		print"inventory?"
		inventory()
		player()
	elif player_choice in ['m','move']:
		print "move"
		player()
	elif player_choice in ['e','exit']:
		print "good bye"
		exit(1)
	else:
		print "what?"
		player()

