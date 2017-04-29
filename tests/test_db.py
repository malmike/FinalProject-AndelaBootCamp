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
from app.database_methods.db_schema import DbSchema
from sqlalchemy import inspect


class DatabaseTest(TestCase):
    def setUp(self):
        self.db_schema = DbSchema()
        engine = create_engine("sqlite://")
        self.db_schema.metadata.create_all(engine)
        self.inspector = inspect(engine)

    def test_table_creation(self):
        table_names = self.inspector.get_table_names()
        self.assertTrue('fellow' in table_names, 'Table fellow not created')
        self.assertTrue('livingspace' in table_names, 'Table livingspace not created')
        self.assertTrue('staff' in table_names, 'Table staff not created')
        self.assertTrue('office' in table_names, 'Table office not created')
        self.assertTrue('livingspace_allocation' in table_names, 'Table livingspace_allocation not create')
        self.assertTrue('office_allocation' in table_names, 'Table office allocation not created')
