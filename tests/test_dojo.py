from unittest import TestCase
from app.controller.dojo import Dojo
from app.models.living_space import LivingSpace
from app.models.office import Office
from app.models.fellow import Fellow
from app.models.staff import Staff

class DojoTests(TestCase):
    
    #Set up the various class variables to be used during computation
    def setUp(self):
        self.living_space_rooms_names = ['la', 'lb', 'lc', 'ld', 'le', 'lf', 'lg', 'lh','li','lj','lk','ll','lm','ln','lo']
        self.office_rooms_names = ['oz', 'oy', 'ox', 'ow', 'ov']
        self.fellows_names = [
            'fa','fb','fc','fd','fe','ff','fg','fh','fi','fj',
            'fk','fl','fm','fn','fo','fp','fq','fr','fs','ft',
            'fu','fv','fw','fx','fy','fz'
            ]
        self.staff_names = [
            'sa','sb','sc','sd','se','sf','sg','sh','si','sj',
            'sk','sl','sm','sn','so','sp','sq','sr','ss','st',
            'su','sv','sw','sx','sy','sz'
            ]
        #Create classes for living space
        self.living_space_rooms = [LivingSpace(x) for x in self.living_space_rooms_names]
        self.office_rooms = [Office(x) for x in self.office_rooms_names]
        self.list_fellows = [Fellow(x) for x in self.fellows_names]
        self.list_staffs = [Staff(x) for x in self.staff_names]

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


    #Test room allocation
    def test_allocate_living_space_and_office(self):
        dojo = Dojo()
        self.create_multiple_rooms(dojo, 'OFFICE')
        self.assertEqual(
            len(dojo.office_dict), 
            len(self.office_rooms_names), 
            "Why were not all rooms created? Verify your create room method and the test"
            )
        self.create_multiple_rooms(dojo, 'LIVINGSPACE')
        self.assertEqual(
            len(dojo.living_space_dict), 
            len(self.living_space_rooms_names), 
            "Why were not all rooms created? Verify your create room method and the test"
            )
        self.add_multiple_people(dojo, 'FELLOW')
        self.room_allocation(dojo, 'FELLOW')
        for item in dojo.allocated_living_space:
            self.assertEqual(
                len(item.allocation_list), 
                len(dojo.living_space_dict[item.name].allocation_list), 
                "Values in the living space dictionary do not match those in the allocated living space list"
                )
        for item in dojo.unallocated_living_space:
            self.assertEqual(
                len(item.allocation_list), 
                len(dojo.living_space_dict[item.name].allocation_list), 
                "Values in the living space dictionary do not match those in the unallocated living space list"
                )
        for item in dojo.allocated_offices:
            self.assertEqual(
                len(item.allocation_list), 
                len(dojo.office_dict[item.name].allocation_list), 
                "Values in the office dictionary do not match those in the allocated office list"
                )
        for item in dojo.unallocated_offices:
            self.assertEqual(
                len(item.allocation_list), 
                len(dojo.office_dict[item.name].allocation_list), 
                "Values in the office dictionary do not match those in the unallocated office list"
                )
        
        
    """
    The functions below are used for computation purposes by the testing function
    They are functions that are repeated across multiple test functions
    """
    
    #Create multiple rooms 
    def create_multiple_rooms(self, dojo, room_type):
        room_list = []
        if room_type is 'LIVINGSPACE':
            initial_living_space_list_length = len(dojo.living_space_dict) 
            self.create_rooms(dojo, room_type, self.living_space_rooms_names)
            self.assertEqual(
                len(self.living_space_rooms_names), 
                len(dojo.living_space_dict)-initial_living_space_list_length, 
                "Rooms added to the living space list do not match the number inserted"
                )
        elif room_type is 'OFFICE':
            initial_office_list_length = len(dojo.office_dict)
            self.create_rooms(dojo, room_type, self.office_rooms_names)
            self.assertEqual(
                len(self.office_rooms_names), 
                len(dojo.office_dict)-initial_office_list_length, 
                "Rooms added to the office list do not match the number inserted"
                )
        else:
            raise ValueError('The value entered is unknown')
        
    def create_rooms(self, dojo, room_type, room_list):
        for item in room_list:
            dojo.create_room(room_type, item)

    #Add multiple people
    def add_multiple_people(self, dojo, person_type):
        people_list = []
        if person_type is 'STAFF':
            initial_staff_list_length = len(dojo.staff_dict)
            self.add_people(dojo, person_type, self.staff_names)
            self.assertEqual(
                len(self.staff_names), 
                len(dojo.staff_dict)-initial_staff_list_length, 
                "People added to the staff list do not match the number inserted"
                )
        elif person_type is 'FELLOW':
            initial_fellow_list_length = len(dojo.fellow_dict)
            self.add_people(dojo, person_type, self.fellows_names)
            self.assertEqual(
                len(self.fellows_names), 
                len(dojo.fellow_dict)-initial_fellow_list_length, 
                "People added to the fellow list do not match the number inserted"
                )
        else:
            raise ValueError('The value entered is unknown')
    
    def add_people(self, dojo, person_type, people_list):
        for person_name in people_list:
            dojo.add_person(person_type, person_name)
            

    #Insert test values into the living_space rooms in the dojo dictionary living_space_dict
    def assign_living_space(self, dojo):
        person_index = 0
        test_index = ""
        count = 0
        for item in dojo.living_space_dict: 
            while True:
                if person_index <= 25:
                    if dojo.living_space_dict[item].is_room_assignable():
                        dojo.living_space_dict[item].add_person(self.list_fellows[person_index])
                        person_index += 1
                    else:
                        self.assertEqual(4, dojo.living_space_dict[item].get_allocate_len(), "Maximum number of people assigned to living space does not match returned number")
                        test_index = item
                        count += 1
                        break 
                else:
                    break
            if person_index == 26:
                break
        #Tests that verify that the living space room has properly been allocated
        self.assertEqual(count, 6, "The expected number should be 6")
        self.assertEqual(len(dojo.living_space_dict)-count, 9, "The expected number of unallocated rooms should be 9")
        self.assertEqual(4, dojo.living_space_dict[test_index].get_allocate_len(), "Value held by the living space dictionary has not been updated")
        return count

    #Insert test values into the living_space rooms in the dojo dictionary living_space_dict
    def assign_office(self, dojo, person_type):
        person_index = 0
        test_index = ""
        count = 0
        for item in dojo.office_dict: 
            while True:
                if person_index <= 25:
                    if dojo.office_dict[item].is_room_assignable():
                        dojo.office_dict[item].add_person(self.list_fellows[person_index])
                        person_index += 1
                    else:
                        self.assertEqual(6, dojo.office_dict[item].get_allocate_len(), "Maximum number of people assigned to living space does not match returned number")
                        test_index = item
                        count += 1
                        break 
                else:
                    break
            if person_index == 26:
                break
        #Tests that verify that the living space room has properly been allocated
        self.assertEqual(count, 4, "The expected number should be 6")
        self.assertEqual(len(dojo.office_dict)-count, 1, "The expected number of unallocated rooms should be 9")
        self.assertEqual(6, dojo.office_dict[test_index].get_allocate_len(), "Value held by the living space dictionary has not been updated")
        return count

    #Room allocation
    def room_allocation(self, dojo, person_type):
        if person_type is 'FELLOW':
            for item in dojo.fellow_dict:
                value = dojo.allocate_rooms(dojo.fellow_dict[item], "OFFICE")
                self.assertTrue(value, "Fellow value has failed to be allocated an office")
                value2 = dojo.allocate_rooms(dojo.fellow_dict[item], "LIVINGSPACE")
                self.assertTrue(value2, "Fellow value has failed to be allocated living space")
        elif person_type is 'STAFF':
            for item in dojo.staff_dict:
                value = dojo.allocate_rooms(dojo.staff_dict[item], "OFFICE")
                self.assertTrue(value, "Staff value has failed to be allocated an office")
        else:
            raise ValueError("The value entered for person type is unknown.")