from .card import Card

class AceCard(Card):
    insure = True

    def _points(self):
        return 1, 11
