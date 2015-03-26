# -*- coding: utf-8 -*-
from cartas import Nipe, FabricaDeCartas


def main():
    Paus, Ouros, Copas, Espada = \
        Nipe('Paus', '♣'), \
        Nipe('Ouros', '♦'), \
        Nipe('Copas', '♥'), \
        Nipe('Espada', '♠')

    carta = FabricaDeCartas()
    deck = []
    for r in range(13):
        for s in (Paus, Ouros, Copas, Espada):
            deck.append(carta.rank(r + 1).suit(s))

    print deck

if __name__ == '__main__':
    main()
