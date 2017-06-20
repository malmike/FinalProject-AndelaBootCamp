from sqlalchemy import create_engine
from app.database_methods.db_schema import DbSchema
from sqlalchemy import select

class CreateSchema(object):
    def __init__(self, dbname):
        self.db_schema = DbSchema()
        if dbname == '':
            print ('here')
            self.engine = create_engine("sqlite://")
        else:
            self.engine = create_engine("sqlite:///"+dbname)
        self.db_schema.metadata.create_all(self.engine)
        self.conn = self.engine.connect()

    def save_state(self, office_dict, living_space_dict, staff_dict, fellow_dict):
        print ('Add Offices To Db')
        if len(office_dict) > 0:
            for i in office_dict:
                print (i)
                insert_stmt = self.db_schema.office.insert().values(name=i)
                print(insert_stmt)
                result = self.conn.execute(insert_stmt)
                print ('Resulting primary key: '+ str(result.inserted_primary_key))
        print ('\nAdd Living Space To Db')
        if len(living_space_dict) > 0:
            for i in living_space_dict:
                insert_stmt = self.db_schema.livingspace.insert().values(name=i)
                result = self.conn.execute(insert_stmt)
                print ('Resulting primary key: '+ str(result.inserted_primary_key))
        print ('\nAdd Staff To Db')
        if len(staff_dict) > 0:
            for i in staff_dict:
                insert_stmt = self.db_schema.staff.insert().values(name=i)
                result = self.conn.execute(insert_stmt)
                print ('Resulting primary key: '+ str(result.inserted_primary_key))
        print ('\nAdd Fellows To Db')
        if len(fellow_dict) > 0:
            for i in fellow_dict:
                insert_stmt = self.db_schema.fellow.insert().values(name=i)
                result = self.conn.execute(insert_stmt)
                print ('Resulting primary key: '+ str(result.inserted_primary_key))
        print ('\nAdd Fellows Allocations In Living Space To Living Space Allocations Table')
        for i in living_space_dict:
            if len(living_space_dict[i].allocation_list) > 0:
                for fellow in living_space_dict[i].allocation_list:
                    insert_stmt = self.db_schema.livingspace_allocation.insert().values(fellow_name=fellow.name, livingspace_name=i)
                    result = self.conn.execute(insert_stmt)
                    print ('Resulting primary key: '+ str(result.inserted_primary_key))
        print ("\nAdd Fellows And Staff In The Offices To Office Allocations Table")
        for i in office_dict:
            if len(office_dict[i].allocation_list) > 0:
                for person in office_dict[i].allocation_list:
                    if person.position == "FELLOW":
                        insert_stmt = self.db_schema.office_allocation.insert().values(fellow_name=person.name, office_name=i)
                    else:
                        insert_stmt = self.db_schema.office_allocation.insert().values(staff_name=person.name, office_name=i)
                    result = self.conn.execute(insert_stmt)
                    print ('Resulting primary key: '+ str(result.inserted_primary_key)) 

    def load_offices(self):
        #office table
        select_stmt = select([self.db_schema.office.c.name])
        result = self.conn.execute(select_stmt).fetchall()
        return result

    def load_living_space(self):
        select_stmt = select([self.db_schema.livingspace.c.name])
        result = self.conn.execute(select_stmt).fetchall()
        return result

    def load_staff(self):
        select_stmt = select([self.db_schema.staff])
        result = self.conn.execute(select_stmt).fetchall()
        return result

    def load_fellow(self):
        select_stmt = select([self.db_schema.fellow])
        result = self.conn.execute(select_stmt).fetchall()
        return result

    def load_office_staff_allocations(self):
        select_stmt = select([self.db_schema.office_allocation]).where(self.db_schema.office_allocation.c.fellow_name == None)
        result = self.conn.execute(select_stmt).fetchall()
        return result

    def load_office_fellow_allocations(self):
        select_stmt = select([self.db_schema.office_allocation]).where(self.db_schema.office_allocation.c.staff_name == None)
        result = self.conn.execute(select_stmt).fetchall()
        return result

    def load_office_allocations(self):
        select_stmt = select([self.db_schema.office_allocation])
        result = self.conn.execute(select_stmt).fetchall()
        return result
        
    def load_living_space_allocations(self):
        select_stmt = select([self.db_schema.livingspace_allocation])
        result = self.conn.execute(select_stmt).fetchall()
        return result

            

