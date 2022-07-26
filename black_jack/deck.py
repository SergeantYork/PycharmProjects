import random
from values import values, ranks, suits
from card import Card


class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                my_card = Card()
                my_card.rank = rank
                my_card.suit = suit
                self.deck.append(my_card)

    def __str__(self):
        deck_comp = ''  # start with an empty string
        for card in self.deck:
            deck_comp += '\n '+card.__str__() # add each Card object's print string
        return 'The deck has:' + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()


