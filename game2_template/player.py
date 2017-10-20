from items import *
from map import rooms

inventory = [item_id, item_laptop, item_money]

def calculatenewmass(items, newitem):
	totalmass = 0
	for item in items:
		totalmass = float(totalmass) + float(item["mass"])
		newtotalmass = float(totalmass) + float(newitem)
	return newtotalmass

# Start game at the reception
current_room = rooms["Reception"]
