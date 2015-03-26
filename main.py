from cartas import FabricaDeCartas


def main():
    carta = FabricaDeCartas()
    deck = []
    for r in range(13):
        for s in (carta.nipes()):
            deck.append(carta.numero(r + 1).nipe(s))

    print deck
    print len(deck)
    print deck[1]
    print repr(deck[1])


if __name__ == '__main__':
    main()
