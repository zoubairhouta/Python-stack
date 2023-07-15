from classes.deck import Deck
from classes.player import Player


class BlackjackGame:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.player = Player("Player")
        self.dealer = Player("Dealer")

    @staticmethod
    def show_hand(player):
        print(f"{player}:")
        for card in player.hand.cards:
            print(card)
        print(f"Total value: {player.hand.value}")

    @classmethod
    def play(cls):
        print("Welcome to Blackjack!")

        game = cls()
        game.deal_initial_cards()

        cls.show_hand(game.player)
        cls.show_one_card(game.dealer)

        while True:
            choice = game.player.choose_action()
            if choice == "h":
                game.hit(game.player)
                cls.show_hand(game.player)
                if game.is_busted(game.player):
                    print("Player busts! You lose.")
                    break
            else:
                break

        if not game.is_busted(game.player):
            cls.show_hand(game.dealer)

            while game.dealer.hand.value < 17:
                game.hit(game.dealer)
                cls.show_hand(game.dealer)
                if game.is_busted(game.dealer):
                    print("Dealer busts! You win.")
                    break

            if not game.is_busted(game.dealer):
                game.compare_hands()

        print("\nThanks for playing!")

    def deal_initial_cards(self):
        for _ in range(2):
            self.hit(self.player)
            self.hit(self.dealer)

    def hit(self, player):
        card = self.deck.deal_card()
        if card:
            player.hand.add_card(card)
            player.hand.adjust_for_ace()

    @staticmethod
    def show_one_card(dealer):
        print("Dealer:")
        print("<card hidden>")
        print(dealer.hand.cards[1])

    @staticmethod
    def is_busted(player):
        return player.hand.value > 21

    def compare_hands(self):
        if self.player.hand.value > self.dealer.hand.value:
            print("Player wins!")
        elif self.player.hand.value < self.dealer.hand.value:
            print("Dealer wins!")
        else:
            print("It's a tie!")


BlackjackGame.play()
