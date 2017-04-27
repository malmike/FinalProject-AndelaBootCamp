from app.models.office import Office
from app.models.living_space import LivingSpace
from app.models.fellow import Fellow
from app.models.staff import Staff

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
    def create_room(self, room_name, room_type):
        if isinstance(room_name, str) and isinstance(room_type, str):
            if room_type == "OFFICE" and room_name not in self.office_dict:
                office = Office(room_name)
                self.office_dict[room_name] = office
                #self.unallocated_offices.append(office)
                return True
            elif room_type == "LIVINGSPACE" and room_name not in self.living_space_dict:
                living_space = LivingSpace(room_name)
                self.living_space_dict[room_name] = living_space
                #self.unallocated_living_space.append(living_space)
                return True
            else:
                return False
        else:
            raise TypeError('Values inserted must both be strings')
    def add_person(self, person_name, person_type):
        if isinstance(person_name, str) and isinstance(person_type, str):
            if person_type == "FELLOW" and person_name not in self.fellow_dict:
                fellow = Fellow(person_name)
                self.fellow_dict[person_name] = fellow
                return True
            elif person_type == "STAFF" and person_name not in self.staff_dict:
                staff = Stuff(person_name)
                self.staff_dict[person_name] = staff
                return True
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
        