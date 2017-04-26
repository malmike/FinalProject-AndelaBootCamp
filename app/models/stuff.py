from app.models.person import Person
class Stuff(Person):
    def __init__(self, name):
        position = "STUFF"
        super(Stuff, self).__init__(name, position)