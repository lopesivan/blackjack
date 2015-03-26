# -*- coding: utf-8 -*-
from cards import Suit, CardFactory, Deck


def main():
    Club, Diamond, Heart, Spade = \
        Suit('Club', '♣'), \
        Suit('Diamond', '♦'), \
        Suit('Heart', '♥'), \
        Suit('Spade', '♠')

    card = CardFactory()
    deck = []
    for r in range(13):
        for s in (Club, Diamond, Heart, Spade):
            deck.append(card.rank(r + 1).suit(s))

    d = Deck(deck)
    print d

if __name__ == '__main__':
    main()
