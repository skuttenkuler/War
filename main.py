import random
#suits + ranks and values
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two','Three','Four','Five',
          'Six','Seven', 'Eight','Nine',
          'Ten','Jack','Queen','King','Ace')
values = {'Two':2,'Three':3,'Four':4,'Five':5,
          'Six':6,'Seven':7, 'Eight':8,'Nine':9,
          'Ten':10,'Jack': 11,'Queen':12,'King':13,'Ace':14}

#CARD CLASS - has suit and rank and value of card 
class Card:
    def __init__(self, suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    def __str__(self):
        return self.rank + " of " + self.suit
    
ace_of_spades = Card('Spades', 'Ace')
two_of_hearts = Card('Hearts','Two')

#Deck Class
class Deck:
    #create deck
    def __init__(self):
        #all cards list
        self.all_cards = []
        #for loop suit and rank iteration
        for suit in suits:
            for rank in ranks:
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)
    def shuffle_deck(self):
        #shuffle instance of created deck with random
        random.shuffle(self.all_cards)
    def deal_one(self):
        #return single card from top of deck or end of list
        return self.all_cards.pop()
#Player Class
class Player:
    def __init__(self, name):
        self.name = name
        self.all_cards = []
    def remove(self):
        return self.all_cards.pop(0)
    def add_cards(self, new_cards):
        #check if player has a list of cards or not
        if type(new_cards) == type([]):
            #add cards to player "hand"
            self.all_cards.extend(new_cards)
        else:
            #if no "hand" add cards to player
            self.all_cards.append(new_cards)
    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'


'''
GAME
'''
#Setup Game
player_one = Player("one")
player_two = Player("two")
#create the deck
new_deck = Deck()
#shuffle deck
new_deck.shuffle_deck()
#split the deck between players
for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())
game_on = True
#track rounds
round_num = 0
while game_on:

    round_num += 1
    print(f"Round {round_num}")

    if len(player_one.all_cards) == 0:
        print('Player One is out of cards. Winner: Player 2')
    #if P1 loses break loop
        game_on = False
        break

    if len(player_two.all_cards) == 0:
        print('Player Two is out of cards. Winner: Player 1')
    #if P2 loses break loop
        game_on = False
        break

    #start new game round
    player_one_cards = []
    player_one_cards.append(player_one.remove())
    
    player_two_cards = []
    player_two_cards.append(player_two.remove())

    
    at_war = True
   
    while at_war:
         #if P1 wins add cards to hand
        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            at_war = False
        #if P2 wins add cards to hand
        elif player_two_cards[-1].value > player_one_cards[-1].value:
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)
            at_war = False
        #if P1 and P2 have same value call war
        else:
            print("WAR")

            #if P1 hand is less than 3 declare loser
            if len(player_one.all_cards) < 3:
                print("Player 1 must surrender.")
                print("Player 2 is the winner.")
                game_on:False
                break
            #if P2 hand is less than 3 declare loser
            elif len(player_two.all_cards) < 3:
                print("Player 2 must surrender.")
                print("Player 1 is the winner.")
                game_on:False
                break
            else:
                for num in range(3):
                    player_two_cards.append(player_one.remove())
                    player_two_cards.append(player_two.remove())

    