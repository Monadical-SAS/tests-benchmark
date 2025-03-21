import unittest
from my_exercise import my_function

class MyExerciseTest(unittest.TestCase):
    def test_basic_case(self):
        self.assertEqual(my_function(3, 4), 7)
    