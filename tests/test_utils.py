import unittest
import os
from src.utils import ensure_dir

class TestUtils(unittest.TestCase):

    def setUp(self):
        self.test_dir = 'data/test_dir'

    def tearDown(self):
        if os.path.exists(self.test_dir):
            os.rmdir(self.test_dir)

    def test_ensure_dir(self):
        ensure_dir(self.test_dir)
        self.assertTrue(os.path.exists(self.test_dir))
        self.assertTrue(os.path.isdir(self.test_dir))

if __name__ == '__main__':
    unittest.main()
