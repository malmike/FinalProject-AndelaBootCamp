from unittest import TestCase

class DojoTests(TestCase):
    def setUp(self):
        self.dojo = Dojo()
    def test_dojo_is_instance_of_Dojo(self):
        self.assertIsInstance(self.dojo, Dojo)