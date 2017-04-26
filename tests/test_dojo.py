from unittest import TestCase
from app.controller.dojo import Dojo

class DojoTests(TestCase):
    def setUp(self):
        self.dojo = Dojo()
    def test_dojo_is_instance_of_Dojo(self):
        self.assertIsInstance(self.dojo, Dojo, "Object dojo is not an instance of class Dojo")
    def test_dojo_has_dict_of_rooms(self):
        self.assertTrue(isinstance(self.dojo.room_dict,dict), "Class dojo doesnot contain any dictionary room_dict")
    def test_dojo_has_dict_of_people(self):
        self.assertTrue(isinstance(self.dojo.people_dict, dict), "Class dojo doesnot contain any dictionary people_dict")
    def test_create_room_successfully(self):
        initial_room_count = len(self.dojo.room_dict)
        blue_office = self.dojo.create_room('Blue', 'office')
        self.assertTrue(blue_office)
        new_room_count = len(self.dojo.room_dict)
        self.assertEqual(new_room_count - initial_room_count, 1)

    