from sys import exit
from player import *

def game():
	print "Welcome to the EAS Anubus"
	print "Prepare to die!!"
	print "Ready? (y/n)"
	ready = raw_input("> ").lower()
	if ready == "y":	
		player()
	else:
		exit(1)

game()
