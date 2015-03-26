class Suit(object):

    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def __repr__(self):
        return self.symbol
