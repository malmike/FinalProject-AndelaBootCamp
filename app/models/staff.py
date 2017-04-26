#Import Person Class
from app.models.person import Person
#Let Staff Inherit Person Class
class Staff(Person):
    #Initialise the attributes of the Staff Class
    position = "STAFF"