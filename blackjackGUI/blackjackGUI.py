import random
from tkinter import *

# Card class will represent a single card out of the deck
class Card:

    def __init__(self, suit, value):
        self.suit = suit # Spades, Clubs, Hearts or Diamonds
        self.value = value # The value of the card

    # How the Card object will be represented
    def __repr__(self):
        offset = int(self.suit)
        index = 0

        # Changing the value to a numeric value
        if self.value.isnumeric():
            index = int(self.value)
        elif self.value == 'A':
            index = 1
        elif self.value == 'J':
            index = 11
        elif self.value == 'Q':
            index = 12
        elif self.value == 'K':
            index = 13

        # Return the path to the image of the card
        return 'images/' + str(index + offset) + '.gif'

# Deck class will represent the deck used for the game
class Deck:

    def __init__(self):
        # Spades = 0, Hearts = 13, Diamonds = 26 and Clubs = 39
        self.cards = [Card(s, v) for s in ['0', '13', '26', '39'] 
                    for v in ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'J', 'Q', 'K']]

    def shuffle(self):
        random.shuffle(self.cards)

    # Pop the top card to give to the player
    def deal(self):
        if len(self.cards) > 0:
            return self.cards.pop()

# Hand class will represent the player's hand or the dealer's hand
class Hand:

    def __init__(self, is_dealer = False):
        self.is_dealer = is_dealer # Default value is false
        self.cards = [] # The list that will contain the cards to be played with
        self.cards_img = [] # The list that will contain the images of the cards
        self.index = 0 # index of the image to be displayed
        self.value = 0 # The value of the hand

    def add_card(self, card):
        self.cards.append(card) # Add a card to the hand

    def calculate(self):
        self.value = 0 # Always reset the value of the Hand
        ace = False
        for card in self.cards:
            if card.value.isnumeric():
                self.value += int(card.value) 
            else: # Translate the value of face cards to ints
                if card.value == 'A':
                    ace = True
                    self.value += 11
                else:
                    self.value += 10

        # If player has an ace and the hand is over 21
        # change the value of the ace to 1
        if ace and self.value > 21:
            self.value -= 10

        return self.value

