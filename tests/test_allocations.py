from unittest import TestCase
from app.controller.dojo import Dojo
from app.models.living_space import LivingSpace
from app.models.office import Office
from app.models.fellow import Fellow
from app.models.staff import Staff

class AllocationsTests(TestCase):


    #Set up the various class variables to be used during during tests
    def setUp(self):
        self.dojo = Dojo()
        self.living_space_rooms_names = [
            'la','lb','lc','ld','le','lf','lg','lh','li','lj',
            'lk','ll','lm','ln','lo','lp','lq','lr','ls','lt',
            'lu','lv','lw','lx','ly','lz'
        ]
        self.office_rooms_names = [
            'oa','ob','oc','od','oe','of','og','oh','oi','oj',
            'ok','ol','om','on','oo','op','oq','or','os','ot',
            'ou','ov','ow','ox','oy','oz',
        ]
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

    
    #Test the method for assigning the sample offices
    def test_assign_sample_offices(self):
        self.dojo = Dojo()
        number_of_assigned_offices = self.assign_sample_offices('STAFF', 10, 25)["count"]
        self.assertEqual(4,number_of_assigned_offices, "Rooms assigned in the test method do not match the expected number")

    
    #Test the method for assigning the sample living space
    def test_assign_sample_living_space(self):
        self.dojo = Dojo()
        number_of_assigned_living_space = self.assign_sample_living_space(10, 25)["count"]
        self.assertEqual(6, number_of_assigned_living_space, "Rooms assigned in the test method do not match the expected number")


    #Test to check for people assigned to a room 
    def test_print_office(self):
        self.dojo = Dojo()
        office_allocations = self.assign_sample_offices('STAFF', 3, 24)["room_assignment"]
        office_allocation_list = office_allocations[self.office_rooms_names[2]]
        assigned_staff_list = self.dojo.room_occupants(self.office_rooms_names[2])
        self.assertEqual(office_allocation_list, assigned_staff_list, 'List doesnot match')


    #Test to check all room allocations
    def test_print_allocations(self):
        self.dojo = Dojo()
        office_allocations = self.assign_sample_offices('STAFF', 3, 24)["room_assignment"]
        living_space_allocations = self.assign_sample_living_space(3, 24)["room_assignment"]
        assigned_allocations = self.dojo.get_allocations()
        expected_allocations_list = living_space_allocations
        expected_allocations_list.update(office_allocations)
        self.assertEqual(len(expected_allocations_list), len(assigned_allocations), 'List doesnot match')


    #Test to check offices that still have unassigned places
    def test_get_unallocated_offices(self):
        self.dojo = Dojo()
        room_number = 20
        staff_number = 26
        office_allocations_count = self.assign_sample_offices('STAFF', room_number, staff_number)["count"]
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
        room_number = 10
        fellow_number = 26
        living_space_allocation_count = self.assign_sample_living_space( room_number, fellow_number)["count"]
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
        room_number = 10
        staff_number = 1
        self.create_office_rooms(room_number)
        self.create_staff(staff_number)
        room_allocated = self.room_allocation(self.dojo.staff_dict[self.staff_names[0]], 'OFFICE')
        self.assertIn(
            self.dojo.staff_dict[self.staff_names[0]], 
            self.dojo.office_dict[room_allocated].allocation_list, 
            'Allocation failed'
        )


    #Test office allocation
    def test_living_space_allocation(self):
        self.dojo = Dojo()
        room_number = 10
        fellow_number = 1
        self.create_living_space_rooms(room_number)
        self.create_fellows(fellow_number)
        room_allocated = self.room_allocation(self.dojo.fellow_dict[self.fellows_names[0]], 'LIVINGSPACE')
        self.assertIn(
            self.dojo.fellow_dict[self.fellows_names[0]], 
            self.dojo.living_space_dict[room_allocated].allocation_list, 
            'Allocation failed'
        )


    #Test unallocated people
    def test_unallocated_people(self):
        self.dojo = Dojo()
        room_number = 2
        fellow_number = 26
        expected_allocations = 12
        self.create_office_rooms(room_number)
        self.create_fellows(fellow_number)
        for person in self.dojo.fellow_dict:
            self.room_allocation(self.dojo.fellow_dict[person], 'OFFICE')
        
        unallocated_list = self.dojo.get_unallocated_people()
        self.assertEqual(
            fellow_number-expected_allocations,
            len(unallocated_list['OFFICE']),
            'The number of people that is expected to be unallocated doesnot match that returned'
        )


    #Test to get the room type
    def test_get_room_type(self):
        self.dojo = Dojo()
        room_number = 26
        self.create_office_rooms(room_number)
        self.create_living_space_rooms(room_number)
        office_type = self.dojo.get_room_type(self.office_rooms_names[5])
        self.assertEqual(office_type, 'OFFICE', 'Room type returned is not the expected room type')

        living_space_type = self.dojo.get_room_type(self.living_space_rooms_names[5])
        self.assertEqual(living_space_type, 'LIVINGSPACE', 'Room type returned is not the expected room type')

        non_existant_room = self.dojo.get_room_type('blue')
        self.assertFalse(non_existant_room, 'This room is not supposed to exist')
    

    #Test for finding person in the various dictionaries
    def test_get_room_assigned(self):
        self.dojo = Dojo()
        self.create_living_space_rooms(2)
        self.create_fellows(26)
        for person in self.dojo.fellow_dict:
            self.room_allocation(self.dojo.fellow_dict[person], 'LIVINGSPACE')
        
        room_allocated = self.dojo.get_room_assigned('LIVINGSPACE', self.fellows_names[3])
        self.assertIn(
            self.dojo.fellow_dict[person], 
            self.dojo.living_space_dict[room_allocated], 
            'Verify that the person was allocated to the returned room'
        )


    #Create list of classes for living space
    def create_living_space_rooms(self, room_number):
        living_space_count = len(self.dojo.living_space_dict)
        for room_name in self.living_space_rooms_names[:room_number]:
            self.dojo.create_room('LIVINGSPACE', room_name)
        self.assertEqual(len(self.dojo.living_space_dict)-living_space_count, room_number, 'Not all living space rooms are created')


    #Create list of classes for office
    def create_office_rooms(self, room_number):
        office_count = len(self.dojo.office_dict)
        for room_name in self.office_rooms_names[:room_number]:
            self.dojo.create_room('OFFICE', room_name)
        self.assertEqual(len(self.dojo.office_dict)-office_count, room_number, 'Not all office rooms are created')


    #Create list of classes for fellows
    def create_fellows(self, fellow_number):
        fellow_count = len(self.dojo.fellow_dict)
        for fellow_name in self.fellows_names[:fellow_number]:
            self.dojo.add_person( 'FELLOW', fellow_name )
        self.assertEqual(len(self.dojo.fellow_dict)-fellow_count, fellow_number, 'Not all fellows are created')

    
    #Create list of classes for staff
    def create_staff(self, staff_number):
        staff_count = len(self.dojo.staff_dict)
        for staff_name in self.staff_names[:staff_number]:
            self.dojo.add_person( 'STAFF', staff_name)
        self.assertEqual(len(self.dojo.staff_dict)-staff_count, staff_number, 'Not all fellows are created')
    

    #Assign sample offices
    def assign_sample_offices(self, person_type, room_number, allocation_number):
        room_assignment = {}
        person_index = 0
        count = 0
        if person_type is "STAFF":
            self.create_staff(allocation_number)
            self.create_office_rooms(room_number)
        elif person_type is "FELLOW":
            self.create_fellows(allocation_number)
            self.create_office_rooms(room_number)
        else:
            raise ValueError('The arguments passed are incorrect, check them')

        #Start assigning offices
        for office in self.dojo.office_dict:
            room_assignment[office] = []
            while True:
                if person_index < allocation_number:
                    if self.dojo.office_dict[office].is_room_assignable():
                        if person_type is "STAFF":
                            self.dojo.office_dict[office].add_person(self.dojo.staff_dict[self.staff_names[person_index]])
                            room_assignment[office].append(self.dojo.staff_dict[self.staff_names[person_index]])
                            person_index += 1
                        elif person_type is "FELLOW":
                            self.dojo.office_dict[office].add_person(self.dojo.fellow_dict[self.fellows_names[person_index]])
                            room_assignment[office].append(self.dojo.fellow_dict[self.fellows_names[person_index]])
                            person_index += 1
                        else:
                            raise ValueError('The arguments passed are incorrect, check them')

                        if not self.dojo.office_dict[office].is_room_assignable():
                            count += 1
                    else:   
                        self.assertEqual(6, self.dojo.office_dict[office].get_allocate_len(), "Maximum number of people assigned to office does not match returned number")
                        break 
                else:
                    break
            if person_index == allocation_number:
                break
        
        return { "count":count, "room_assignment":room_assignment}


    #Assign sample living space
    def assign_sample_living_space(self, room_number, allocation_number):
        room_assignment = {}
        person_index = 0
        count = 0
        self.create_fellows(allocation_number)
        self.create_living_space_rooms(room_number)

        #Start assigning offices
        for living_space in self.dojo.living_space_dict:
            room_assignment[living_space] = []
            while True:
                if person_index < allocation_number:
                    if self.dojo.living_space_dict[living_space].is_room_assignable():
                        self.dojo.living_space_dict[living_space].add_person(self.dojo.fellow_dict[self.fellows_names[person_index]])
                        room_assignment[living_space].append(self.dojo.fellow_dict[self.fellows_names[person_index]])
                        person_index += 1
                        if not self.dojo.living_space_dict[living_space].is_room_assignable(): 
                            count += 1
                    else:   
                        self.assertEqual(4, self.dojo.living_space_dict[living_space].get_allocate_len(), "Maximum number of people assigned to living space does not match returned number")
                        break 
                else:
                    break
            if person_index == allocation_number:
                break
        
        return { "count":count, "room_assignment":room_assignment}
            

    #Method for allocating rooms
    def room_allocation(self, person_object, room_type):
        return self.dojo.allocate_rooms(person_object, room_type)