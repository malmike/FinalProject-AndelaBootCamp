from unittest import TestCase
from app.controller.dojo import Dojo
from app.models.fellow import Fellow
from app.models.staff import Staff
from app.models.living_space import LivingSpace
from app.models.office import Office
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
    def test_get_office_dict(self):
        dojo = Dojo()
        general_computations = GeneralComputations(dojo)
        general_computations.create_office_rooms(1)
        office_dict = dojo.get_dict("OFFICE")
        self.assertEqual(
            office_dict,
            dojo.office_dict,
            "Dictionary returned should be the same as the office_dict in dojo"
        )


    #Test to get living space dictonary when room type LIVINGSPACE is passed
    def test_get_living_space_dict(self):
        dojo = Dojo()
        general_computations = GeneralComputations(dojo)
        general_computations.create_living_space_rooms(1)
        living_space_dict = dojo.get_dict("LIVINGSPACE")
        self.assertEqual(
            living_space_dict,
            dojo.living_space_dict,
            "Dictionary returned should be the same as the office_dict in dojo"
        )


    #Test to get staff dictonary when person type STAFF is passed
    def test_get_staff_dict(self):
        dojo = Dojo()
        general_computations = GeneralComputations(dojo)
        general_computations.create_staff(1)
        staff_dict = dojo.get_dict("STAFF")
        self.assertEqual(
            staff_dict,
            dojo.staff_dict,
            "Dictionary returned should be the same as the sta in dojo"
        )


    #Test to get office dictonary when room type OFFICE is passed
    def test_get_fellow_dict(self):
        dojo = Dojo()
        general_computations = GeneralComputations(dojo)
        general_computations.create_fellows(1)
        fellow_dict = dojo.get_dict("FELLOW")
        self.assertEqual(
            fellow_dict,
            dojo.fellow_dict,
            "Dictionary returned should be the same as the office_dict in dojo"
        )


    #Test for the creation of office object
    def test_create_office_object(self):
        dojo = Dojo()
        office_object = dojo.create_item_object("OFFICE", 'office')
        self.assertIsInstance(office_object, Office, "An office object should be returned")


    #Test for the creation of living space object
    def test_create_living_space_object(self):
        dojo = Dojo()
        living_space_object = dojo.create_item_object("LIVINGSPACE", 'livingspace')
        self.assertIsInstance(living_space_object, LivingSpace, "A livingspace object should be returned")


    #Test for the creation of office object
    def test_create_fellow_object(self):
        dojo = Dojo()
        fellow_object = dojo.create_item_object("FELLOW", 'fellow')
        self.assertIsInstance(fellow_object, Fellow, "A fellow object should be returned")


    #Test for the creation of office object
    def test_create_staff_object(self):
        dojo = Dojo()
        staff_object = dojo.create_item_object("STAFF", 'staff')
        self.assertIsInstance(staff_object, Staff, "A staff object should be returned")

    #Test for adding return item object when added
    def test_add_object_return_object(self):
        dojo = Dojo()
        fellow_dict = dojo.fellow_dict
        fellow_object = dojo.add_object_to_dict(fellow_dict, "FELLOW", 'Male Michael')
        self.assertIsInstance(fellow_object, Fellow)

    #Test for checking that the item object is added to item dict
    def test_add_object_to_item_dict(self):
        dojo = Dojo()
        dict_len = len(dojo.office_dict)
        dojo.add_object_to_dict(dojo.office_dict, "OFFICE", 'Red')
        new_dict_len = len(dojo.office_dict)
        self.assertEqual(
            new_dict_len - dict_len,
            1,
            "Item was not added to the item dict, Check the add_object_to_dict method"
        )