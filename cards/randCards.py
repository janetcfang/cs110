import random

class Card: 
    def __init__(self,suit,value):
        self.suit = suit 
        self.value = value
        
    def __str__(self): 
        return str(self.value)  + " of "  +  str(self.suit) 

    

class Deck: 
    def __init__(self):
        self.cards = list()
        self.suits = ["Hearts","Diamonds","Spades","Clubs"]
        self.cardDic={2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:'10',11:'Jack',12:'Queen',13:'King',14:'Ace'}
        self.yay = [2,3,4,5,6,7,8,9,10,"Jack","Queen","King","Ace"]
               
        for suit in self.suits:
            for i in self.yay:  
                c = Card(suit,i,)
                self.cards.append(c)

    def __str__(self): 
        for card in self.cards: 
            print(card)   
        return "END"
        
    def dealCard(self):
        randomIndex = random.randrange(0, self.cards.__len__()) 
        randomCard = self.cards[randomIndex]
        self.cards.pop(randomIndex)
        return randomCard
#main
d = Deck()
print d.dealCard()
print d.dealCard()
print d.dealCard()
print d.dealCard()
print d.dealCard()
