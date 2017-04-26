from app.models.person import Person
class Fellow(Person):
    def __init__(self, name):
        position = "FELLOW"
        super(Fellow, self).__init__(name, position)