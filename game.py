from sys import exit
from rooms import *

class game:
	@staticmethod
	def start():
		player.controls()
	def end():
		print "Better luck next time!!"
		exit(0)

#player system
class player:
	
	
	@staticmethod
	def controls():
		print "What would you like to do?"
		player_choice = raw_input("> ").lower()

		if player_choice in ['i','inventory']:
			inventory_sys.inventory()
			player.controls()
		elif player_choice in ['m','move']:
			movement_sys.move()
			player.controls()
		elif player_choice in ['e','exit']:
			print "good bye"
			exit(1)
		else:
			print "what?"
			player.controls()
	@staticmethod
	def death():
		print "you died"
		restart = raw_input("again? (y/n): ")
		if restart == 'y':
			game.start()
		else:
			game.end

# inventory system
class inventory_sys:
	# all possible items
	master_inventory =['mask', 'knife', 'gun', 'cross', 'ninja']
	current_inventory = []
	def __init__():
		print "let's go"

	#inventory commands
	@staticmethod
	def inventory_list():
		print inventory_sys.current_inventory

	@staticmethod
	def grab():
		item = raw_input("Grab what?> ").lower()
		if item in inventory_sys.master_inventory:	
			inventory_sys.current_inventory.append(item)
			print item, "added."
		else:
			print item, "dosen't exist."

	@staticmethod
	def drop():
		item = raw_input("Drop what?> ").lower()
		if item in inventory_sys.current_inventory:
			inventory_sys.current_inventory.remove(item)
			print item, "removed"
		elif item not in inventory_sys.current_inventory:
			print "You do not have that item."
		else:
			print item, "dosen't exist."

	@staticmethod
	def use():
		item = raw_input("Use what?> ").lower()
		if item in inventory_sys.current_inventory and item == "gun":
			gun()
		elif item in inventory_sys.current_inventory and item == "knife":
			knife()
		elif item in inventory_sys.current_inventory and item == "cross":
			cross()
		else:
			print "You don't have", item
			inventory()

	# Items
	@staticmethod
	def gun():
		print "Bang!"
		inventory()

	@staticmethod
	def knife():
		print "stab"
		inventory()

	@staticmethod
	def cross():
		print "Jesus"
		inventory()

	#inventorys	
	@staticmethod	
	def inventory():
		print "Welcome to your inventory."
		print "What would you like to do?"
		choice = raw_input("> ")

		if choice == "list":
			inventory_sys.inventory_list()
			inventory_sys.inventory()
		elif choice == "grab":
			inventory_sys.grab()
			player()
		elif choice == "drop":
			inventory_sys.drop()
			player()
		elif choice == "use":
			inventory_sys.use()
			player()
		elif choice == "exit":
			player.controls()
		else:
			print "What?"
			inventory_sys.inventory()

#movement system
class movement_sys:
	@staticmethod
	def move():
		print "You are in",map.current_room
		print "Which way?", map.exits
		direction = raw_input("> ")
		if direction == "north":
			movement_sys.north()
		elif direction == "south":
			movement_sys.south()
		elif direction == "west":
			movement_sys.west()
		elif direction == "east":
			movement_sys.east()
		else:
			print "What?"
			player.controls()
	@staticmethod
	def north():
		print "moving north"
		player.controls()
	@staticmethod
	def south():
		print "moving south"
		player.controls()
	@staticmethod
	def west():
		print "moving west"
		player.controls()
	@staticmethod
	def east():
		player.controls()
		print "moving east"

#rooms
class map:
	exits = ['north','south','east','west']
	current_room = ['room1']
	@staticmethod
	def room():
		if current_room == room1:
			map.exits.remove('north','south','east','west')
			map.exits.append('north','south','east','west')
		elif current_room == room2:
			map.exits.remove('north','south','east','west')
			map.exits.append('south')
		elif current_room == room3:
			map.exits.remove('north','south','east','west')
			map.exits.append('east')
		elif current_room == room4:
			map.exits.remove('north','south','east','west')
			map.exits.append('north')
		elif cuRRent_room == room5:
			map.exits.remove('north','south','east','west')
			map.exits.append('west')

	


	#def encounter():

	#def items():


		

		

	

game.start()












