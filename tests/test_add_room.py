from unittest import TestCase
from app.controller.dojo import Dojo
from app.models.living_space import LivingSpace
from app.models.office import Office

class AddRoomTests(TestCase):
    #Test that the Dojo can create an office and add it to the office dictionary
    def test_create_office(self):
        dojo = Dojo()
        initial_office_count = len(dojo.office_dict)
        blue_office = dojo.create_room('OFFICE', 'Blue')
        self.assertTrue(blue_office, "Room has not been created")
        new_office_count = len(dojo.office_dict)
        self.assertEqual(new_office_count - initial_office_count, 1, "Room office has not been created")
       
    #Check that no two offices can be created with the same name 
    def test_fail_repeated_office_creation(self):
        dojo = Dojo()
        initial_office_count = len(dojo.office_dict)
        blue_office = dojo.create_room('OFFICE', 'Blue')
        blue_office2 = dojo.create_room('OFFICE', 'Blue')
        self.assertFalse(blue_office2, "Check that the room creation method doesnot create repeated rooms")
        new_office_count = len(dojo.office_dict)
        self.assertEqual(
            new_office_count - initial_office_count, 1, 
            "Only the first room should be created and not the second"
        )

    #Test that the Dojo can create an living space and add it to the office dictionary
    def test_create_living_space(self):
        dojo = Dojo()
        initial_living_space_count = len(dojo.living_space_dict)
        blue_living_space = dojo.create_room('LIVINGSPACE', 'Blue')
        self.assertTrue(blue_living_space, "Room has not been created")
        new_living_space_count = len(dojo.living_space_dict)
        self.assertEqual(new_living_space_count - initial_living_space_count, 1, "There is an error in the room creation method")
       
    #Check that no two living space rooms can be created with the same name 
    def test_fail_repeated_office_creation(self):
        dojo = Dojo()
        initial_living_space_count = len(dojo.living_space_dict)
        blue_living_space = dojo.create_room('LIVINGSPACE', 'Blue')
        blue_living_space2 = dojo.create_room('LIVINGSPACE', 'Blue')
        self.assertFalse(blue_living_space2, "Check that the room creation method doesnot create repeated rooms")
        new_living_space_count = len(dojo.living_space_dict)
        self.assertEqual(
            new_living_space_count - initial_living_space_count, 1, 
            "Only the first room should be created and not the second"
        )
    