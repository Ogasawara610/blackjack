import random
import sys

class Deck:
    def __inti__(self): #デッキ作り
        self.deck = []
        marks = ["♠","♧","♡","♦"]
        fig = ["A","A","A","A",2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,"J","J","J","J","Q","Q","Q","Q","K","K","K","K"]
        self.deck = [(x,y) for x in fig for y in marks]
        random.shuffle(self.deck)
    def draw_card(self):    #カードを引く
        return self.deck.pop()

class Card():
    def __inti__(self,name):
        self.name = name
        self.sum = 0
        self.hand = []
        self.time = 0
    #def get_card(self):
        #self.hand = draw_card()
        #self.time = self.time + 1
        #return self.time,self.hand
    def get_sum(self):    #点数計算
        for card in len(self.hand):
            if card == "A": return 1
            if card == "J": return 10
            if card == "Q": return 10
            if card == "K": return 10
            else:
                fig = int(card)
            self.sum = self.sum + fig
            return self.sum
    def get_card(self,display=True):
        self.time = self.time + 1
        #カード表示
        if display:
            print("{}のカードは{}の{}です".format(self.name,self.hand[self.time][self.time],self.hand[self.time][self.time+1]))
        else:
            print("{}のカードはわかりません".format(self.name))
        return self.time,self.hand
    def over_twenty_one(self):
        if self.sum > 21:
            return True
        return False

class Player(Card):
    def is_continue(self):
        print("{}の合計は{}".format(self.name,self.sum))
        if input("カードを引きますか？y/n") == "y":
            return True
        return False

class Dealer(Card):
    def is_continue(self):
        print("{}の合計は{}".format(self.name,self.sum))
        if self.sum > 17:
            return True
        return False

def main():
    deck = Deck()
    player = Player('player')
    dealer = Dealer('dealer')
    player.get_card(deck.draw_card())
    dealer.get_card(deck.draw_card())
    player.get_card(deck.draw_card())
    dealer.get_card(deck.draw_card(),display = False)

    while player.is_continue():
        player.get_card(deck.draw_card())
        if player.over_twenty_one():
            print('21 を越えました')
            print('あなたの負けです')
            break

    if not player.over_twenty_one():
        print("dealerの{}枚目のカードは{}の{}です".format(dealer.time+1,dealer_hand[dealer.time+1][dealer.time],dealer_hand[dealer.time+1][dealer.time+1]))
        while dealer.is_continue():
            dealer.hand(deck.draw_card())

        if dealer.over_twenty_one() or player.get_sum() >= dealer.get_sum():
            print('あなたの勝ちです')
        else:
            print('あなたの負けです')
main()
