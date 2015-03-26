from .card import Card


class NumberCard(Card):

    def _points(self):
        return int(self.rank), int(self.rank)
