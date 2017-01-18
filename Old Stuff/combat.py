import random

class combat:
	armor = random.randint(1,10)
	

	def attack():
		attack_number = input("Attack number? ")
		if attack_number == armor:
			print "hit"
			combat.attack()
		else:
			print 'miss'
			combat.attack()

combat.attack()