#Import Person Class
from app.models.person import Person

#Let Fellow inherit the Person Class
class Fellow(Person):
    #Initialise the attributes of the Fellow Class
    position = "FELLOW"
    