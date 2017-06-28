from unittest import TestCase
from app.controller.dojo import Dojo
from app.models.living_space import LivingSpace
from app.models.office import Office
from app.models.fellow import Fellow
from app.models.staff import Staff

class DojoTests(TestCase):
    

    #Test that when the class Dojo is instantiated, the object that is created is an instance of the Dojo class
    def test_dojo_is_instance_of_Dojo(self):
        dojo = Dojo()
        self.assertIsInstance(dojo, Dojo, "Object dojo is not an instance of class Dojo")


    #Test that the Dojo class has a dictionary for living space and one for office space
    def test_dojo_has_dict_of_rooms(self):
        dojo = Dojo()
        self.assertTrue(isinstance(dojo.living_space_dict,dict), "Class dojo doesnot contain any dictionary living_space_dict")
        self.assertTrue(isinstance(dojo.office_dict,dict), "Class dojo doesnot contain any dictionary office_dict")


    #Test that the Dojo class a dictionary of all people
    def test_dojo_has_dict_of_people(self):
        dojo = Dojo()
        self.assertTrue(isinstance(dojo.people_dict, dict), "Class dojo doesnot contain any dictionary people_dict")


    
    