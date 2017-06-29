from unittest import TestCase
from app.controller.dojo import Dojo
from tests.general_computations import GeneralComputations

class AllocationsTests(TestCase):


    #Set up the various class variables to be used during during tests
    def setUp(self):
        self.dojo = Dojo()

    
    #Test the method for assigning the sample offices
    def test_assign_sample_offices(self):
        self.dojo = Dojo()
        general_computations = GeneralComputations(self.dojo)
        number_of_assigned_offices = general_computations.assign_sample_offices('STAFF', 10, 25)["count"]
        self.assertEqual(4,number_of_assigned_offices, "Rooms assigned in the test method do not match the expected number")

    
    #Test the method for assigning the sample living space
    def test_assign_sample_living_space(self):
        self.dojo = Dojo()
        general_computations = GeneralComputations(self.dojo)
        number_of_assigned_living_space = general_computations.assign_sample_living_space(10, 25)["count"]
        self.assertEqual(6, number_of_assigned_living_space, "Rooms assigned in the test method do not match the expected number")


    #Test to check for people assigned to a room 
    def test_print_office(self):
        self.dojo = Dojo()
        general_computations = GeneralComputations(self.dojo)
        office_allocations = general_computations.assign_sample_offices('STAFF', 3, 24)["room_assignment"]
        office_allocation_list = office_allocations[general_computations.office_rooms_names[2]]
        assigned_staff_list = general_computations.dojo.room_occupants(general_computations.office_rooms_names[2])
        self.assertEqual(office_allocation_list, assigned_staff_list, 'List doesnot match')


    #Test to check all room allocations
    def test_print_allocations(self):
        self.dojo = Dojo()
        general_computations = GeneralComputations(self.dojo)
        office_allocations = general_computations.assign_sample_offices('STAFF', 3, 24)["room_assignment"]
        living_space_allocations = general_computations.assign_sample_living_space(3, 24)["room_assignment"]
        assigned_allocations = self.dojo.get_allocations()
        expected_allocations_list = living_space_allocations
        expected_allocations_list.update(office_allocations)
        self.assertEqual(len(expected_allocations_list), len(assigned_allocations), 'List doesnot match')


    #Test to check offices that still have unassigned places
    def test_get_unallocated_offices(self):
        self.dojo = Dojo()
        general_computations = GeneralComputations(self.dojo)
        room_number = 20
        staff_number = 26
        office_allocations_count = general_computations.assign_sample_offices('STAFF', room_number, staff_number)["count"]
        unallocated_offices = self.dojo.get_unallocated_rooms('OFFICE')
        self.assertIsInstance(unallocated_offices, list, 'A list should be returned if they are still unallocated offices')
        self.assertEqual(
            len(unallocated_offices), 
            room_number-office_allocations_count, 
            'Unallocated rooms doesnot match the expected number'
        )

    
    #Test to check living spaces that still have unassigned places
    def test_get_unallocated_living_spaces(self):
        self.dojo = Dojo()
        general_computations = GeneralComputations(self.dojo)
        room_number = 10
        fellow_number = 26
        living_space_allocation_count = general_computations.assign_sample_living_space( room_number, fellow_number)["count"]
        unallocated_living_spaces = self.dojo.get_unallocated_rooms('LIVINGSPACE')
        self.assertIsInstance(unallocated_living_spaces, list, 'A list should be returned if they are still unallocated living spaces')
        self.assertEqual(
            len(unallocated_living_spaces), 
            room_number-living_space_allocation_count, 
            'Unallocated rooms doesnot match the expected number'
        )


    #Test office allocation
    def test_office_allocation(self):
        self.dojo = Dojo()
        general_computations = GeneralComputations(self.dojo)
        room_number = 10
        staff_number = 1
        general_computations.create_office_rooms(room_number)
        general_computations.create_staff(staff_number)
        room_allocated = general_computations.room_allocation(self.dojo.staff_dict[general_computations.staff_names[0]], 'OFFICE')
        self.assertIn(
            self.dojo.staff_dict[general_computations.staff_names[0]], 
            self.dojo.office_dict[room_allocated].allocation_list, 
            'Allocation failed'
        )


    #Test office allocation
    def test_living_space_allocation(self):
        self.dojo = Dojo()
        general_computations = GeneralComputations(self.dojo)
        room_number = 10
        fellow_number = 1
        general_computations.create_living_space_rooms(room_number)
        general_computations.create_fellows(fellow_number)
        room_allocated = general_computations.room_allocation(self.dojo.fellow_dict[general_computations.fellows_names[0]], 'LIVINGSPACE')
        self.assertIn(
            self.dojo.fellow_dict[general_computations.fellows_names[0]], 
            self.dojo.living_space_dict[room_allocated].allocation_list, 
            'Allocation failed'
        )


    #Test unallocated people
    def test_unallocated_people(self):
        self.dojo = Dojo()
        general_computations = GeneralComputations(self.dojo)
        room_number = 2
        fellow_number = 26
        expected_allocations = 12
        general_computations.create_office_rooms(room_number)
        general_computations.create_fellows(fellow_number)
        for person in self.dojo.fellow_dict:
            general_computations.room_allocation(self.dojo.fellow_dict[person], 'OFFICE')
        
        unallocated_list = self.dojo.get_unallocated_people()
        self.assertEqual(
            fellow_number-expected_allocations,
            len(unallocated_list['OFFICE']),
            'The number of people that is expected to be unallocated doesnot match that returned'
        )

