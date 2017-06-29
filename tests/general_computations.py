from unittest import TestCase
from app.models.living_space import LivingSpace
from app.models.office import Office
from app.models.fellow import Fellow
from app.models.staff import Staff

class GeneralComputations(object):
    
    #Set up the various class variables to be used during during tests
    def __init__(self, dojo):
        self.dojo = dojo
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

        #Create list of classes for living space
    def create_living_space_rooms(self, room_number):
        for room_name in self.living_space_rooms_names[:room_number]:
            self.dojo.create_room('LIVINGSPACE', room_name)


    #Create list of classes for office
    def create_office_rooms(self, room_number):
        for room_name in self.office_rooms_names[:room_number]:
            self.dojo.create_room('OFFICE', room_name)


    #Create list of classes for fellows
    def create_fellows(self, fellow_number):
        for fellow_name in self.fellows_names[:fellow_number]:
            self.dojo.add_person( 'FELLOW', fellow_name )

    
    #Create list of classes for staff
    def create_staff(self, staff_number):
        for staff_name in self.staff_names[:staff_number]:
            self.dojo.add_person( 'STAFF', staff_name)
    

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
                        break 
                else:
                    break
            if person_index == allocation_number:
                break
        
        return { "count":count, "room_assignment":room_assignment}
            

    #Method for allocating rooms
    def room_allocation(self, person_object, room_type):
        return self.dojo.allocate_rooms(person_object, room_type)
