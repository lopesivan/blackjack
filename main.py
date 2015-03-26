from cartas import FabricaDeCartas
from cartas import Deck


def main():
    carta = FabricaDeCartas()
    cartas = []
    for r in range(13):
        for s in (carta.nipes()):
            cartas.append(carta.numero(r + 1).nipe(s))

    deck = Deck(cartas)

    print deck.pop()
    print deck.len()
    print deck.pop()
    print deck.len()

    print cartas
    print len(cartas)
    print cartas[1]
    print repr(cartas[1])


if __name__ == '__main__':
    main()
