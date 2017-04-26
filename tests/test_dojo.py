from unittest import TestCase
from app.controller.dojo import Dojo

class DojoTests(TestCase):
    def setUp(self):
        self.dojo = Dojo()
    def test_dojo_is_instance_of_Dojo(self):
        self.assertIsInstance(self.dojo, Dojo, "Object dojo is not an instance of class Dojo")
    def test_dojo_has_dict_of_rooms(self):
        self.assertTrue(isinstance(self.room_dict,dict), "Class dojo doesnot contain any dictionary room_dict")
    def test_dojo_has_dict_of_people(self):
        self.assertTrue(isinstance(self.people_dict, dict), "Class dojo doesnot contain any dictionary people_dict")
    