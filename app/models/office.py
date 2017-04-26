#Import Room Class
from app.models.room import Room
#Let Office Inherit the Room Class
class Office(Room):
    #Initialise the attributes of the Office Class  
    capacity = 6
    room_type = "OFFICE"
