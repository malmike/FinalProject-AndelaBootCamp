from unittest import TestCase
from app.controller.dojo import Dojo
from app.models.living_space import LivingSpace
from app.models.office import Office
from app.models.fellow import Fellow
from app.models.staff import Staff

class DojoTests(TestCase):
    def setUp(self):
        self.living_space_rooms_names = ['la', 'lb', 'lc', 'ld', 'le', 'lf', 'lg', 'lh','li','lj','lk','ll','lm','ln','lo']
        self.office_rooms_names = ['oz', 'oy', 'ox', 'ow', 'ov', 'ou', 'ot', 'os', 'or', 'oq']
        self.fellows_names = ['fa','fb','fc','fd','fe','ff','fg','fh','fi','fj','fk','fl','fm','fn','fo','fp','fq','fr','fs','ft','fu','fv','fw','fx','fy','fz']
        self.staff_names = ['sa','sb','sc','sd','se','sf','sg','sh','si','sj','sk','sl','sm','sn','so','sp','sq','sr','ss','st','su','sv','sw','sx','sy','sz']
        #Create classes for living space
        self.living_space_rooms = [LivingSpace(x) for x in self.living_space_rooms_names]
        self.office_rooms = [Office(x) for x in self.office_rooms_names]
        self.list_fellows = [Fellow(x) for x in self.fellows_names]
        self.list_staffs = [Staff(x) for x in self.staff_names]
        #Assign people to the rooms
        person_index = 0
        self.assigned_living_space = []
        for i in self.living_space_rooms: 
            while True:
                if person_index <= 25:
                    if i.is_room_assignable():
                        i.add_person(self.list_fellows[person_index])
                        person_index += 1
                    else:
                        self.assertEqual(4, i.get_allocate_len(), "Maximum number of people assigned to living space does not match returned number")
                        self.assigned_living_space.append(i)
                        break 
                else:
                    break
            if person_index == 26:
                break
        self.assertEqual(6,len(self.assigned_living_space), "Rooms assigned in the test method do not match the expected number")

    def test_dojo_is_instance_of_Dojo(self):
        dojo = Dojo()
        self.assertIsInstance(dojo, Dojo, "Object dojo is not an instance of class Dojo")
    def test_dojo_has_dict_of_rooms(self):
        dojo = Dojo()
        self.assertTrue(isinstance(dojo.living_space_dict,dict), "Class dojo doesnot contain any dictionary living_space_dict")
        self.assertTrue(isinstance(dojo.office_dict,dict), "Class dojo doesnot contain any dictionary office_dict")
    def test_dojo_has_dict_of_people(self):
        dojo = Dojo()
        self.assertTrue(isinstance(dojo.people_dict, dict), "Class dojo doesnot contain any dictionary people_dict")
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
    def test_unallocated_and_allocated_living_space(self):
        dojo = Dojo()
        initial_office_list_length = len(dojo.living_space_dict)  
        for items in self.living_space_rooms_names:
            dojo.create_room("LIVINGSPACE", items)
        self.assertEqual(len(self.living_space_rooms_names), len(dojo.living_space_dict)-initial_office_list_length, "Rooms added to the office list do not match the number inserted")
        #Insert test values into the living_space rooms in the dojo dictionary living_space_dict
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
        self.assertEqual(count, 6, "The expected number should be 6")
        self.assertEqual(len(dojo.living_space_dict)-count, 9, "The expected number of unallocated rooms should be 9")
        self.assertEqual(4, dojo.living_space_dict[test_index].get_allocate_len(), "Value held by the living space dictionary has not been updated")

        value = dojo.sort_allocated_room(dojo.living_space_dict, 'LIVINGSPACE')
        self.assertTrue(value, "The sorting stopped mid way, check the reason. Probable problem is you are passing wrong room_type")
        length_of_assigned_living_space_list = len(dojo.allocated_living_space)
        length_of_unassigned_living_space_list = len(dojo.unallocated_living_space)
        self.assertEqual(length_of_assigned_living_space_list, len(self.assigned_living_space), "The living space dict was not properly sorted")
        self.assertEqual(length_of_unassigned_living_space_list, len(self.living_space_rooms)-len(self.assigned_living_space), "The living space dict was not properly sorted")
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
    def test_allocate_office(self):
        dojo = Dojo()
        for office in  self.office_rooms_names:
            value = dojo.create_room("OFFICE", office)
            self.assertTrue(value, "Why isn't the create room function working, cross check the tests and methods for create room")
        self.assertEqual(len(dojo.office_dict), len(self.office_rooms_names), "Why were not all rooms created? Verify your create room method and the test")
        for staff in self.staff_names:
            value = dojo.add_person("STAFF", staff)
            self.assertTrue(value, "The add person function is failing. Check it and also verify that it's test is proper")
        self.assertEqual(len(dojo.staff_dict), len(self.staff_names), "Why were not all staff created? Verify your add person method and the test")
        for item in dojo.staff_dict:
            value = dojo.allocate_rooms(dojo.staff_dict[item], "OFFICE")
            self.assertTrue(value, "Staff value has failed to be allocated an office")
        for item in dojo.allocated_offices:
            self.assertEqual(len(item.allocation_list), len(dojo.office_dict[item.name].allocation_list), "Values in the office dictionary do not match those in the allocated office list")
        for item in dojo.unallocated_offices:
            self.assertEqual(len(item.allocation_list), len(dojo.office_dict[item.name].allocation_list), "Values in the office dictionary do not match those in the unallocated office list")
    def test_allocate_living_space(self):
        dojo = Dojo()
        for living_space in self.living_space_rooms_names:
            value = dojo.create_room("LIVINGSPACE", living_space)
            self.assertTrue(value, "Why isn't the create room function working, cross check the tests and methods for create room")
        self.assertEqual(len(dojo.living_space_dict), len(self.living_space_rooms_names), "Why were not all rooms created? Verify your create room method and the test")
        for fellow in self.fellows_names:
            value = dojo.add_person("FELLOW", fellow)
            self.assertTrue(value, "The add person function is failing. Check it and also verify that it's test is proper")
        self.assertEqual(len(dojo.living_space_dict), len(self.living_space_rooms_names), "Why were not all staff created? Verify your add person method and the test")
        for item in dojo.living_space_dict:
            value = dojo.allocate_rooms(dojo.living_space_dict[item], "LIVINGSPACE")
            self.assertTrue(value, "Fellow value has failed to be allocated living space")
        for item in dojo.allocated_living_space:
            self.assertEqual(len(item.allocation_list), len(dojo.living_space_dict[item.name].allocation_list), "Values in the living space dictionary do not match those in the allocated living space list")
        for item in dojo.unallocated_living_space:
            self.assertEqual(len(item.allocation_list), len(dojo.living_space_dict[item.name].allocation_list), "Values in the living space dictionary do not match those in the unallocated living space list")
    def test_person_exists_in_dict(self):
        dojo = Dojo()
        blue_person = dojo.add_person('FELLOW', 'Blue')
        value = dojo.find_person('Blue', 'FELLOW')
        value2 = dojo.find_person('Blue2', 'FELLOW')
        self.assertTrue(value, "Value should be existing in the fellow dictionary")
        self.assertFalse(value2, "Value 2 should not exist in the fellow dictionary")
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
        list_items = dojo.room_occupants('Blue', 'OFFICE')
        value = dojo.room_occupants('test', 'OFFICE')
        self.assertListEqual(list_items, assigned_people, 'The values returned should match those in the test list')
        self.assertFalse(value, 'The room put should not exsit in the office dictionary')
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
        list_items = dojo.room_occupants('Blue', 'OFFICE')
        value = dojo.room_occupants('test', 'OFFICE')
        self.assertListEqual(list_items, assigned_people, 'The values returned should match those in the test list')
        self.assertFalse(value, 'The room put should not exsit in the office dictionary')
    def test_get_room_allocations(self):
        dojo = Dojo()
        list_length = len(dojo.living_space_dict)  
        for items in self.living_space_rooms_names:
            value = dojo.create_room("LIVINGSPACE", items)
            self.assertTrue(value)
        self.assertEqual(len(self.living_space_rooms_names), len(dojo.living_space_dict)-list_length, "Rooms added to the office list do not match the number inserted")
        #Insert test values into the living_space rooms in the dojo dictionary living_space_dict
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
        self.assertEqual(count, 6, "The expected number should be 6")
        self.assertEqual(len(dojo.living_space_dict)-count, 9, "The expected number of unallocated rooms should be 9")
        self.assertEqual(4, dojo.living_space_dict[test_index].get_allocate_len(), "Value held by the living space dictionary has not been updated")

        list_length = len(dojo.office_dict)  
        for items in self.office_rooms_names:
            dojo.create_room("OFFICE", items)
        self.assertEqual(len(self.office_rooms_names), len(dojo.office_dict)-list_length, "Rooms added to the office list do not match the number inserted")
        #Insert test values into the living_space rooms in the dojo dictionary living_space_dict
        person_index = 0
        test_index = ""
        count2 = 0
        for item in dojo.office_dict: 
            while True:
                if person_index <= 25:
                    if dojo.office_dict[item].is_room_assignable():
                        dojo.office_dict[item].add_person(self.list_staffs[person_index])
                        person_index += 1
                    else:
                        self.assertEqual(6, dojo.office_dict[item].get_allocate_len(), "Maximum number of people assigned to living space does not match returned number")
                        test_index = item
                        count2 += 1
                        break 
                else:
                    break
            if person_index == 26:
                break
        self.assertEqual(count2, 4, "The expected number should be 6")
        value = dojo.get_allocations()
        self.assertLess( count + count2, len(value), "Not all the values were returned")
        self.assertTrue(isinstance(value, dict), 'The returned value should be a dictionary')
        
