import random
import os

numPlayers = 2
players = {}
startingCards = 7
winner = None
unlimitedDraw = False

# Player class: 
class Player:

    def __init__(self, playerNumber):
        self.playerNumber = playerNumber
        self.cards = []
        self.numCards = startingCards

    def printHand(self):
        for i in range(len(self.cards)):
            self.cards[i].printCard(i)

    def draw(self, deck):
        self.cards.append(deck.cards.pop())
        self.numCards += 1


class Deck:
    def __init__(self):
        self.cards = []
        colors = ["Red", "Blue", "Green", "Yellow"]
        for i in range(4):
            for j in range(10):
                self.cards.append(Card(colors[i], j))
                if j != 0:
                    self.cards.append(Card(colors[i], j))
        random.shuffle(self.cards)
        self.topCard = self.cards.pop()

    def printDeck(self):
        for card in self.cards:
            card.printCard()


class Card:
    def __init__(self, color, number):
        self.color = color
        self.number = number

class SpecialCard(Card):
    def __init__(self, number):
        if number == 10:
            self.specialAbility = "Draw 2"


        # can have the additional powers assigned by number
        # i.e. 10 = draw 2
        # 11 = skip
        # 12 = reverse
        # 13 = wild card
        # 15 = draw four

    def printCard(self, number):
        print(str(number + 1) + ": " + str(self.color) + " " + str(self.number))
        # print("Color: " + str(self.color) + ", Number: " + str(self.number))

def createPlayers(deck):
    # create players
    for i in range(1, numPlayers + 1):
        players[i] = Player(i)
    # give players cards
    for i in players:
        for j in range(startingCards):
            players[i].cards.append(deck.cards.pop())
    

def printAllHands():
    for i in players:
        print("Player: " + str(i))
        players[i].printHand()
        print()


def playGame(deck):
    while (victory() != True):
        for i in players:
            os.system('cls||clear')
            currentPlayer = players[i]
            currentCard = deck.topCard
            print("-----")
            print("Current card: " + str(currentCard.color) + " " + str(currentCard.number))
            print()
            ready = input("Player " + str(currentPlayer.playerNumber) + ", press key to see cards: ")
            

            # if player has a valid move, let them do it
            # otherwise make them draw
            # if they can play after drawing, give them a change to do so
            # otherwise advance to the next player
            drewCard = False
            if hasValidMove(deck, currentPlayer) == False:
                if unlimitedDraw == True:
                    while (hasValidMove(deck, currentPlayer) != True):
                        print("No valid moves, draw card")
                        print()
                        currentPlayer.draw(deck)
                        currentPlayer.printHand()
                        drewCard = True
                else:
                    print("DRAW CARD")
                    currentPlayer.draw(deck)
                    currentPlayer.printHand()
                    drewCard = True

            if hasValidMove(deck, currentPlayer) == False:
                print()
                next = input("~~ NO VALID MOVES ~~ enter to continue: ")
                continue

            if drewCard == False:
                currentPlayer.printHand()

            flag = False
            card = None
            while flag == False:
                cardNumber = int(input("Enter the card number you wish to play: "))
                cardIndex = cardNumber - 1
                card = currentPlayer.cards[cardIndex]
                if verifyCard(deck, card) == True:
                    currentPlayer.numCards -= 1
                    flag = True
            
            tempCard = currentPlayer.cards.pop(cardIndex)
            deck.topCard = tempCard
            print()
            victory()
            next = input("Enter key to continue: ")

def hasValidMove(deck, player):
    for card in player.cards:
        if (deck.topCard.number == card.number or deck.topCard.color == card.color):
            return True
    return False

def verifyCard(deck, card):
    if (deck.topCard.number == card.number or deck.topCard.color == card.color):
        return True
    return False



def victory():
    for i in players:
        if players[i].numCards == 0:
            winner = players[i]
            print("The winner is: Player " + str(i))
            quit()
    return False



def main():
    deck = Deck()
    createPlayers(deck)
    playGame(deck)


main()
