import unittest
from app.etl import load_data

class TestETL(unittest.TestCase):
    def test_load_data(self):
        load_data('data/tweets.json')
        # Add assertions to verify the data load process

if __name__ == '__main__':
    unittest.main()
