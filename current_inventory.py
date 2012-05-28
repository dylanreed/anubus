def move():
	print "Which way?"
	choice = raw_input("> ")

	if choice == "south" and room == 'one':
		current_room.append('three')
		current_room.remove('one')
		return room_three()

	elif choice == "south" and room == 'two':
		current_room.remove('two')
		current_room.append('four')
		return room_four()
		
	elif choice == "east" and room == 'one':
		current_room.remove('one')
		current_room.append('two')
		return room_two()

	elif choice == "east" and room == 'three':
		current_room.remove('three')
		current_room.append('four')
		return room_four()

	elif choice == "north" and room == 'three':
		current_room.remove('three')
		current_room.append('one')
		return room_one()

	elif choice == "north" and room == 'four':
		current_room.remove('four')
		current_room.append('two')
		return room_two()

	elif choice == "west" and room == 'four':
		current_room.remove('four')
		current_room.append('three')
		return room_three()

	elif choice == "west" and room == 'two':
		current_room.remove('two')
		current_room.append('one')
		return room_one()

	else:
		print room
		print "Can't go", choice,"here."
		control()