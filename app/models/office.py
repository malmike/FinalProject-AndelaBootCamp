from app.models.room import Room
class Office(Room):
    def __init__(self, name):
        capacity = 6
        room_type = "OFFICE"
        super(Office, self).__init__(name, capacity, room_type)