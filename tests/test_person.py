from unittest import TestCase

class PersomTests(TestCase):
    def setUp(self):
        self.name = 'malmike'
        self.position = 'fellow'
        self.person = Persom(self.name, self.position)
        self.fellow = Fellow(self.name)
        self.stuff = Stuff(self.name)
    def test_person_instance(self):
        self.assertIsInstance(self.person, Persom, "Object person is not an instance of class Persom")
    def test_person_attributes(self):
        self.assertEqual(self.person.name, self.name, "The value that is passed into name and that returned, do not match")
        self.assertEqual(self.person.position, self.position, "The value that is passed into position and that returned, do not match")
