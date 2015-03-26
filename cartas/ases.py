from .carta import Carta

class Ases(Carta):
    insure = True

    def _points(self):
        return 1, 11
