import unittest
from tests import test_person, test_room, test_add_room
from tests import test_add_person, test_dojo
from tests import test_allocations, test_reallocation
from tests import test_load_people, test_db

suite = unittest.TestLoader().loadTestsFromTestCase(
    test_person.PersonTests
)

suite.addTest(unittest.TestLoader().loadTestsFromTestCase(
    test_room.RoomTests
))

suite.addTest(unittest.TestLoader().loadTestsFromTestCase(
    test_add_room.AddRoomTests
))

suite.addTest(unittest.TestLoader().loadTestsFromTestCase(
    test_add_person.AddPersonTests
))

suite.addTest(unittest.TestLoader().loadTestsFromTestCase(
    test_dojo.DojoTests
))

suite.addTest(unittest.TestLoader().loadTestsFromTestCase(
    test_allocations.AllocationsTests
))

suite.addTest(unittest.TestLoader().loadTestsFromTestCase(
    test_reallocation.ReallocationsTests
))

suite.addTest(unittest.TestLoader().loadTestsFromTestCase(
    test_load_people.LoadPeopleTests
))

suite.addTest(unittest.TestLoader().loadTestsFromTestCase(
    test_db.DatabaseTest
))

unittest.TextTestRunner(verbosity=2).run(suite)
