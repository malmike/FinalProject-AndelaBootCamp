from abc import ABCMeta

class Person(object):
    __metaclass__ = ABCMeta
    #Initialise the attributes of the Person Class
    position = ""

    def __init__(self, name):
        self.name = name
