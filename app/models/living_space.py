from app.models.room import Room
class LivingSpace(Room):
    def __init__(self, name):
        capacity = 4
        room_type = "LIVINGSPACE"
        super(LivingSpace, self).__init__(name, capacity, room_type)