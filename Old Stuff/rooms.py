import yaml


room = open('rooms.yaml')
roomMap = yaml.load(room)
room.close()
print roomMap
print"----"
print roomMap['room1']
print "---"
print roomMap['room2']

