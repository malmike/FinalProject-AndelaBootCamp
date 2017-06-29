from unittest import TestCase
from app.controller.dojo import Dojo
from tests.general_computations import GeneralComputations

class ReallocationsTests(TestCase):


    #Set up the various class variables to be used during during tests
    def setUp(self):
        dojo = Dojo()

    
    #Test to get the room type
    def test_get_room_type(self):
        self.dojo = Dojo()
        general_computations = GeneralComputations(self.dojo)
        room_number = 26
        general_computations.create_office_rooms(room_number)
        general_computations.create_living_space_rooms(room_number)
        office_type = self.dojo.get_room_type(general_computations.office_rooms_names[5])
        self.assertEqual(office_type, 'OFFICE', 'Room type returned is not the expected room type')

        living_space_type = self.dojo.get_room_type(general_computations.living_space_rooms_names[5])
        self.assertEqual(living_space_type, 'LIVINGSPACE', 'Room type returned is not the expected room type')

        non_existant_room = self.dojo.get_room_type('blue')
        self.assertFalse(non_existant_room, 'This room is not supposed to exist')
    

    #Test for finding person in the living space dictionaries
    def test_get_living_space_assigned(self):
        self.dojo = Dojo()
        general_computations = GeneralComputations(self.dojo)
        general_computations.create_living_space_rooms(2)
        general_computations.create_fellows(26)
        allocated_person = ""
        for person in self.dojo.fellow_dict:
            allocated_room = general_computations.room_allocation(self.dojo.fellow_dict[person], 'LIVINGSPACE')
            if allocated_room:
                allocated_person = person
        
        room_allocated = self.dojo.get_room_assigned('LIVINGSPACE', allocated_person)
        self.assertIn(
            self.dojo.fellow_dict[allocated_person], 
            self.dojo.living_space_dict[room_allocated].allocation_list, 
            'Verify that the person was allocated to the returned room'
        )


    #Test for finding person in unallocated list 
    def test_get_living_space_unassigned(self):
        self.dojo = Dojo()
        general_computations = GeneralComputations(self.dojo)
        general_computations.create_living_space_rooms(2)
        general_computations.create_fellows(26)
        unallocated_person = ""
        for person in self.dojo.fellow_dict:
            allocated_room = general_computations.room_allocation(self.dojo.fellow_dict[person], 'LIVINGSPACE')
            if not allocated_room:
                unallocated_person = person

        unallocated = self.dojo.get_room_assigned('LIVINGSPACE', unallocated_person)
        self.assertIn(
            unallocated, 
            self.dojo.unallocated_people['LIVINGSPACE'], 
            'Verify that the person was allocated to the returned room'
        )


    #Test for finding person in the living space dictionaries
    def test_get_office_assigned(self):
        self.dojo = Dojo()
        general_computations = GeneralComputations(self.dojo)
        general_computations.create_office_rooms(2)
        general_computations.create_staff(26)
        allocated_person = ""
        for person in self.dojo.staff_dict:
            allocated_room = general_computations.room_allocation(self.dojo.staff_dict[person], 'OFFICE')
            if allocated_room:
                allocated_person = person
        
        room_allocated = self.dojo.get_room_assigned('OFFICE', allocated_person)
        self.assertIn(
            self.dojo.staff_dict[allocated_person], 
            self.dojo.office_dict[room_allocated].allocation_list, 
            'Verify that the person was allocated to the returned room'
        )
    

    #Test for finding person in unallocated list 
    def test_get_office_unassigned(self):
        self.dojo = Dojo()
        general_computations = GeneralComputations(self.dojo)
        general_computations.create_office_rooms(2)
        general_computations.create_staff(26)
        unallocated_person = ""
        for person in self.dojo.staff_dict:
            allocated_room = general_computations.room_allocation(self.dojo.staff_dict[person], 'OFFICE')
            if not allocated_room:
                unallocated_person = person

        unallocated = self.dojo.get_room_assigned('OFFICE', unallocated_person)
        self.assertIn(
            unallocated, 
            self.dojo.unallocated_people['OFFICE'], 
            'Verify that the person was allocated to the returned room'
        )

    
    #Test for unallocating a person from an office
    def test_unallocate_office(self):
        self.dojo = Dojo()
        general_computations = GeneralComputations(self.dojo)
        general_computations.create_office_rooms(2)
        general_computations.create_staff(26)
        allocated_person = ""
        for person in self.dojo.staff_dict:
            allocated_room = general_computations.room_allocation(self.dojo.staff_dict[person], 'OFFICE')
            if allocated_room:
                allocated_person = person
        
        room_allocated = self.dojo.get_room_assigned('OFFICE', allocated_person)
        self.assertIn(
            self.dojo.staff_dict[allocated_person], 
            self.dojo.office_dict[room_allocated].allocation_list, 
            'Verify that the person was allocated to the returned room'
        )
    
        self.dojo.unallocate_room(room_type, room_allocated, self.dojo.staff_dict[allocated_person])
        self.assertNotIn(
            self.dojo.staff_dict[allocated_person], 
            self.dojo.office_dict[room_allocated].allocation_list, 
            'Verify that the person was unallocated from the returned room'
        )


    #Test for unallocating a person from living space 
    def test_unallocate_living_space(self):
        self.dojo = Dojo()
        general_computations = GeneralComputations(self.dojo)
        general_computations.create_living_space_rooms(2)
        general_computations.create_fellows(26)
        allocated_person = ""
        for person in self.dojo.fellow_dict:
            allocated_room = general_computations.room_allocation(self.dojo.fellow_dict[person], 'LIVINGSPACE')
            if allocated_room:
                allocated_person = person
        
        room_allocated = self.dojo.get_room_assigned('LIVINGSPACE', allocated_person)
        self.assertIn(
            self.dojo.fellow_dict[allocated_person], 
            self.dojo.living_space_dict[room_allocated].allocation_list, 
            'Verify that the person was allocated to the returned room'
        )

        self.dojo.unallocate_room(room_type, room_allocated, self.dojo.fellow_dict[allocated_person])
        self.assertNotIn(
            self.dojo.fellow_dict[allocated_person], 
            self.dojo.living_space_dict[room_allocated].allocation_list, 
            'Verify that the person was unallocated from the returned room'
        )