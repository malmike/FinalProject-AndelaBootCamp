from abc import ABCMeta, abstractmethod

class Room(object):
    __metaclass__ = ABCMeta
    #Initialise the attributes of the Room Class
    capacity = 0
    room_type = ""

    def __init__(self, name):
        self.allocation_list = []
        self.name = name

    def add_person(self, person):
        if len(self.allocation_list) < self.capacity:
            self.allocation_list.append(person)
            return True
        else:
            return False

    def get_allocate_len(self):
        return len(self.allocation_list)

    def is_room_assignable(self):
        if len(self.allocation_list) < self.capacity or not self.allocation_list:
            return True
        else:
            return False
