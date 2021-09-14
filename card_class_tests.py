from card import *
import unittest


class TestCard(unittest.TestCase):

    def setUp(self):
        self.card1 = Card('Clubs', '7', False)
        self.card2 = Card('Spades', '7', True)
        self.card3 = Card('Hearts', 'K', False)
        self.card4 = Card('Spades', 'A', False)
        self.card5 = Card('Diamonds', '2', True)
        self.card6 = Card('Spades', 'A', False)
        self.card7 = Card('Hearts', '2', False)

    def test_equals(self):
        self.assertEqual(self.card1, self.card2)
        self.assertEqual(self.card4, self.card6)
        self.assertEqual(self.card5, self.card7)
        self.assertNotEqual(self.card1, self.card3)
        self.assertNotEqual(self.card2, self.card4)
        self.assertNotEqual(self.card2, self.card5)

    def test_sort_index(self):
        self.assertFalse(self.card1 > self.card2)
        self.assertFalse(self.card3 > self.card4)
        self.assertFalse(self.card6 < self.card5)
        self.assertFalse(self.card5 > self.card7)
        self.assertTrue(self.card6 > self.card3)
        self.assertTrue(self.card3 > self.card2)
        self.assertTrue(self.card5 < self.card4)


if __name__ == "__main__":
    unittest.main()
