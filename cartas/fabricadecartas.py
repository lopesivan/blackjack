# -*- coding: utf-8 -*-
from .ases import Ases
from .figura import Figura
from .numero import Numero
from .nipe import Nipe


class FabricaDeCartas(object):

    def numero(self, numero):
        self.class_, self.numero_str = {
            1: (Ases, 'A'),
            11: (Figura, 'J'),
            12: (Figura, 'Q'),
            13: (Figura, 'K'),
        }.get(numero, (Numero, str(numero)))
        return self

    def nipe(self, nipe):
        return self.class_(self.numero_str, nipe)

    def nipes(self):
        return Nipe('Paus', '♣'), \
            Nipe('Ouros', '♦'), \
            Nipe('Copas', '♥'), \
            Nipe('Espada', '♠')
