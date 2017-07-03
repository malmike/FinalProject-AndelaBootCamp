from unittest import TestCase
from app.controller.dojo import Dojo
from tests.general_computations import GeneralComputations

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
        self.assertTrue(isinstance(dojo.staff_dict, dict), "Class dojo doesnot contain any dictionary staff_dict")
        self.assertTrue(isinstance(dojo.fellow_dict, dict), "Class dojo doesnot contain any dictionary fellow_dict")


    #Test check for strings
    def test_check_str(self):
        dojo = Dojo()
        with self.assertRaises(TypeError):
            dojo.check_str(RoomType=1)

    #Test to get office dictonary when room type OFFICE is passed
    def test_get_office_dict_(self):
        dojo = Dojo()
        general_computations = GeneralComputations(dojo)
        general_computations.create_office_rooms(1)
        office_dict = dojo.get_dict("ROOM", "OFFICE")
        self.assertEqual(
            office_dict,
            dojo.office_dict,
            "Dictionary returned should be the same as the office_dict in dojo"
        )


    #Test to get living space dictonary when room type LIVINGSPACE is passed
    def test_get_living_space_dict_(self):
        dojo = Dojo()
        general_computations = GeneralComputations(dojo)
        general_computations.create_living_space_rooms(1)
        living_space_dict = dojo.get_dict("ROOM", "LIVINGSPACE")
        self.assertEqual(
            living_space_dict,
            dojo.living_space_dict,
            "Dictionary returned should be the same as the office_dict in dojo"
        )


    #Test to get staff dictonary when person type STAFF is passed
    def test_get_staff_dict_(self):
        dojo = Dojo()
        general_computations = GeneralComputations(dojo)
        general_computations.create_staff(1)
        staff_dict = dojo.get_dict("PERSON", "STAFF")
        self.assertEqual(
            staff_dict,
            dojo.staff_dict,
            "Dictionary returned should be the same as the sta in dojo"
        )


    #Test to get office dictonary when room type OFFICE is passed
    def test_get_fellow_dict_(self):
        dojo = Dojo()
        general_computations = GeneralComputations(dojo)
        general_computations.create_fellows(1)
        fellow_dict = dojo.get_dict("PERSON", "FELLOW")
        self.assertEqual(
            fellow_dict,
            dojo.fellow_dict,
            "Dictionary returned should be the same as the office_dict in dojo"
        )