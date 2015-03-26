import random


class Deck(object):
    """ A simple Deck definition."""
    def __init__(self, cards):
        self._cards = cards
        random.shuffle(self._cards)

    def pop(self):
        return self._cards.pop()
