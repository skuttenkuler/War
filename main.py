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

new_deck = Deck()
new_deck.shuffle_deck()
mycard = new_deck.deal_one()
new_player = Player("Sam")
print(new_player)
new_player.add_cards(mycard)
print(new_player)
new_player.add_cards([mycard, mycard,mycard])
new_player.remove
print(new_player.all_cards)
