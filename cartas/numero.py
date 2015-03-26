from .carta import Carta


class Numero(Carta):

    def _points(self):
        return int(self.numero), int(self.numero)
