# Make sure you have an empty database for unit testing
# Create the engine, create one connection and start a transaction in it
# Create the tables
# Optionally, insert test fixtures
# For every test, repeat:
    # Create a savepoint
    # Run the test
    # Roll back to the savepoint
    # Roll back the transaction


from unittest import TestCase
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from app.entity_classes.base import *
from app.entity_classes.room import Room

def setup_module():
    global engine
    #Connect to a database and create a schema using a transaction
    engine = create_engine("sqlite://")
    Base.metadata.create_all(engine)


class DatabaseTest(TestCase):
    def setUp(self):
        self.session = Session(bind=engine)
    def tearDown(self):
        self.session.rollback()
    def room_test(self):
        room = Room(name='orange', capacity=6, description='LIVINGSPACE')
        self.session.add(room)
        test_table_room = room in self.session
        self.assertTrue(test_table_room, "Room not added to the sqlalchemy session")
        self.session.commit()
        item = room.name
        self.assertEqual('orange', item, "The room has not been commited to the database")
        num_db_entries = self.session.query(Room).filter(Room.name=='orange').count()
        self.assertEqual(1, num_db_entries, "Multiple entries of room are existing in the database")

    def person_test(self):
        person = Person(name='malmike', position='FELLOW')
        self.session.add(person)
        test_table_person = person in self.session
        self.assertTrue(test_table_person, "Person not added to the sqlalchemy session")
        self.session.commit()
        item = person.name
        self.assertEqual('malmike', item, "The person has not been commited to the database")
        num_db_entries = self.session.query(Room).filter(Room.name=='malmike').count()
        self.assertEqual(1, num_db_entries, "Multiple entries of person are existing in the database")


