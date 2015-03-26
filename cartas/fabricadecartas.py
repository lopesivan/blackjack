from .ases import Ases
from .figura import Figura
from .numero import Numero


class FabricaDeCartas(object):

    def rank(self, rank):
        self.class_, self.rank_str = {
            1: (Ases, 'A'),
            11: (Figura, 'J'),
            12: (Figura, 'Q'),
            13: (Figura, 'K'),
        }.get(rank, (Numero, str(rank)))
        return self

    def suit(self, suit):
        return self.class_(self.rank_str, suit)
