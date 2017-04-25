from app.entity_classes.base import *
class Room(Base):
    __tablename__='room'
    name = Column(String(30), nullable=False, primary_key=True)
    capacity = Column(Integer, nullable=False)
    description = Column(String(20), nullable=False)

    def __repr__(self):
        print ("Room<name:%r, capacity:%r, description:%r>" % (self.name, self.capacity, self.description))

print (Room.__table__)