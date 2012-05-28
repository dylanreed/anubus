
knife = False
gun = False
mask = False
ninja = False	

def add():
	item = raw_input("What do you want to add? ")
	#inventory items
	possible_items = ['knife', 'gun', 'mask', 'ninja']
	#in inventory
	

	print knife, gun, mask, ninja

	if item == "knife" in possible_items:
		knife = True
		print "Knife added."
		print knife
		add()

	else:
		print "I don't know what that is."
		add()



#def use(item):
	#item = raw_input("Use what? ")
	#if item in possible_items and == knife:
		#print "STAB!!"				
	#else:
		#print "nope!"

#use('item')
add()
#use('item')



