"""This script contains the Dojo class which contains controller
modules for this application"""

from random import choice
from app.models.office import Office
from app.models.living_space import LivingSpace
from app.models.fellow import Fellow
from app.models.staff import Staff
from app.database_methods.create_schema import CreateSchema


class Dojo(object):
    """Dojo class that is the main class of the system. It acts as a system controller by
    calling and implementing most of the system functionality"""

    #Initializing the variables that are used by the class
    def __init__(self):
        """Init method of the dojo class. Initializes the global variables within the dojo
        class"""
        self.office_dict = {}
        self.living_space_dict = {}
        self.fellow_dict = {}
        self.staff_dict = {}
        self.unallocated_people = {'OFFICE':[], 'LIVINGSPACE':[]}


    #Method to create a room
    def create_room(self, room_type, room_name):
        """
        This creates a room of either office or living space and adds it
        to office_dict or living_space_dict respectively
        :param room_type.upper()
        :param room_name
        :return: Boolean
        """
        self.check_str(RoomType=room_type.upper(), RoomName=room_name)
        room_dict = self.get_dict(room_type.upper())
        room_object = self.add_object_to_dict(room_dict, room_type.upper(), room_name)
        if room_object:
            return True

        return False


    #Add a method to add a person
    def add_person(self, person_type, person_name):
        """
        Adds a person to staff_dict if person_type.upper() is staff or to fellow_dict
        if fellow_type.upper() is fellow
        :params person_type.upper()
        :params person_name
        :return: Object<type 'Person'> or Boolean
        """
        self.check_str(PersonType=person_type.upper(), PersonName=person_name)
        person_dict = self.get_dict(person_type.upper())
        return self.add_object_to_dict(person_dict, person_type.upper(), person_name)



    #Method to get unallocated rooms
    def get_unallocated_rooms(self, room_type):
        """
        Gets a list of unallocated rooms basing on the room_type.upper() provided
        :param room_type.upper()
        :return: List[]
        """
        unallocated_rooms = []
        self.check_str(RoomType=room_type.upper())
        room_dict = self.get_dict(room_type.upper())
        for room in room_dict:
            if room_dict[room].is_room_assignable():
                unallocated_rooms.append(room)

        return unallocated_rooms


    #Method to allocate rooms at random, it takes in a person object and room type
    def allocate_rooms(self, person_object, room_type):
        """
        Allocates a person to a random room
        :param person_object
        :param room_type.upper()
        :return String or Boolean
        """
        unallocated_rooms = self.get_unallocated_rooms(room_type.upper())

        if not unallocated_rooms:
            self.unallocated_people[room_type.upper()].append(person_object)
            return False

        room_dict = self.get_dict(room_type.upper())
        index = choice(range(len(unallocated_rooms)))
        value = room_dict[unallocated_rooms[index]].add_person(person_object)
        if not value:
            return self.allocate_rooms(person_object, room_type.upper())

        return unallocated_rooms[index]


    #Method to get room occupants
    def room_occupants(self, room_name):
        """
        Gets a list of people in a room
        :param room_name
        :return List[]
        """
        self.check_str(RoomName=room_name)
        if room_name in self.office_dict:
            return self.office_dict[room_name].allocation_list

        if room_name in self.living_space_dict:
            return self.living_space_dict[room_name].allocation_list

        return False


    #Method to get all room allocations
    def get_allocations(self):
        """
        Gets a dictionary containing rooms and a list of people allocated to each
        room
        :param
        :return Dictionary
        """
        alloc_list = {}
        rooms = self.get_allocations_for_room_category("OFFICE")
        rooms.update(self.get_allocations_for_room_category("LIVINGSPACE"))
        return rooms

    #Method to get unallocated people
    def get_unallocated_people(self):
        """
        Gets a dictionary containing people not allocated to a specific type of room
        :param
        :return Dictionary
        """
        return self.unallocated_people


    #Method to get the room type of inserted room
    def get_room_type(self, room_name):
        """
        Gets the room type when provided the room name
        :param room_name
        :return String or Boolean
        """
        for room in self.office_dict:
            if room == room_name:
                return 'OFFICE'

        for room in self.living_space_dict:
            if room == room_name:
                return 'LIVINGSPACE'

        return False


    #Method to retrieve the room an individual is assigned
    def get_room_assigned(self, room_type, person_name):
        """
        Gets the room an individual is assigned to or if the individual is
        not allocated to any room
        :param room_type.upper()
        :param person_name
        :return Dictionary
        """
        self.check_str(RoomType=room_type.upper(), PersonName=person_name)

        person_object = self.get_person(person_name)
        if not person_object:
            return "Person does not exist"

        if room_type.upper() == 'LIVINGSPACE' or room_type.upper() == 'OFFICE':
            for person in self.unallocated_people[room_type.upper()]:
                if person.name == person_name:
                    return {"person": person, "room": None}

        room_dict = self.get_dict(room_type.upper())
        for room in room_dict:
            if person_object in room_dict[room].allocation_list:
                return {"person": person_object, "room": room}
        return False


    #Method to unallocate someone from a room
    def unallocate_room(self, room_type, room_allocated, person_object):
        """
        Removes some one from the room in which he/ she was assigned
        :param room_type.upper()
        :param room_allocated
        :param person_object
        :return None
        """
        self.check_str(RoomType=room_type.upper(), RoomAllocated=room_allocated)
        room_dict = self.get_dict(room_type.upper())
        room_dict[room_allocated].allocation_list.remove(person_object)


    #Method to assign some one to a room
    def assign_individual_room(self, room_type, room_name, person_object):
        """
        Method assigns an individual to a room that has been specified
        :param room_type.upper()
        :param room_name
        :param person_object
        :return Boolean
        """
        self.check_str(RoomType=room_type.upper(), RoomName=room_name)
        room_dict = self.get_dict(room_type.upper())
        if not room_dict[room_name].is_room_assignable():
            self.unallocated_people[room_type.upper()].append(person_object)
            return False
        value = room_dict[room_name].add_person(person_object)
        return value



    #Method to reallocate someones room
    def reallocate_room(self, person_name, room_name):
        """
        Method that reallocates some one to a room that has been specified
        :param person_name
        :param room_name
        :return String or Boolean
        """
        self.check_str(RoomName=room_name, PersonName=person_name)
        #Get the room type
        room_type = self.get_room_type(room_name)
        room_dict = self.get_dict(room_type.upper())

        if room_dict[room_name].is_room_assignable:
            return self.reassign_room(room_type.upper(), room_name, person_name)

        if not room_dict[room_name].is_room_assignable:
            return 'The room specified is not assignable'

        return 'The room '+room_name+' does not exist'


    #Method for reassigning room
    def reassign_room(self, room_type, room_name, person_name):
        """
        Method that is used when reassigning some one to a room
        :param room_type.upper()
        :param room_name
        :param person_name
        """
        #Get room individual is assigned to
        returned_value = self.get_room_assigned(room_type.upper(), person_name)
        if not returned_value:
            return 'Check that the individual exists'

        if not returned_value['room']:
            self.assign_individual_room(room_type.upper(), room_name, returned_value['person'])
            return True

        self.unallocate_room(room_type.upper(), returned_value['room'], returned_value['person'])
        self.assign_individual_room(room_type.upper(), room_name, returned_value['person'])
        return True


    #Method to save the state of the data into a database
    def save_state(self, db_name):
        """
        Method that saves the data in the dictionaries and lists to the
        stated database
        :param db_name
        :return None
        """
        create_schema = CreateSchema(db_name)
        create_schema.save_state(
            self.office_dict,
            self.living_space_dict,
            self.staff_dict,
            self.fellow_dict
        )

    #Method to load data from the database
    def load_data(self, db_name):
        """
        Method that loads data from the stated database into the lists and
        dictionaries
        :param db_name
        :return None
        """
        create_schema = CreateSchema(db_name)
        offices = create_schema.load_offices()
        livingspaces = create_schema.load_living_space()
        staffs = create_schema.load_staff()
        fellows = create_schema.load_fellow()
        office_staff_alloc = create_schema.load_office_staff_allocations()
        office_fellow_alloc = create_schema.load_office_fellow_allocations()
        livingspaces_alloc = create_schema.load_living_space_allocations()
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


    #Method to check that the variable passed is a string type
    @classmethod
    def check_str(cls, **kwargs):
        """
        Method that helps check that the arguments passed are of type string
        :param kwargs
        :return None
        """
        for value in kwargs:
            if not isinstance(kwargs[value], str):
                raise TypeError(value+' must be of type string')


    #Method that is used to get a person if person exists in dictionaries
    def get_person(self, person_name):
        """
        Method that helps get the person object if the person name is in the
        staff or fellow dictionary
        :param person_name
        :return Object<type 'Person'> or Boolean
        """
        self.check_str(PersonName=person_name)

        for person in self.fellow_dict:
            if person == person_name:
                return self.fellow_dict[person]

        for person in self.staff_dict:
            if person == person_name:
                return self.staff_dict[person]

        return False

    #Method to get specific dictionary with the dojo class
    def get_dict(self, item_type):
        """
        Method returns a dictionary basing on the arguments passed
        :param item_type.upper()
        :return Dictionary
        """
        self.check_str(ItemType=item_type.upper())

        if item_type.upper() == "STAFF":
            return self.staff_dict

        if item_type.upper() == "FELLOW":
            return self.fellow_dict

        if item_type.upper() == "OFFICE":
            return self.office_dict

        if item_type.upper() == "LIVINGSPACE":
            return self.living_space_dict

        return False


    #Method to create an object basing on the arguments passed
    def create_item_object(self, item_type, item_name):
        """
        Method creates an object of type room or person basing on the argument
        passed and returns the object created
        :param item_type.upper()
        :param item_name
        :return Object<type 'Room'> or Object<type 'Person'> or False
        """
        self.check_str(ItemType=item_type.upper(), ItemName=item_name)

        if item_type.upper() == "STAFF":
            return Staff(item_name)

        if item_type.upper() == "FELLOW":
            return Fellow(item_name)

        if item_type.upper() == "OFFICE":
            return Office(item_name)

        if item_type.upper() == "LIVINGSPACE":
            return LivingSpace(item_name)

        return False


    #Method to add item to dict
    def add_object_to_dict(self, item_dict, item_type, item_name):
        """
        Method creates an object based on the item type passed and adds that object
        to the dictionary that is passed as item_dict
        :param item_dict
        :param item_type
        :param item_name
        :return Object or False
        """
        if item_type.upper() == "STAFF" or item_type.upper() == "FELLOW":
            not_in = item_name not in self.fellow_dict and item_name not in self.staff_dict
        elif item_type.upper() == "OFFICE" or item_type.upper() == "LIVINGSPACE":
            not_in = item_name not in self.office_dict and item_name not in self.living_space_dict
        else:
            raise ValueError('Item category must either be ROOM or PERSON')

        #Add a fellow and add to the fellow list
        if isinstance(item_dict, dict) and not_in:
            item_object = self.create_item_object(item_type.upper(), item_name)
            if item_object:
                item_dict[item_name] = item_object
                return item_object

            return False

        return False

    #Method to get list of allocations
    def get_allocations_for_room_category(self, room_type):
        """
        Method generates a dictionary containing the room allocations based on
        the room type provided
        :param room_type
        :param room_name
        :return dict
        """
        self.check_str(RoomType=room_type)
        room_dict = self.get_dict(room_type.upper())
        return {
            room_name:
            (room_dict[room_name].allocation_list)
            for room_name in room_dict
            if room_dict[room_name].allocation_list
        }


