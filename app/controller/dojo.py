from app.models.office import Office
from app.models.living_space import LivingSpace
from app.models.fellow import Fellow
from app.models.staff import Staff
from app.database_methods.create_schema import CreateSchema
import random



class Dojo(object):
    
    def __init__(self):
        self.people_dict = {}
        self.office_dict = {}
        self.living_space_dict = {}
        self.unallocated_offices = []
        self.allocated_offices = []
        self.unallocated_living_space = []
        self.allocated_living_space = []
        self.fellow_dict = {}
        self.staff_dict = {}
        self.unallocated_people = {}

    def create_room(self, room_type, room_name):
        if isinstance(room_type, str):
            if room_type == "OFFICE" and room_name not in self.office_dict:
                office = Office(room_name)
                self.office_dict[room_name] = office
                self.unallocated_offices.append(office)
                return office
            elif room_type == "LIVINGSPACE" and room_name not in self.living_space_dict:
                living_space = LivingSpace(room_name)
                self.living_space_dict[room_name] = living_space
                self.unallocated_living_space.append(living_space)
                return living_space
            else:
                return False
        else:
            raise TypeError('Values inserted must both be strings')
    def add_person(self, person_type, person_name):
        if isinstance(person_type, str):
            if person_type == "FELLOW" and person_name not in self.fellow_dict:
                fellow = Fellow(person_name)
                self.fellow_dict[person_name] = fellow
                return fellow
            elif person_type == "STAFF" and person_name not in self.staff_dict:
                staff = Staff(person_name)
                self.staff_dict[person_name] = staff
                return staff
            else:
                return False
        else:
            raise TypeError('Values inserted must both be strings')
           
    def sort_allocated_room(self, sample_dictionary, room_type):
        self.allocated_living_space = []
        self.unallocated_living_space = []
        for item in sample_dictionary:
            if sample_dictionary[item].is_room_assignable():
                if room_type is "LIVINGSPACE":
                    self.unallocated_living_space.append(item)
                elif room_type is "OFFICE":
                    self.unallocated_offices.append(item)
                else:
                    return False
            else:
                if room_type is "LIVINGSPACE":
                    self.allocated_living_space.append(item)
                elif room_type is "OFFICE":
                    self.allocated_offices.append(item)
                else:
                    return False
        return True
    def allocate_rooms(self, person_object, room_type):
        if room_type is "OFFICE":
            
            if len(self.unallocated_offices) > 0:   
                index = random.choice(range(len(self.unallocated_offices)))
                value = self.unallocated_offices[index].add_person(person_object)
                if not value:
                    if not self.unallocated_offices[index].is_room_assignable:
                        self.allocated_offices.append(self.unallocated_offices[index])
                        del self.unallocated_offices[index]
                    return self.allocate_rooms(person_object, room_type)
                else:
                    self.office_dict[self.unallocated_offices[index].name] = self.unallocated_offices[index]
                    allocation_office_name = self.unallocated_offices[index].name
                    if not self.unallocated_offices[index].is_room_assignable:
                        self.allocated_offices.append(self.unallocated_offices[index])
                        del self.unallocated_offices[index]
                    return allocation_office_name
            else:
                self.unallocated_people['OFFICE'] = person_object
                return False
        elif room_type is "LIVINGSPACE":
            if len(self.unallocated_living_space) > 0:
                index = random.choice(range(len(self.unallocated_living_space)))
                value = self.unallocated_living_space[index].add_person(person_object)
                if not value:
                    if not self.unallocated_living_space[index].is_room_assignable:
                        self.allocated_living_space.append(self.unallocated_living_space[index])
                        del self.unallocated_living_space[index]
                    return self.allocate_rooms(person_object, room_type)
                else:
                    self.living_space_dict[self.unallocated_living_space[index].name] = self.unallocated_living_space[index]
                    allocation_living_space_name = self.unallocated_living_space[index].name
                    if not self.unallocated_living_space[index].is_room_assignable:
                        self.allocated_living_space.append(self.unallocated_living_space[index])
                        del self.unallocated_living_space[index]
                    return allocation_living_space_name
            else:
                self.unallocated_people['LIVINGSPACE'] = person_object
                return False
        else:
            return False
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
    def room_occupants(self, room_name):
        if room_name in self.office_dict:
            return self.office_dict[room_name].allocation_list
        elif room_name in self.living_space_dict:
            return self.living_space_dict[room_name].allocation_list
        else:
            return False

    def get_allocations(self):
        allocations_list = {}
        for i in self.office_dict:
            if len(self.office_dict[i].allocation_list) > 0:
                allocations_list[self.office_dict[i].name] = self.office_dict[i].allocation_list
        for i in self.living_space_dict:
            if len(self.living_space_dict[i].allocation_list) > 0:
                allocations_list[self.living_space_dict[i].name] = self.living_space_dict[i].allocation_list  
        return allocations_list 
    def get_unallocated_people(self):
        return self.unallocated_people

    def save_state(self, db):
        create_schema = CreateSchema(db)
        create_schema.save_state(self.office_dict, self.living_space_dict, self.staff_dict, self.fellow_dict)

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
        print (office_alloc)
        print (livingspaces_alloc)
        print (staffs)

        for office in offices:
            self.create_room("OFFICE", office[0])
        for livingspace in livingspaces:
            self.create_room("LIVINGSPACE", livingspace[0])
        for staff in staffs:
            self.create_room("STAFF", staff[0])
        for fellow in fellows:
            self.create_room("FELLOW", fellow[0])
        print ('Creating office staff allocations')
        for alloc_office in office_staff_alloc:
            print (alloc_office)
        print ('Creating office fellow allocations')
        for alloc_office in office_fellow_alloc:
            print (alloc_office)
        print ('Living space allocations')
        for alloc_living_space in livingspaces_alloc:
            print (alloc_living_space)

            
        