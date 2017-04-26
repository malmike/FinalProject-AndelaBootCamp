#Import Room Class
from app.models.room import Room
#Let Office Inherit the Room Class
class Office(Room):
    #Initialise the attributes of the Office Class
    def __init__(self, name):
        self.allocation_list = []
        self.capacity = 6
        room_type = "OFFICE"
        #Make call to the base class Room
        super(Office, self).__init__(name, room_type)
    def add_person(self, person):
        if len(self.allocation_list) < self.capacity:
            self.allocation_list.append(person)
            return True
        else:
            return False
    def get_allocate_len(self):
        return len(self.allocation_list)
    def is_room_assignable(self):
        if len(self.allocation_list) < self.capacity or not self.allocation_list:
            return True
        else:
            return False