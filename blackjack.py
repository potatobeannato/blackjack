import random

# Type of card for the deck


class LuxCard:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return "of".join((self.value, self.suit))

# Building a deck and making it shuffle and deal


class LuxDeck:
    def __init__(self):
        self.cards = [LuxCard(s, v) for s in [" Spades ", " Clubs ", " Hearts ", " Diamonds "] for v in [
            " A ", " 2 ", " 3 ", " 4 ", " 5 ", " 6 ", " 7 ", " 8 ", " 9 ", " 10 ", " J ", " Q ", " K "]]

    def shuffle(self):
        if len(self.cards) > 1:
            random.shuffle(self.cards)

    def deal(self):
        if len(self.cards) > 1:
            return self.cards.pop(0)

# Making the dealer hand and players hands and to calculate the total value
# To make an ace value class to be seperate from other values


class LuxHand:
    def __init__(self, dealer=False):
        self.dealer = dealer
        self.cards = []
        self.value = 0

    def add_card(self, card):
        self.cards.append(card)

    def calculate_cardvalue(self):
        self.value = 0
        has_ace = False
        for card in self.cards:
            if card.value.isnumeric():
                self.value += int(card.value)
            else:
                if card.value == "A":
                    has_ace = True
                    self.value += 11
                else:
                    self.value += 10
        if has_ace and self.value > 21:
            self.value -= 10

    def get_cardvalue(self):
        self.calculate_cardvalue()
        return self.value

    def display_card(self):
        if self.dealer:
            print(" hidden ")
            print(self.cards[1])
        else:
            for card in self.cards:
                print(card)
            print("Value: ", self.get_cardvalue())

# Start to play the game. Make sure to have the deck shuffle, see the player hand and dealer hand
# Dealer hand have to be hidden, need to compare dealer and player hand. Display the hand as well
# Check to see if player and dealer has blackjack or not
# Ask player if they want to hit or stay
# Display loser for both player and dealer same with winner
# After game is over check to see if player want to play again or not


class Game:
    def __init__(self):
        pass

    def play(self):
        playing = True

        while playing:
            self.deck = LuxDeck()
            self.deck.shuffle()

            self.my_hand = LuxHand()
            self.theBoss_hand = LuxHand(dealer=True)

            for i in range(2):
                self.my_hand.add_card(self.deck.deal())
                self.theBoss_hand.add_card(self.deck.deal())

            print("My hand is: ")
            self.my_hand.display_card()
            print()
            print("Boss's hand is: ")
            self.theBoss_hand.display_card()
            game_over = False

            while not game_over:
                my_blackjack, theBoss_blackjack = self.check_blackjack()
                if my_blackjack or theBoss_blackjack:
                    game_over = True
                    self.get_result_blackjack(
                        my_blackjack, theBoss_blackjack)
                    continue

                option = input("Would you like to [Hit Me / Stay] ").lower()
                while option not in ["h", "s", "hit", "stay"]:
                    option = input(
                        "Please enter 'hit' or 'stay' (or H/S) ").lower()

                if option in ['hit', 'h']:
                    self.my_hand.add_card(self.deck.deal())
                    self.my_hand.display_card()
                    if self.player_gone_over():
                        print("OH NO! You gone gone over! Loser! ")
                        game_over = True
                else:
                    myhand_value = self.my_hand.get_cardvalue()
                    bosshand_value = self.theBoss_hand.get_cardvalue()
                    print("Last Stand")
                    print("Your hand: ", myhand_value)
                    print("Boss's hand: ", bosshand_value)

                    if myhand_value > bosshand_value:
                        print("That's Wild you Win!!")
                    elif myhand_value == bosshand_value:
                        print("Lucky, you tied!")
                    else:
                        print("Dealer beat you, Loser!")
                    game_over = True

                    again = input("Would you like to play again? [Y/N]")
                    while again.lower() not in ["y", "n"]:
                        again = input("Enter Y or N now!")
                    if again.lower() == "n":
                        print(
                            "Thanks for playing! Do come again when you want more money")
                        playing = False
                    else:
                        game_over = False

# This is the class for checking blackjack result for both dealer and player
# Check to see if they will have a tie or not
    def check_blackjack(self):
        player = False
        dealer = False
        if self.my_hand.get_cardvalue() == 21:
            player = True
        if self.theBoss_hand.get_cardvalue() == 21:
            dealer = True

        return player, dealer

    def get_result_blackjack(self, my_blackjack, theBoss_blackjack):
        if my_blackjack and theBoss_blackjack:
            print("This is a draw! Both boss and mee has blackjack!")

        elif my_blackjack:
            print("Blackjack! Winner winner chicken dinner!")

        elif theBoss_blackjack:
            print("Blackjack! Boss wins, now hand over your money!")

    def player_gone_over(self):
        return self.my_hand.get_cardvalue() > 21


game = Game()
game.play()
