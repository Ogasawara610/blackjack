import random
import sys
card = []

class Deck:
    def __init__(self): #デッキ作り
        self.deck = []
        marks = ["♠","♧","♡","♦"]
        fig = ["A","A","A","A",2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,"J","J","J","J","Q","Q","Q","Q","K","K","K","K"]
        self.deck = [(x,y) for x in fig for y in marks]
        random.shuffle(self.deck)
    def draw_card(self):    #カードを引く
        return self.deck.pop()
    
class Player:
    def __init__(self,name):
        self.time = 0
        self.name = name
        self.hand = []
        self.sum = 0
        self.sum_sub = []
    def hit(self,card):
        self.hand.append(card)
        self.time = self.time + 1
        return self.hand,self.time
    def get_sum(self):    #点数計算
        self.sum = 0
        self.sum_sub = []
        for fig in range(len(self.hand)):
            num = self.hand[fig][0]
            if num == "A":
                if self.sum > 11:
                    fig == 1
                else:
                    fig == 11
            elif num == "J": fig = 10
            elif num == "Q": fig = 10
            elif num == "K": fig = 10
            else:
                fig = int(num)
            self.sum_sub.append(fig)
            self.sum = sum(self.sum_sub)
        return self.sum

def main():
    deck = Deck()
    player = Player("player")
    dealer = Player("dealer")
    tip = 3
    card = deck.draw_card()
    while tip < 0 or input("続けますか？y/n\n") == "y":
        if len(card) == 0:
            card = deck.draw_card()
        else:
            bet = input("何枚掛けますか？※現在{}".format(tip))
            tip = tip - int(bet)
            player.hit(card)
            print("playerの1枚目のカードは{}の{}です".format(player.hand[0][1],player.hand[0][0]))
            card = deck.draw_card()
            dealer.hit(card)
            print("dealerの1枚目のカードは{}の{}です".format(dealer.hand[0][1],dealer.hand[0][0]))
            card = deck.draw_card()
            player.hit(card)
            print("playerの2枚目のカードは{}の{}です".format(player.hand[1][1],player.hand[1][0]))
            card = deck.draw_card()
            dealer.hit(card)
            print("dealerの2枚目のカードはわからないです")
            print(player.hand)
            player_sum = player.get_sum()
            print("playerの合計は{}です\n".format(player_sum))
            while player_sum < 21:
                if input("カードを一枚引きますか？y/n\n") == "y":
                    card = deck.draw_card()
                    player.hit(card)
                    print("playerの{}枚目のカードは{}の{}です\n".format(player.time,player.hand[player.time-1][1],player.hand[player.time-1][0]))
                    print(dealer.hand)
                    player_sum = player.get_sum()
                    print("playerの合計は{}です\n".format(player_sum))
                    if player_sum == 21:
                        print("Natural")
                        break
                    if player_sum > 21:
                        print("playerの負け")
                        sys.exit()
                else:
                    if player_sum == 21:
                        print("Natural")
                    break
            
            print("dealerの2枚目のカードは{}の{}です\n".format(dealer.hand[1][1],dealer.hand[1][0]))
            dealer_sum = dealer.get_sum()
            print("dealerの合計は{}です\n".format(dealer_sum))
            while dealer_sum < 17: 
                if dealer_sum < 17:
                    card = deck.draw_card()
                    dealer.hit(card)      
                    print("dealerの{}枚目のカードは{}の{}です\n".format(dealer.time,dealer.hand[dealer.time-1][1],dealer.hand[dealer.time-1][0]))
                    print(dealer.hand)
                    dealer_sum = dealer.get_sum()  
                    print("dealerの合計は{}です\n".format(dealer_sum))
                    if dealer_sum == 21:
                        print("Natural")
                        break            
                    if dealer_sum > 21:
                        print("playerの勝ち")
                        sys.exit()
                else:
                    if player_sum == 21:
                        print("Natural")
                    break

            if player_sum > dealer_sum:
                print("プレイヤーの勝ち")
                tip = tip + bet*2
                print("持ち枚数は{}枚".format(tip))
            if player_sum == dealer_sum:
                print("引き分け")
                tip = tip + bet
                print("持ち枚数は{}枚".format(tip))
            if player_sum < dealer_sum:
                print("プレイヤーの負け")
                print("持ち枚数は{}枚".format(tip))

main()

    
        