#Import Room Class
from app.models.room import Room
#Let LivingSpace inherit the Room Class
class LivingSpace(Room):
    #Initialise the attributes of the LivingSpace Class
    def __init__(self, name):
        self.allocation_list = []
        capacity = 4
        room_type = "LIVINGSPACE"
        #Make call to base class Room
        super(LivingSpace, self).__init__(name, room_type)
    def add_person(self, person):
        pass
    def get_allocate_len(self):
        pass