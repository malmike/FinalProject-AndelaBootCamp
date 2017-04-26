from unittest import TestCase
from app.controller.dojo import Dojo

class DojoTests(TestCase):
    def setUp(self):
        self.dojo = Dojo()
    def test_dojo_is_instance_of_Dojo(self):
        self.assertIsInstance(self.dojo, Dojo, "Object dojo is not an instance of class Dojo")
    def test_dojo_has_dict_of_rooms(self):
        self.assertTrue(isinstance(self.dojo.living_space_dict,dict), "Class dojo doesnot contain any dictionary living_space_dict")
        self.assertTrue(isinstance(self.dojo.office_dict,dict), "Class dojo doesnot contain any dictionary office_dict")
    def test_dojo_has_dict_of_people(self):
        self.assertTrue(isinstance(self.dojo.people_dict, dict), "Class dojo doesnot contain any dictionary people_dict")
    def test_add_room_and_repeated_room(self):
        #Check whether one office room can be created
        initial_office_count = len(self.dojo.office_dict)
        blue_office = self.dojo.add_room('Blue', 'office')
        self.assertTrue(blue_office, "Room has not been created")
        new_office_count = len(self.dojo.office_dict)
        self.assertEqual(new_office_count - initial_office_count, 1, "Multiple values are being added to the office dictionary. Why is that!!!")
        #Check whether the same office room can be created
        initial_office_count = len(self.dojo.office_dict)
        blue_office2 = self.dojo.add_room('Blue', 'office')
        self.assertFalse(blue_office2, "Repeated room being created")
        new_office_count = len(self.dojo.office_dict)
        self.assertEqual(new_office_count - initial_office_count, 0, "The value is being added to the office dictionary when it should not")

        #Check whether one living space room can be created
        initial_room_count = len(self.dojo.living_space_dict)
        blue_living_space = self.dojo.add_room('Blue', 'living_space')
        self.assertTrue(blue_living_space, "Room has not been created")
        new_room_count = len(self.dojo.living_space_dict)
        self.assertEqual(new_room_count - initial_room_count, 1, "Multiple values are being added to the living space dictionary. Why is that!!!")
        #Check whether the same living space room can be created
        initial_room_count = len(self.dojo.living_space_dict)
        blue_living_space2 = self.dojo.add_room('Blue', 'living_space')
        self.assertFalse(blue_living_space2, "Repeated room being created")
        new_room_count = len(self.dojo.office_dict)
        self.assertEqual(new_room_count - initial_room_count, 0, "The value is being added to the living space dictionary when it should not")

    # def test_create_room_successfully(self):
    #     initial_room_count = len(self.dojo.office_dict)
    #     blue_office = self.dojo.create_room('Blue', 'office')
    #     self.assertTrue(blue_office)
    #     new_room_count = len(self.dojo.office_dict)
    #     self.assertEqual(new_room_count - initial_room_count, 1, "Multiple values are being added to the dictionary. Why is that!!!")
    
    