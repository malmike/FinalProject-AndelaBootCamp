"""
    Usage:
        TheDojo start
        TheDojo create_room <room_type> <room_name>...
        TheDojo add_person <first_name> <last_name> <position> [<Y> | <N>]
        TheDojo print_room <room_name>
        TheDojo print_allocations [-o <filename>]
        TheDojo save_state [--db <sqlite_database>]
        TheDojo save_state <sqlite_database>
        TheDojo -h | --help
        TheDojo --version

    Options:
        --db         Specifies which database we are to use
        -o           Specifies whether to write the resulting values to a text file
        -h  --help   Show this screen.
        --version    Show version.


"""
import sys
import cmd
from docopt import docopt
from app.controller.dojo import Dojo
dojo = Dojo()

"""
This patch of code is to help docopt become interactive. It was got from:
https://github.com/docopt/docopt/blob/master/examples/interactive_example.py
"""
def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """
    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn

class TheDojo(cmd.Cmd):
    intro = 'Welcome to the Dojo Room Allocation Application!'\
        + '(type help for a list of commands)'
    prompt = '(TheDojo)'
    file = None

    @docopt_cmd
    def do_create_room(self, arg):
        """Usage: create_room <room_type> <room_name>..."""
        room_type = arg['<room_type>']
        room_names = arg['<room_name>']
        if isinstance(room_type, str):
            room_type = room_type.upper()
            if isinstance(room_names, str):
                value = dojo.create_room(room_type, room_name)
                if value:
                    print ("An "+ room_type.lower() +" called "+value.name+" has been successfully created!")
                else:
                    if room_type.upper() == "OFFICE" or room_type.upper() == "LIVINGSPACE":
                        print ( room_type.upper() +" "+ room_name+" already exists \ncreate_room <room_type> <room_name>...\n\n" )
                    else:
                        print ("RoomType is meant to be office or livingspace \main.py create_room <room_type> <room_name>...")
            else:
                for room_name in room_names:
                    value = dojo.create_room(room_type, room_name)
                    if value:
                        print ("An "+ room_type.lower() +" called "+value.name+" has been successfully created!")
                    else:
                        if room_type.upper() == "OFFICE" or room_type.upper() == "LIVINGSPACE":
                            print ( room_type.upper() +" "+ room_name+" already exists \ncreate_room <room_type> <room_name>...\n\n" )
                        else:
                            print ("RoomType is meant to be office or livingspace \main.py create_room <room_type> <room_name>...")
        else:
            raise TypeError("RoomType is meant to be a string \nmain.py create_room <room_type> <room_name>...")
    @docopt_cmd
    def do_add_person(self, arg):
        """Usage: add_person <first_name> <last_name> <position> [<Y> | <N>]"""
        first_name = arg['<first_name>']
        last_name = arg['<last_name>']
        position = arg['<position>']
        accomodation = arg['<Y>']
        name = first_name+" "+ last_name

        person_value = dojo.add_person(position.upper(), name)
        if person_value:
            print (position.capitalize() +" "+ name +" has been successfully added")
            office_value = dojo.allocate_rooms(person_value, 'OFFICE')
            if office_value:
                print (first_name.capitalize()+' has been allocated the office '+ office_value)
            else:
                print (first_name.capitalize()+' could not be allocated an office')
            if accomodation == "Y" and position.upper() == "FELLOW":
                living_space_value = dojo.allocate_rooms(person_value, 'LIVINGSPACE')
                if living_space_value:
                    print (first_name.capitalize()+' has been allocated the living space '+ living_space_value)
                else:
                    print (first_name.capitalize()+' could not be allocated living space')
        else:
            if position.upper() == "STAFF" or position.upper() == "FELLOW":
                print ( position.capitalize() +" "+ name+" already exists \nadd_person <first_name> <last_name> <position> [<Y> | <N>]\n\n" )
            else:
                print ("Position is meant to be staff or fellow \nadd_person <first_name> <last_name> <position> [<Y> | <N>]\n\n")
    
    @docopt_cmd
    def do_print_room(self, arg):
        """Usage: print_room <room_name>"""
        room_name = arg['<room_name>']
        allocation_list = dojo.room_occupants(room_name)
        if allocation_list:
            print ("OCCUPANTS OF THE ROOM "+ room_name.upper())
            for i in allocation_list:
                print ('-\t'+ i.name)
        else:
            print ("This room does not have any allocations or does not exist")


    @docopt_cmd
    def do_print_allocation(self, arg):
        """Usage: print_allocations [-o <filename>]"""
        test = arg ['-o']
        filename = arg['<filename>']
        allocations = dojo.get_allocations()
        if test:
            file = open(filename, "w")
            for i in allocations:
                file.write('\n'+str(i).upper()+'\n')
                r = 1
                for x in allocations[i]:
                    if r < len(allocations[i]):
                        file.write(str(x.name)+', ')
                    else:
                        file.write(str(x.name)+ '\n')
                    r += 1
                file.write('---------------------------------------------')
            file.close()
        else:
            for i in allocations:
                print ('\n'+str(i).upper())
                r = 1
                for x in allocations[i]:
                    if r < len(allocations[i]):
                        print (str(x.name), end=', ')
                    else:
                        print (str(x.name))
                    r += 1
                print('---------------------------------------------')
    
    @docopt_cmd
    def do_save_state(self, arg):
        """Usage: save_state [--db <sqlite_database>]"""
        db = arg['--db']
        sqlite_database = arg['<sqlite_database>']
        create_schema = None
        if db and sqlite_database:
            dojo.save_state(sqlite_database)
        else:
            dojo.save_state('')
    
    @docopt_cmd
    def do_load_state(self, arg):
        """Usage: save_state <sqlite_database>"""
        sqlite_database = arg['<sqlite_database>']
        dojo.load_data(sqlite_database)
    
    @docopt_cmd
    def do_start(self, arg):
        """Usage: start"""
        pass

    def do_quit(self, arg):
        """Quit out of interactive dojo"""
        print('See ya!')
        exit()
        
opt = docopt(__doc__, sys.argv[1:])
#if opt['--interactive']:
TheDojo().cmdloop()

print(opt)
        
        