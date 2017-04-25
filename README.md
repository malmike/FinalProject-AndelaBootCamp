# FinalProject-AndelaBootCamp
This is the repository for the final project of the Andela Boot Camp

PROJECT DESCRIPTION
When a new Fellow joins Andela they are assigned an office space and an optional living space if they choose to opt in. When a new Staff joins they are assigned an office space only. In this exercise you will be required to digitize and randomize a room allocation system for one of Andela Kenya’s facilities called The Dojo.

CONSTRAINTS
The Dojo has rooms, which can be offices or living spaces. An office can accommodate a maximum of 6 people. A living space can accommodate a maximum of 4 people.

A person to be allocated could be a fellow or staff. Staff cannot be allocated living spaces. Fellows have a choice to choose a living space or not.

This system will be used to automatically allocate spaces to people at random.

**Capitalised attributes are fixed attributes in the class
**Small lettered attributes are the ones passed into the class during initiation

CLASSES
Person attributes(name, position) 
Fellow constraint(inherit Person) attributes(POSITION) 
Staff constraint(inherit Person) attributes(name, position) 

Room attributes(name, type, capacity) 
Office constraint(inherit Room) attributes(name, TYPE, CAPACITY)
LivingSpace constraint(inherit Room) attributes(name, TYPE, CAPACITY)

Dojo attributes(number_of_rooms, rooms: Room) methods(createRoom(room_type, room_name):list, getRooms():list, getNumberOfRooms():int)





