#Import Room Class
from app.models.room import Room
#Let Office Inherit the Room Class
class Office(Room):
    #Initialise the attributes of the Office Class
    def __init__(self, name):
        self.allocation_list = []
        capacity = 6
        room_type = "OFFICE"
        #Make call to the base class Room
        super(Office, self).__init__(name, room_type)