from app.models.office import Office
from app.models.living_space import LivingSpace
from app.models.fellow import Fellow
from app.models.staff import Staff
from app.database_methods.create_schema import CreateSchema
import random
"""
This is the main controller class of the application. It is meant to interact with the 
models and database interaction files and also with the user interaction interface module
"""


class Dojo(object):


    #Initializing the varibles that are used by the class
    def __init__(self):
        self.office_dict = {}
        self.living_space_dict = {}
        self.fellow_dict = {}
        self.staff_dict = {}
        self.unallocated_people = {'OFFICE':[], 'LIVINGSPACE':[]}


    #Method to create a room
    def create_room(self, room_type, room_name):
        if isinstance(room_type, str):
            #Create an office room and add it to office list
            if room_type == "OFFICE" and room_name not in self.office_dict:
                office = Office(room_name)
                self.office_dict[room_name] = office
                return office
            #Create livingspace room and add it to livingspace list
            elif room_type == "LIVINGSPACE" and room_name not in self.living_space_dict:
                living_space = LivingSpace(room_name)
                self.living_space_dict[room_name] = living_space
                return living_space
            else:
                return False
        else:
            raise TypeError('Values inserted must both be strings')


    #Add a method to add a person
    def add_person(self, person_type, person_name):
        if isinstance(person_type, str):
            #Add a fellow and add to the fellow list
            if person_type == "FELLOW" and person_name not in self.fellow_dict:
                fellow = Fellow(person_name)
                self.fellow_dict[person_name] = fellow
                return fellow
            #Add a staff and add to the staff list
            elif person_type == "STAFF" and person_name not in self.staff_dict:
                staff = Staff(person_name)
                self.staff_dict[person_name] = staff
                return staff
            else:
                return False
        else:
            raise TypeError('Values inserted must both be strings')


    #Method to get unallocated rooms
    def get_unallocated_rooms(self, room_type):
        unallocated_rooms = []
        if isinstance(room_type, str):
            #sort though the office/ living space dictionary and get unallocated rooms
            if room_type.upper() == 'OFFICE':
                for room in self.office_dict:
                    if self.office_dict[room].is_room_assignable():
                        unallocated_rooms.append(room)
            elif room_type.upper() == 'LIVINGSPACE':
                for room in self.living_space_dict:
                    if self.living_space_dict[room].is_room_assignable():
                        unallocated_rooms.append(room)
            else:
                raise ValueError('Room type entered must be OFFICE or LIVINGSPACE')

            return unallocated_rooms
            
        else:
            raise TypeError('Room Type must be a string')


    #Method to allocate rooms at random, it takes in a person objec and room type
    def allocate_rooms(self, person_object, room_type):
        unallocated_rooms = self.get_unallocated_rooms(room_type)

        if unallocated_rooms:
            if room_type == "OFFICE":
                index = random.choice(range(len(unallocated_rooms)))
                value = self.office_dict[unallocated_rooms[index]].add_person(person_object)
                if not value:
                    return value
                else:
                    return unallocated_rooms[index]
            elif room_type == "LIVINGSPACE":
                index = random.choice(range(len(unallocated_rooms)))
                value = self.living_space_dict[unallocated_rooms[index]].add_person(person_object)
                if not value:
                    return value
                else:
                    return unallocated_rooms[index]
            else:
                raise ValueError('Room type entered must be OFFICE or LIVINGSPACE')
        else:
            self.unallocated_people[room_type.upper()].append(person_object)
            return False


    #Method to find if person is already assigned to the dictionary
    def find_person(self, person_name, position):
        if position is "FELLOW":
            if person_name in self.fellow_dict:
                return True
            else:
                return False
        if position is "STAFF":
            if person_name in self.staff_dict:
                return True
            else:
                return False


    #Method to get room occupants
    def room_occupants(self, room_name):
        if room_name in self.office_dict:
            return self.office_dict[room_name].allocation_list
        elif room_name in self.living_space_dict:
            return self.living_space_dict[room_name].allocation_list
        else:
            return False


    #Method to get all room allocations
    def get_allocations(self):
        allocations_list = {}
        for i in self.office_dict:
            if len(self.office_dict[i].allocation_list) > 0:
                allocations_list[self.office_dict[i].name] = self.office_dict[i].allocation_list
        for i in self.living_space_dict:
            if len(self.living_space_dict[i].allocation_list) > 0:
                allocations_list[self.living_space_dict[i].name] = self.living_space_dict[i].allocation_list  
        return allocations_list


    #Method to get unallocated people 
    def get_unallocated_people(self):
        return self.unallocated_people


    #Method to save the state of the data into a database
    def save_state(self, db):
        create_schema = CreateSchema(db)
        create_schema.save_state(self.office_dict, self.living_space_dict, self.staff_dict, self.fellow_dict)


    #Method to load data from the database
    def load_data(self, db):
        create_schema = CreateSchema(db)
        offices = create_schema.load_offices()
        livingspaces = create_schema.load_living_space()
        staffs = create_schema.load_staff()
        fellows = create_schema.load_fellow()
        office_staff_alloc = create_schema.load_office_staff_allocations()
        office_fellow_alloc = create_schema.load_office_fellow_allocations()
        livingspaces_alloc = create_schema.load_living_space_allocations()
        office_alloc = create_schema.load_office_allocations()
        #Adding offices
        for office in offices:
            self.create_room("OFFICE", office[0])
        #Adding living spaces
        for livingspace in livingspaces:
            self.create_room("LIVINGSPACE", livingspace[0])
        #Adding staff
        for staff in staffs:
            self.add_person("STAFF", staff[0])
        #Adding fellows
        for fellow in fellows:
            self.add_person("FELLOW", fellow[0])
        #Creating office staff allocations'
        for alloc_office in office_staff_alloc:
            value = self.staff_dict[str(alloc_office[1])]
            self.allocate_rooms(value, "OFFICE")
        #Creating office fellow allocations
        for alloc_office in office_fellow_alloc:
            value = self.fellow_dict[str(alloc_office[2])]
            self.allocate_rooms(value, "OFFICE")
        # Allocating Living space
        for alloc_living_space in livingspaces_alloc:
            value = self.fellow_dict[str(alloc_living_space[1])]
            self.allocate_rooms(value, "LIVINGSPACE")

            
        