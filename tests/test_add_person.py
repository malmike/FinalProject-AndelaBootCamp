from unittest import TestCase
from app.controller.dojo import Dojo
from app.models.fellow import Fellow
from app.models.staff import Staff

class AddPersonTests(TestCase):
    

    #Test that a fellow can be created and added to the fellow dictionary
    def test_add_fellow(self):
        dojo = Dojo()
        initial_fellow_count = len(dojo.fellow_dict)
        test_fellow = dojo.add_person('FELLOW', 'Male Michael')
        self.assertTrue(test_fellow, "Fellow has not been created")
        new_fellow_count = len(dojo.fellow_dict)

        self.assertEqual(
            new_fellow_count - initial_fellow_count, 
            1, 
            "Only a single fellow object should have been added to the fellow dictionary"
            )
    

    #Check whether the same fellow can be created
    def test_fail_creation_of_repeated_fellow(self):
        dojo = Dojo()
        initial_fellow_count = len(dojo.fellow_dict)
        test_fellow = dojo.add_person('FELLOW', 'Male Michael')
        test_fellow_2 = dojo.add_person('FELLOW', 'Male Michael')
        self.assertFalse(test_fellow_2, "Repeated fellow should not be created")

        new_fellow_count = len(dojo.fellow_dict)
        self.assertEqual(
            new_fellow_count - initial_fellow_count, 
            1, 
            "Check that there are no repeated fellows created"
            )
    
    
    #Test that a fellow can be created and added to the fellow dictionary
    def test_add_staff(self):
        dojo = Dojo()
        initial_staff_count = len(dojo.staff_dict)
        test_staff = dojo.add_person('STAFF', 'John Wink')
        self.assertTrue(test_staff, "Staff has not been created")
        new_staff_count = len(dojo.staff_dict)

        self.assertEqual(
            new_staff_count - initial_staff_count, 
            1, 
            "Only a single staff should have been added to the staff dictionary"
            )
    

    #Check whether the same staff can be created
    def test_fail_creation_of_repeated_staff(self):
        dojo = Dojo()
        initial_staff_count = len(dojo.staff_dict)
        test_staff = dojo.add_person('STAFF', 'John Wink')
        test_staff_2 = dojo.add_person('STAFF', 'John Wink')
        self.assertFalse(test_staff_2, "Repeated staff should not be created")

        new_staff_count = len(dojo.staff_dict)
        self.assertEqual(
            new_staff_count - initial_staff_count, 
            1, 
            "Check that there are no repeated staff created"
            )