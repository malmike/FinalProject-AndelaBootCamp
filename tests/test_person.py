from unittest import TestCase
from app.models.person import Person
from app.models.fellow import Fellow
from app.models.stuff import Stuff

class PersonTests(TestCase):
    def setUp(self):
        self.name = 'malmike'
        self.position = 'fellow'
        self.person = Person(self.name, self.position)
        self.fellow = Fellow(self.name)
        self.stuff = Stuff(self.name)
    def test_person_instance(self):
        self.assertIsInstance(self.person, Person, "Object person is not an instance of class Person")
    def test_person_attributes(self):
        self.assertEqual(self.person.name, self.name, "The value that is passed into name and that returned, do not match")
        self.assertEqual(self.person.position, self.position, "The value that is passed into position and that returned, do not match")
    def test_fellow_inherits_person(self):
        self.assertTrue(issubclass(Fellow, Person), "Fellow class doesnot inherit from the Person class")
    def test_fellow_is_an_instance_of_Fellow(self):
        self.assertIsInstance(self.fellow, Fellow, "Object fellow is not an instance of the Fellow class")
    def test_name_attribute_in_fellow(self):
        self.assertEqual(self.fellow.name, self.name, "The value that is passed into name for fellow object and that returned, do not match")
    def test_fixed_attributes_in_fellow(self):
        self.asserEqual(self.fellow.position, 'FELLOW', "Fellow doesnot contain any attribute position")
    def test_stuff_inherits_person(self):
        self.assertTrue(issubclass(Stuff, Person), "Stuff class doesnot inherit from the Person class")
    def test_stuff_is_instance_of_Stuff(self):
        self.assertIsInstance(self.stuff, Stuff, "Object stuff is not an instance of class Stuff")
    def test_name_attribute_in_stuff(self):
        self.assertEqual(self.stuff.name, self.name, "The value that is passed into name for stuff object and that returned, do not match")
    def test_fixed_attributes_in_stuff(self):
        self.asserEqual(self.stuff.position, 'STUFF', "Stuff doesnot contain any attribute position")