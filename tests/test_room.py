from unittest import TestCase
from app.models.room import Room
from app.models.office import Office
from app.models.living_space import LivingSpace
from app.models.person import Person

class RoomTests(TestCase):
    def setUp(self):
        self.name = 'orange'
        self.room_type = 'office'
        self.room = Room(self.name, self.room_type)
        self.office = Office(self.name)
        self.living_space = LivingSpace(self.name)

        self.person_list = []
        self.person_list.append(Person('john', 'FELLOW'))
        self.person_list.append(Person('peter', 'FELLOW'))
        self.person_list.append(Person('jackson', 'FELLOW'))
        self.person_list.append(Person('james', 'FELLOW'))
        self.person_list.append(Person('luck', 'FELLOW'))
        self.person_list.append(Person('william', 'FELLOW'))
        self.person_list.append(Person('kron', 'FELLOW'))

    def test_room_instance(self):
        self.assertIsInstance(self.room, Room, "Object room is not an instance of class Room")
    def test_room_attributes(self):
        self.assertEqual(self.room.name, self.name, "The value that is passed into name and that returned, do not match")
        self.assertEqual(self.room.room_type, self.room_type, "The value that is passed into room_type and that returned, do not match")
    def test_office_inherits_room(self):
        self.assertTrue(issubclass(Office, Room), "Office class doesnot inherit from the Room class")
    def test_office_is_an_instance_of_Office(self):
        self.assertIsInstance(self.office, Office, "Object office is not an instance of the Office class")
    def test_name_attribute_in_office(self):
        self.assertEqual(self.office.name, self.name, "The value that is passed into name for office object and that returned, do not match")
    def test_fixed_attributes_in_office(self):
        self.assertEqual(self.office.room_type, 'OFFICE', "Office doesnot contain any attribute type")
    def test_allocate_list_in_office(self):
        self.assertTrue(isinstance(self.office.allocation_list, list), "There is no list allocate_list in office")
    def test_allocate_list_values_in_office(self):
        x = 1
        for i in self.person_list:
            value = self.office.add_person(i)
            if x <= 6:
                self.assertTrue(value, "Person has not been added to room")
                self.assertEqual(self.office.get_allocate_len(), x, "The list length in office does not match")
            else:
                self.assertFalse(value, "Room is adding extra people")
                self.assertFalse(value)
            x += 1
    def test_check_office_allocatable(self):
        x = 0
        for i in self.person_list:
            value = self.office.is_room_assignable()
            if x < 6:
                self.assertTrue(value, "Office is meant to be allocatable at position "+str(x))
                self.office.add_person(i)
            else:
                self.assertFalse(value, "Office is not meant to be allocatable at position "+str(x))
                self.office.add_person(i)
            x += 1
    def test_living_space_inherits_room(self):
        self.assertTrue(issubclass(LivingSpace, Room), "LivingSpace class doesnot inherit from the Room class")
    def test_living_space_is_instance_of_LivingSpace(self):
        self.assertIsInstance(self.living_space, LivingSpace, "Object living_space is not an instance of class LivingSpace")
    def test_name_attribute_in_living_space(self):
        self.assertEqual(self.living_space.name, self.name, "The value that is passed into name for living_space object and that returned, do not match")
    def test_fixed_attributes_in_living_space(self):
        self.assertEqual(self.living_space.room_type, 'LIVINGSPACE', "LivingSpace doesnot contain any attribute type")
    def test_allocate_list_in_living_space(self):
        self.assertTrue(isinstance(self.living_space.allocation_list, list), "There is no list allocate_list in office")
    def test_allocate_list_values_in_living_space(self):
        x = 1
        for i in self.person_list:
            value = self.living_space.add_person(i)
            if x <= 4:
                self.assertTrue(value, "Person has not been added to room")
                self.assertEqual(self.living_space.get_allocate_len(), x, "The list length in living_space does not match")
            else:
                self.assertFalse(value, "Room is adding extra people")
            x += 1
    def test_check_living_space_allocatable(self):
        x = 0
        for i in self.person_list:
            value = self.living_space.is_room_assignable()
            if x < 4:
                self.assertTrue(value, "Living Space is meant to be allocatable at position "+str(x))
                self.living_space.add_person(i)
            else:
                self.assertFalse(value, "Living Space is not meant to be allocatable at position "+str(x))
                self.living_space.add_person(i)
            x += 1
    
    
    
