import random


class Deck(object):
    """ A simple Deck definition."""
    def __init__(self, cartas):
        self._cartas = cartas
        random.shuffle(self._cartas)

    def pop(self):
        return self._cartas.pop()
