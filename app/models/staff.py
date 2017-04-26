#Import Person Class
from app.models.person import Person
#Let Staff Inherit Person Class
class Staff(Person):
    #Initialise the attributes of the Staff Class
    def __init__(self, name):
        position = "STAFF"
        #Make a call to base Class Person
        super(Staff, self).__init__(name, position)