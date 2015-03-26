class Hand:
    def __init__(self, dealer_card):
        self.dealer_card = dealer_card
        self.cards = []
    def hard_total(self):
        return sum(c.hard for c in self.cards)
    def soft_total(self):
        return sum(c.soft for c in self.cards)