# tests/test_utils.py
import unittest
from app.utils import clean_text, score_tweet

class TestUtils(unittest.TestCase):
    def test_clean_text(self):
        self.assertEqual(clean_text(" Hello World "), "hello world")
        self.assertEqual(clean_text("PYTHON"), "python")
        self.assertEqual(clean_text("  Data Science  "), "data science")

    def test_score_tweet(self):
        self.assertEqual(score_tweet("This is a tweet"), 15)
        self.assertEqual(score_tweet("Short"), 5)
        self.assertEqual(score_tweet(""), 0)

if __name__ == '__main__':
    unittest.main()
