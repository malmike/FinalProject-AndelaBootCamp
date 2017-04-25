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

def setup_module():
    global transaction, connection, engine
    #Connect to a database and create a schema using a transaction
    engine = create_engine("sqlite://")
    transaction = engine.connect()
    connection = transaction.begin()
    Base.metadata.create_all(connection)

def teardown_module():
    #Rollback the top level transaction and disconnect from the database
    connection.Rollback()
    transaction.close()
    engine.dispose()

class DatabaseTest(TestCase):
    def setup():
        self.__transaction = connection.begin_nested()
        self.session = Session(connection)
    def teardown():
        self.session.close()
        self.__transaction.Rollback()

