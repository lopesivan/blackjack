# -*- coding: utf-8 -*-
from cartas import Nipe, FabricaDeCartas


def main():
    Club, Diamond, Heart, Spade = \
        Nipe('Club', '♣'), \
        Nipe('Diamond', '♦'), \
        Nipe('Heart', '♥'), \
        Nipe('Spade', '♠')

    carta = FabricaDeCartas()
    deck = []
    for r in range(13):
        for s in (Club, Diamond, Heart, Spade):
            deck.append(carta.rank(r + 1).suit(s))

    print deck

if __name__ == '__main__':
    main()
