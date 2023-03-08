import unittest
from unittest.mock import Mock
from .model import Card

class TestCard(unittest.TestCase):
    def setUp(self):
        self.card1 = Card(10, 'H')
        self.card2 = Card(10, 'D')
        self.card3 = Card('K', 'S')
        self.card4 = Card('A', 'C')

    def test_eq(self):
        self.assertIs(self.card1.__eq__(self.card2), True)
        self.assertIs(self.card1.__eq__(self.card3), False)
        self.assertIs(self.card3.__eq__(self.card4), False)

    def test_ne(self):
        self.assertIs(self.card1.__ne__(self.card2), False)
        self.assertIs(self.card1.__ne__(self.card3), True)
        self.assertIs(self.card3.__ne__(self.card4), True)

    def test_lt(self):
        self.assertIs(self.card1.__lt__(self.card3), True)
        self.assertIs(self.card4.__lt__(self.card3), True)
        self.assertIs(self.card2.__lt__(self.card4), True)
        self.assertIs(self.card1.__lt__(self.card1), False)
        self.assertIs(self.card3.__lt__(self.card2), False)

    def test_le(self):
        self.assertIs(self.card1.__le__(self.card2), True)
        self.assertIs(self.card3.__le__(self.card3), True)
        self.assertIs(self.card1.__le__(self.card3), True)
        self.assertIs(self.card3.__le__(self.card2), False)

    def test_gt(self):
        self.assertIs(self.card3.__gt__(self.card1), True)
        self.assertIs(self.card3.__gt__(self.card4), True)
        self.assertIs(self.card4.__gt__(self.card2), True)
        self.assertIs(self.card1.__gt__(self.card1), False)
        self.assertIs(self.card2.__gt__(self.card3), False)

    def test_ge(self):
        self.assertIs(self.card2.__ge__(self.card1), True)
        self.assertIs(self.card3.__ge__(self.card3), True)
        self.assertIs(self.card3.__ge__(self.card1), True)
        self.assertIs(self.card2.__ge__(self.card3), False)

    def test_sort(self):
        # Create a list of mock cards with random values and suits
        cards = [Mock(spec=Card, value=random.randint(2, 14), suit=random.choice('shdc')) for _ in range(10)]

        # Sort the list using the Card comparison methods
        cards.sort()

        # Check that the sorted list is in ascending order
        self.assertCountEqual(cards, sorted(cards))

if __name__ == '__main__':
    unittest.main()
