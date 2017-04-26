#Import Room Class
from app.models.room import Room
#Let LivingSpace inherit the Room Class
class LivingSpace(Room):
    #Initialise the attributes of the LivingSpace Class
    def __init__(self, name):
        self.allocation_list = []
        self.capacity = 4
        room_type = "LIVINGSPACE"
        #Make call to base class Room
        super(LivingSpace, self).__init__(name, room_type)
    def add_person(self, person):
        if len(self.allocation_list) < self.capacity:
            self.allocation_list.append(person)
            return True
        else:
            return False
    def get_allocate_len(self):
        return len(self.allocation_list)
    def room_assignable(self):
        if len(self.allocation_list) < self.capacity:
            return True
        else:
            return False
    def is_room_assignable(self):
        if len(self.allocation_list) < self.capacity:
            return True
        else:
            return False