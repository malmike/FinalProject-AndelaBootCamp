from app.models.office import Office
from app.models.living_space import LivingSpace

class Dojo(object):
    
    def __init__(self):
        self.people_dict = {}
        self.office_dict = {}
        self.living_space_dict = {}
    def create_room(self, room_name, room_type):
        if isinstance(room_name, str) and isinstance(room_type, str):
            if room_type == "office" and room_name not in self.office_dict:
                office = Office(room_name)
                self.office_dict[room_name] = office
                return True
            elif room_type == "living_space" and room_name not in self.living_space_dict:
                living_space = LivingSpace(room_name)
                self.living_space_dict[room_name] = living_space
                return True
            else:
                return False
        else:
            return False
                 
