class Player:
    def __init__(self, name):
        self.name = name
        self.hand = Hand()

    def __str__(self):
        return self.name

    @staticmethod
    def choose_action():
        while True:
            choice = input("Do you want to hit or stand? (h/s): ")
            if choice.lower() == "h" or choice.lower() == "s":
                return choice.lower()
            else:
                print("Invalid choice. Please enter 'h' or 's'.")

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += card.value()
        if card.rank == "Ace":
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1