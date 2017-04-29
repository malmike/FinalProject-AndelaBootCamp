#Import Room Class
from app.models.room import Room
#Let LivingSpace inherit the Room Class
class LivingSpace(Room):
    #Initialise the attributes of the LivingSpace Class
    capacity = 4
    room_type = "LIVINGSPACE"