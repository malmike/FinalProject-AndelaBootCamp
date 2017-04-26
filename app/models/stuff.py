#Import Person Class
from app.models.person import Person
#Let Stuff Inherit Person Class
class Stuff(Person):
    #Initialise the attributes of the Stuff Class
    def __init__(self, name):
        position = "STUFF"
        #Make a call to base Class Person
        super(Stuff, self).__init__(name, position)