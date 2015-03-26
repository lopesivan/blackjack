from .acecard import AceCard
from .facecard import FaceCard
from .numbercard import NumberCard


class CardFactory(object):

    def rank(self, rank):
        self.class_, self.rank_str = {
            1: (AceCard, 'A'),
            11: (FaceCard, 'J'),
            12: (FaceCard, 'Q'),
            13: (FaceCard, 'K'),
        }.get(rank, (NumberCard, str(rank)))
        return self

    def suit(self, suit):
        return self.class_(self.rank_str, suit)
