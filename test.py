import unittest


class TestStringMethods(unittest.TestCase):

    """
    https://docs.python.org/3/library/unittest.html
    """
    
    @classmethod
    def setUpClass(cls):
        print('---> before all...')

    @classmethod
    def tearDownClass(cls):
        print('---> after all...')

    # before each test
    def setUp(self):
        print('setting up...')

    # after each test
    def tearDown(self):
        print('tearing down...')

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    @unittest.skip("showing skipping")
    def test_is_upper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])

        with self.assertRaises(TypeError):
            s.split(2)



if __name__ == '__main__':
    unittest.main()