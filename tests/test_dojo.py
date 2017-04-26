from unittest import TestCase
from app.controller.dojo import Dojo

class DojoTests(TestCase):
    def setUp(self):
        self.dojo = Dojo()
    def test_dojo_is_instance_of_Dojo(self):
        self.assertIsInstance(self.dojo, Dojo, "Object dojo is not an instance of class Dojo")