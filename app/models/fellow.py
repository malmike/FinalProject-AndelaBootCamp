#Import Person Class
from app.models.person import Person
#Let Fellow inherit the Person Class
class Fellow(Person):
    #Initialise the attributes of the Fellow Class
    def __init__(self, name):
        position = "FELLOW"
        #Make call to base class Person
        super(Fellow, self).__init__(name, position)