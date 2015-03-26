class Card(object):
    insure = False

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.hard, self.soft = self._points()

    def __eq__(self, other):
        return (self.suit == other.suit and
                self.rank == other.rank and
                self.hard == other.hard and
                self.soft == other.soft)

    def __repr__(self):
        return "{__class__.__name__}(suit={suit!r}, rank={rank!r})".format(__class__=self.__class__, **self.__dict__)

    def __str__(self):
        return "{rank}{suit}".format(**self.__dict__)
