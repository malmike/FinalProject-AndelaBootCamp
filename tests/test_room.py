from unittest import TestCase

class RoomTests(TestCase):
    def setUp(self):
        self.name = 'orange'
        self.capacity = 4
        self.room_type = 'office'
        self.room = Room(self.name, self.capacity, self.room_type)
        self.office = Office(self.name)
        self.living_space = LinvingSpace(self.name)
    def test_room_instance(self):
        self.assertIsInstance(self.room, Room, "Object room is not an instance of class Room")
    def test_room_attributes(self):
        self.assertEqual(self.room.name, self.name, "The value that is passed into name and that returned, do not match")
        self.assertEqual(self.room.capacity, self.capacity, "The value that is passed into capacity and that returned, do not match")
        self.assertEqual(self.room.room_type, self.room_type, "The value that is passed into room_type and that returned, do not match")
   
