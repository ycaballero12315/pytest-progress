import unittest
class TestClass(unittest.TestCase):

    def test_one(self):
        x = 'this'
        self.assertIn( 'h', x)
    
    def test_two(self):
        x = 'Hello'
        self.assertTrue(hasattr(x, 'some'))

class TestClassDemoInstance(unittest.TestCase):
    value = 0

    def test_add_value(self):
        self.value = 1
        self.assertEqual(self.value, 1)
    
    def test_add_scope(self):
        self.assertEqual(self.value, 1)