"""
    Usage:
        TheDojo create_room <room_type> <room_name>...
        TheDojo add_person <first_name> <last_name> <position> [<Y> | <N>]
        TheDojo print_room <room_name>
        TheDojo print_allocations [-o <filename>]
        TheDojo -h | --help
        TheDojo --version

    Options:
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


    def do_quit(self, arg):
        """Quit out of interactive dojo"""
        print('See ya!')
        exit()
        
opt = docopt(__doc__, sys.argv[1:])
#if opt['--interactive']:
TheDojo().cmdloop()

print(opt)
        
        