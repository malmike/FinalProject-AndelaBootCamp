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

    #Test that the Dojo can create an office and add it to the office dictionary
    #Test that the Dojo does not allow for duplicate offices being created
    def test_add_create_office_and_repeated_room(self):
        dojo = Dojo()
        #Check whether one office room can be created
        initial_office_count = len(dojo.office_dict)
        blue_office = dojo.create_room('OFFICE', 'Blue')
        self.assertTrue(blue_office, "Room has not been created")
        new_office_count = len(dojo.office_dict)
        self.assertEqual(new_office_count - initial_office_count, 1, "Multiple values are being added to the office dictionary. Why is that!!!")
        #Check whether the same office room can be created
        initial_office_count = len(dojo.office_dict)
        blue_office2 = dojo.create_room('OFFICE', 'Blue')
        self.assertFalse(blue_office2, "Repeated room being created")
        new_office_count = len(dojo.office_dict)
        self.assertEqual(new_office_count - initial_office_count, 0, "The value is being added to the office dictionary when it should not")
    
    #Test that the Dojo can create a living space and add it to the living space dictionary
    #Test that the Dojo does not allow for duplicate living spaces being created
    def test_add_create_living_space_and_repeated_room(self):
        dojo = Dojo()
        #Check whether one living space room can be created
        initial_room_count = len(dojo.living_space_dict)
        blue_living_space = dojo.create_room('LIVINGSPACE', 'Blue')
        self.assertTrue(blue_living_space, "Room has not been created")
        new_room_count = len(dojo.living_space_dict)
        self.assertEqual(new_room_count - initial_room_count, 1, "Multiple values are being added to the living space dictionary. Why is that!!!")
        #Check whether the same living space room can be created
        initial_room_count = len(dojo.living_space_dict)
        blue_living_space2 = dojo.create_room('LIVINGSPACE', 'Blue')
        self.assertFalse(blue_living_space2, "Repeated room being created")
        new_room_count = len(dojo.living_space_dict)
        self.assertEqual(new_room_count - initial_room_count, 0, "The value is being added to the living space dictionary when it should not")
    
    #Test add that the Dojo can create a fellow or staff and them to the fellow or staff dictionary 
    def test_add_person(self):
        dojo = Dojo()
        #Check whether one person room can be created
        initial_fellow_count = len(dojo.fellow_dict)
        malmike_fellow = dojo.add_person('FELLOW', 'Male Michael')
        self.assertTrue(malmike_fellow, "Fellow has not been created")
        new_fellow_count = len(dojo.fellow_dict)
        self.assertEqual(new_fellow_count - initial_fellow_count, 1, "Multiple values are being added to the fellow dictionary. Why is that!!!")
        #Check whether the same office room can be created
        initial_fellow_count = len(dojo.fellow_dict)
        malmike_fellow2 = dojo.add_person('FELLOW', 'Male Michael')
        self.assertFalse(malmike_fellow2, "Repeated fellow being created")
        new_fellow_count = len(dojo.fellow_dict)
        self.assertEqual(new_fellow_count - initial_fellow_count, 0, "The value is being added to the fellow dictionary when it should not")
    
    #Test living space assignment using test data
    def test_living_space_assignment(self):
        dojo = Dojo()
        assigned_living_space = self.assign_sample_room_objects('LIVINGSPACE')
        self.create_multiple_rooms(dojo, 'LIVINGSPACE')
        #Insert test values into the living_space rooms in the dojo dictionary living_space_dict
        self.assign_living_space(dojo)
        value = dojo.sort_allocated_room(dojo.living_space_dict, 'LIVINGSPACE')
        self.assertTrue(value, "The sorting stopped mid way, check the reason. Probable problem is you are passing wrong room_type")
        self.assertEqual(
            len(dojo.allocated_living_space), 
            len(assigned_living_space), 
            "The living space dict was not properly sorted"
            )
        self.assertEqual(
            len(dojo.unallocated_living_space), 
            len(self.living_space_rooms)-len(assigned_living_space), 
            "The living space dict was not properly sorted"
            )

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
    #Test to check that some one exists in the dictionary
    def test_person_exists_in_dict(self):
        dojo = Dojo()
        blue_person = dojo.add_person('FELLOW', 'Blue')
        value = dojo.find_person('Blue', 'FELLOW')
        value2 = dojo.find_person('Blue2', 'FELLOW')
        self.assertTrue(value, "Value should be existing in the fellow dictionary")
        self.assertFalse(value2, "Value 2 should not exist in the fellow dictionary")
    
    #Test to check for room occupants that are assigned to the room
    def test_get_room_occupants(self):
        dojo = Dojo()
        blue_office = dojo.create_room('OFFICE', 'Blue')
        assigned_people = []
        for i in self.list_fellows:
            if dojo.office_dict['Blue'].is_room_assignable():
                dojo.office_dict['Blue'].add_person(i)
                assigned_people.append(i)
            else:
                break
        self.assertEqual(len(dojo.office_dict['Blue'].allocation_list), len(assigned_people), 'Test values do not match')
        list_items = dojo.room_occupants('Blue')
        value = dojo.room_occupants('test')
        self.assertListEqual(list_items, assigned_people, 'The values returned should match those in the test list')
        self.assertFalse(value, 'The room put should not exist in the office dictionary')
    
    #Test to check room occupants
    def test_get_room_occupants(self):
        dojo = Dojo()
        blue_office = dojo.create_room('OFFICE', 'Blue')
        assigned_people = []
        for i in self.list_fellows:
            if dojo.office_dict['Blue'].is_room_assignable():
                dojo.office_dict['Blue'].add_person(i)
                assigned_people.append(i)
            else:
                break
        self.assertEqual(len(dojo.office_dict['Blue'].allocation_list), len(assigned_people), 'Test values do not match')
        list_items = dojo.room_occupants('Blue')
        value = dojo.room_occupants('test')
        self.assertListEqual(list_items, assigned_people, 'The values returned should match those in the test list')
        self.assertFalse(value, 'The room put should not exsit in the office dictionary')
    
    def test_get_room_allocations(self):
        dojo = Dojo()
        self.create_multiple_rooms(dojo, 'LIVINGSPACE')
        self.add_multiple_people(dojo, "FELLOW")
        count = self.assign_living_space(dojo)
        self.create_multiple_rooms(dojo, 'OFFICE')
        self.add_multiple_people(dojo, "STAFF")
        count2 = self.assign_office(dojo, 'STAFF')
        value = dojo.get_allocations()
        self.assertLess( count + count2, len(value), "Not all the values were returned")
        self.assertTrue(isinstance(value, dict), 'The returned value should be a dictionary')


    """
    The functions below are used for computation purposes by the testing function
    They are functions that are repeated across multiple test functions
    """
    #Assign people to a list of rooms
    def assign_sample_room_objects(self, room_type):
        rooms_list = []
        allocation_len = 0
        number_of_assigned_rooms = 0
        assigned_rooms = []
        person_index = 0
        #Set room variables based on the type of room
        if room_type is 'LIVINGSPACE':
            rooms_list = self.living_space_rooms
            number_of_assigned_rooms = 6
            allocation_len = 4
        elif room_type is 'OFFICE':
            rooms_list = self.office_rooms
            number_of_assigned_rooms = 4
            allocation_len = 6
        else:
            raise ValueError('The room type inserted is unknown, you have to insert LIVINGSPACE or OFFICE')
        #Start assigning rooms
        for i in rooms_list: 
            while True:
                if person_index <= 25:
                    if i.is_room_assignable():
                        i.add_person(self.list_fellows[person_index])
                        person_index += 1
                    else:
                        self.assertEqual(
                            allocation_len, i.get_allocate_len(), 
                            "Maximum number of people assigned to "+ room_type +" does not match returned number"
                            )
                        assigned_rooms.append(i)
                        break 
                else:
                    break
            if person_index == 26:
                break
        self.assertEqual(number_of_assigned_rooms,len(assigned_rooms), "Rooms assigned in the test method do not match the expected number")
        return assigned_rooms
    
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