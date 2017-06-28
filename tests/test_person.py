from unittest import TestCase
from app.models.person import Person
from app.models.fellow import Fellow
from app.models.staff import Staff

class PersonTests(TestCase):
    
    def setUp(self):
        self.name = 'malmike'
        self.position = 'fellow'
        self.person = Person(self.name)
        self.fellow = Fellow(self.name)
        self.staff = Staff(self.name)
    
    def test_person_instance(self):
        self.assertIsInstance(self.person, Person, "Object person is not an instance of class Person")
    
    def test_person_attributes(self):
        self.assertEqual(self.person.name, self.name, "The value that is passed into name and that returned, do not match")
    
    def test_fellow_inherits_person(self):
        self.assertTrue(issubclass(Fellow, Person), "Fellow class doesnot inherit from the Person class")
    
    def test_fellow_is_an_instance_of_Fellow(self):
        self.assertIsInstance(self.fellow, Fellow, "Object fellow is not an instance of the Fellow class")
    
    def test_name_attribute_in_fellow(self):
        self.assertEqual(self.fellow.name, self.name, "The value that is passed into name for fellow object and that returned, do not match")
    
    def test_fixed_attributes_in_fellow(self):
        self.assertEqual(self.fellow.position, 'FELLOW', "Fellow doesnot contain any attribute position")
    
    def test_staff_inherits_person(self):
        self.assertTrue(issubclass(Staff, Person), "Staff class doesnot inherit from the Person class")
    
    def test_staff_is_instance_of_Staff(self):
        self.assertIsInstance(self.staff, Staff, "Object staff is not an instance of class Staff")
    
    def test_name_attribute_in_staff(self):
        self.assertEqual(self.staff.name, self.name, "The value that is passed into name for staff object and that returned, do not match")
    
    def test_fixed_attributes_in_staff(self):
        self.assertEqual(self.staff.position, 'STAFF', "Staff doesnot contain any attribute position")