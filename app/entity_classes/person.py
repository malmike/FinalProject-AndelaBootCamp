from app.entity_classes.base import *
class Person(Base):
    __tablename__='person'
    name = Column(String(30), nullable=False, primary_key=True)
    position = Column(String(20), nullable=False)

    def __repr__(self):
        print ("Person<name:%r, position:%r>" % (self.name, self.position))

print (Person.__table__)