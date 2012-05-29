import random

def attack():
	defense = random.randint(1,10)
	print defense
	attack_number = raw_input("Attack number? ")
	if attack_number == defense:
		print "hit"
	else:
		print 'miss'
		attack()

attack()