class GameGUI:

    def __init__(self):
        self.window = Tk()
        self.window.title('Blackjack')

        # Create the green canvas where the cards will be placed
        self.canvas = Canvas(self.window, width = 600, height = 600, bg = 'green')
        self.canvas.grid(row = 0, column = 0)
        
        # Draw the "Deck" on the canvas
        self.img = PhotoImage(file = 'images/back.gif')
        image = self.canvas.create_image(500, 100, image = self.img)

        # Draw the frame where the buttons will be
        self.frame = Frame(self.window, width = 600, height = 100, bg = 'red')
        self.frame.grid(row = 1, column = 0)

        # Variable for game with two players
        self.two_players = False
        self.placeButtons()

        self.window.mainloop()

    # Function to place the quit and play buttons in the red frame
    def placeButtons(self):
        self.play = Button(self.frame, width = 15, text = 'Play Round', command = self.playRound)
        self.multiplayer = Button(self.frame, width = 15, text = '2 Player Game', command = self.twoPlayers)
        self.quit = Button(self.frame, width = 15, text = 'Quit', command = self.window.destroy)
        self.play.place(x = 45, y = 40)
        self.multiplayer.place(x = 245, y = 40)
        self.quit.place(x = 445, y = 40)
    
    # Function to destroy the quit and play buttons in the red frame
    # to make space for the hit and stick buttons for the game
    def destroyButtons(self):
        self.play.destroy()
        self.quit.destroy()
        self.multiplayer.destroy()

    # Animate the cards to go to the player (not animated yet)
    def animate_player_deal(self):
        # Get path to the image files create images on the canvas 
        # increase the image index and move image to corresponding position
        self.player.cards_img.append(PhotoImage(file = self.player.cards[self.player.index]))
        image = self.canvas.create_image(500, 100, image = self.player.cards_img[self.player.index])
        self.canvas.move(image, -400 + (self.player.index * 25), 400)
        self.player.index += 1

    # Animate the cards to go to the player 2 (not animated yet)
    def animate_player_2_deal(self):
        # Get path to the image files create images on the canvas 
        # increase the image index and move image to corresponding position
        self.player_2.cards_img.append(PhotoImage(file = self.player_2.cards[self.player_2.index]))
        image = self.canvas.create_image(500, 100, image = self.player_2.cards_img[self.player_2.index])
        self.canvas.move(image, -50 + (self.player_2.index * 25), 400)
        self.player_2.index += 1

    # Animate the cards to go to the dealer (not animated yet)
    def animate_dealer_deal(self):
        # For the first card, the back image is used in order to hide
        # the value of the card to the player(s)
        if self.dealer.index == 0:
            self.dealer.cards_img.append(PhotoImage(file = self.dealer.cards[self.dealer.index]))
            self.image = self.canvas.create_image(500, 100, image = self.img)
            self.canvas.move(self.image, -400, 0)
            self.dealer.index += 1
        # Get path to the image files create images on the canvas
        # increase the image index and move image to corresponding position
        else:
            self.dealer.cards_img.append(PhotoImage(file = self.dealer.cards[self.dealer.index]))
            image2 = self.canvas.create_image(500, 100, image = self.dealer.cards_img[self.dealer.index])
            self.canvas.move(image2, -400 + (self.dealer.index * 25), 0)
            self.dealer.index += 1

    def playRound(self):
        self.var = IntVar() # Variable to wait for player1
        self.var2 = IntVar() # Variable to wait for player2

        self.canvas.delete('all') # Clean canvas for game
        image = self.canvas.create_image(500, 100, image = self.img) # Place the deck on the top right corner
        self.destroyButtons()
        # Buttons to be used for the game for either one player or two players
        if self.two_players:
            hit1 = Button(self.frame, width = 15, text = 'Hit', command = self.hit)
            stick1 = Button(self.frame, width = 15, text = 'Stick', command = self.stick)
            hit2 = Button(self.frame, width = 15, text = 'Hit', command = self.hit_2)
            stick2 = Button(self.frame, width = 15, text = 'Stick', command = self.stick_2)
            hit1.place(x = 85, y = 15)
            stick1.place(x = 85, y = 55)
            hit2.place(x = 385, y = 15)
            stick2.place(x = 385, y = 55)
        else:
            hit = Button(self.frame, width = 15, text = 'Hit', command = self.hit)
            stick = Button(self.frame, width = 15, text = 'Stick', command = self.stick)
            hit.place(x = 85, y = 40)
            stick.place(x = 385, y = 40)

        self.deck = Deck() # Create a deck
        self.deck.shuffle() # Shuffle the deck

        self.player = Hand() # Player's hand
        self.dealer = Hand(is_dealer = True) # Dealer's hand
        if self.two_players:
            self.player_2 = Hand() # Second player's hand


        # Give cards to dealer and player and animate on to the canvas
        for i in range(2):
            self.player.add_card(self.deck.deal())
            self.animate_player_deal()
            self.dealer.add_card(self.deck.deal())
            self.animate_dealer_deal()
            if self.two_players:
                self.player_2.add_card(self.deck.deal())
                self.animate_player_2_deal()

        self.over = False # Variable for infinite loop

        while not self.over:
            if self.checkBlackjack(): # If player or dealer have black jack, the game is over
                self.showBlackjackResults() # Show the blackjack results
                break
            else:
                if not self.bust(): # IF player1 is over 21, do not wait for their input
                    self.window.wait_variable(self.var) # Wait for player1 input
                if self.two_players:
                    if not self.bust_2(): # If player2 is over 21, do not wait for their input
                        self.window.wait_variable(self.var2) # Wait for player2 input

                # Dealer hits only until his total is 17 or higher
                if self.dealer.calculate() < 17:
                    self.dealer.add_card(self.deck.deal())
                    self.animate_dealer_deal()
                
                if not self.two_players:  
                    if self.bust(): # If the player goes over 21 the game is over
                        self.canvas.create_text(300, 300, fill = 'white', font = 'Times 30 bold', text = 'Bust! \nYou have lost')
                        break
                    else:
                        continue
                else:
                    if self.bust() and self.bust_2():
                        self.canvas.create_text(300, 300, fill = 'white', font = 'Times 30 bold', text = 'Bust! \nYou both have lost')
                        break
                    else:
                        if self.bust():
                            self.canvas.create_text(100, 400, fill = 'white', font = 'Times 30 bold', text = 'Bust!')
                        if self.bust_2():
                            self.canvas.create_text(500, 400, fill = 'white', font = 'Times 30 bold', text = 'Bust!')
                    continue

        # Replace hit and stick buttons with original Menu for either
        # two players or one player
        if self.two_players:
            hit1.destroy()
            stick1.destroy()
            hit2.destroy()
            stick2.destroy()
        else:
            hit.destroy()
            stick.destroy()
        self.placeButtons()

        self.canvas.itemconfig(self.image, image = self.dealer.cards_img[0]) # Revealing the hidden card at the end

        # If Blackjack, exit out of the function to avoid calling showResults()
        if self.two_players:
            if (self.bust() and self.bust_2()) or self.checkBlackjack():
                return
        else:
            if self.bust() or self.checkBlackjack():
                return

        self.showResults()

    # Function to set up 2 player game
    def twoPlayers(self):
        self.two_players = True
        self.playRound()

    def stick(self):
        self.var.set(1)
        self.over = True # Playing the the cards in hand

    def stick_2(self):
        self.var2.set(1)
        self.over = True # Playing the cards in hand

    def hit(self):
        self.player.add_card(self.deck.deal()) # Add an extra card to the player's hand
        self.animate_player_deal() # Animate the extra card
        self.over = False # Make sure the game keeps going if other player sticks
        self.var.set(1)

    def hit_2(self):
        self.player_2.add_card(self.deck.deal()) # Add an extra card to the player 2 hand
        self.animate_player_2_deal() # Animate the extra card
        self.over = False # Make sure the game keeps going if the other player sticks
        self.var2.set(1)

    # Function to check for blackjack
    def checkBlackjack(self):
        # If either the player or the dealer have blackjack
        # return True otherwise False and the game continues
        if self.two_players:
            if self.player.calculate() == 21 or self.player_2.calculate() == 21 or self.dealer.calculate() == 21:
                return True
        else:
            if self.player.calculate() == 21 or self.dealer.calculate() == 21:
                return True
        
        return False

    # Function to check if the player has gone over 21
    def bust(self):
        return self.player.calculate() > 21

    # Function to check if dealer has gone over 21
    def bust_dealer(self):
        return self.dealer.calculate() > 21

    # Function to check if they player 2 has gone over 21
    def bust_2(self):
        return self.player_2.calculate() > 21

    def showBlackjackResults(self):
        self.canvas.itemconfig(self.image, image = self.dealer.cards_img[0]) # Revealing the hidden card at the end

        # Print out the result of the game
        if self.two_players:
            if self.player.calculate() == 21 and self.dealer.calculate() == 21 and self.player_2.calculate() == 21:
                self.canvas.create_text(300, 300, fill = 'white', font = 'Times 30 bold', text = 'All have Blackjack!')
            elif self.player.calculate() == 21 and self.player_2.calculate() == 21:
                self.canvas.create_text(300, 300, fill = 'white', font = 'Times 30 bold', text = 'Player1 and Player2\n have Blackjack!')
            elif self.player.calculate() == 21 and self.dealer.calculate() == 21:
                self.canvas.create_text(300, 300, fill = 'white', font = 'Times 30 bold', text = 'Player1 and Dealer\n have Blackjack!')
            elif self.player_2.calculate() == 21 and self.dealer.calculate() == 21:
                self.canvas.create_text(300, 300, fill = 'white', font = 'Times 30 bold', text = 'Player2 and Dealer\n have Blackjack!')
            elif self.player.calculate() == 21:
                self.canvas.create_text(300, 300, fill = 'white', font = 'Times 30 bold', text = 'Player1 has Blackjack!')
            elif self.player_2.calculate() == 21:
                self.canvas.create_text(300, 300, fill = 'white', font = 'Times 30 bold', text = 'Player2 has Blackjack!')
            elif self.dealer.calculate() == 21:
                self.canvas.create_text(300, 300, fill = 'white', font = 'Times 30 bold', text = 'Dealer has Blackjack!')
        else:
            if self.player.calculate() == 21 and self.dealer.calculate() == 21:
                self.canvas.create_text(300, 300, fill = 'white', font = 'Times 30 bold', text = 'Both have Blackjack!')
            elif self.player.calculate() == 21:
                self.canvas.create_text(300, 300, fill = 'white', font = 'Times 30 bold', text = 'You have Blackjack!')
            elif self.dealer.calculate() == 21:
                self.canvas.create_text(300, 300, fill = 'white', font = 'Times 30 bold', text = 'Dealer has Blackjack!')

    def showResults(self):
        # Print out the result of the game
        if self.two_players:
            if self.player.calculate() == self.dealer.calculate() == self.player_2.calculate():
                self.canvas.create_text(300, 300, fill = 'white', font = 'Times 30 bold', text = 'It\'s a Draw for everyone!')
            elif self.player.calculate() > self.dealer.calculate() and self.player.calculate() > self.player_2.calculate() and not self.bust():
                self.canvas.create_text(300, 300, fill = 'white', font = 'Times 30 bold', text = 'Player1 Wins!')
            elif self.player_2.calculate() > self.dealer.calculate() and self.player_2.calculate() > self.player.calculate() and not self.bust_2():
                self.canvas.create_text(300, 300, fill = 'white', font = 'Times 30 bold', text = 'Player2 Wins!')
            elif self.dealer.calculate() > self.player.calculate() and self.dealer.calculate() > self.player_2.calculate() and not self.bust_dealer():
                self.canvas.create_text(300, 300, fill = 'white', font = 'Times 30 bold', text = 'Dealer Wins!')
            elif self.player.calculate() == self.player_2.calculate() and not self.bust() and not self.bust_2():
                self.canvas.create_text(300, 300, fill = 'white', font = 'Times 30 bold', text = 'It\'s a Draw for \nPlayer1 and Player2!')
            elif self.player.calculate() == self.dealer.calculate() and not self.bust()  and not self.bust_dealer():
                self.canvas.create_text(300, 300, fill = 'white', font = 'Times 30 bold', text = 'It\'s a Draw for \nPlayer1 and dealer!')
            elif self.player_2.calculate() == self.dealer.calculate() and not self.bust_2() and not self.bust_dealer():
                self.canvas.create_text(300, 300, fill = 'white', font = 'Times 30 bold', text = 'It\'s a Draw for \nPlayer2 and dealer!')
        else:
            if self.player.calculate() == self.dealer.calculate():
                self.canvas.create_text(300, 300, fill = 'white', font = 'Times 30 bold', text = 'It\'s a Draw!')
            elif self.dealer.calculate() > self.player.calculate() and not self.bust_dealer():
                self.canvas.create_text(300, 300, fill = 'white', font = 'Times 30 bold', text = 'Dealer Wins!')
            else:
                self.canvas.create_text(300, 300, fill = 'white', font = 'Times 30 bold', text = 'You Win!')
game = GameGUI()