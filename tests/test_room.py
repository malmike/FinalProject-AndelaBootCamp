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
    def test_office_inherits_room(self):
        self.assertTrue(issubclass(Office, Room), "Office class doesnot inherit from the Room class")
    def test_office_is_an_instance_of_Office(self):
        self.assertIsInstance(self.office, Office, "Object office is not an instance of the Office class")
    def test_fixed_attributes_in_office(self):
        self.assertEqual(self.office.capacity, 6, "Office doesnot contain any attribute capacity")
        self.asserEqual(self.office.type, 'OFFICE', "Object doesnot contain any attribute type")
    
    
