from sqlalchemy import MetaData
from sqlalchemy import Table, Column
from sqlalchemy import Integer, String
from sqlalchemy import ForeignKey
"""
These are file meant to allow mapping of the database tables to the class
It is using sqlalchemy as an orm for the attributes to tables in the database
"""

class DbSchema(object):
    def __init__(self):
        #Mapping variables to the database tables
        self.metadata = MetaData()
        self.office = Table('office', self.metadata, Column('name', String, primary_key=True))
        self.livingspace = Table('livingspace', self.metadata, Column('name', String, primary_key=True))
        self.staff = Table('staff', self.metadata, Column('name', String, primary_key=True))
        self.fellow = Table('fellow', self.metadata, Column('name', String, primary_key=True))
        self.office_allocation = Table('office_allocation', self.metadata, 
            Column('id', Integer, primary_key=True), 
            Column('staff_name', String, ForeignKey('staff.name')),
            Column('fellow_name', String, ForeignKey('fellow.name')),
            Column('office_name', String, ForeignKey('office.name'))            
            )
        self.livingspace_allocation = Table('livingspace_allocation', self.metadata, 
            Column('id', Integer, primary_key=True), 
            Column('fellow_name', String, ForeignKey('fellow.name')),
            Column('livingspace_name', String, ForeignKey('livingspace.name'))            
            )

        

