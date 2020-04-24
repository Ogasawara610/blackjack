import random

def all_card():
    marks = ["♠","♧","♡","♦"]
    num = range(1,14)
    trump = [(x,y) for x in num for y in marks]
    random.shuffle(trump)
    return trump

player_time = 1
def main():
    player_hand = []
    dealer_hand = []
    trump = all_card()
    #print(trump)
    card = trump.pop()  #P1,D0
    player_hand.append(card)
    card = trump.pop()  #P1,D1
    dealer_hand.append(card)
    card = trump.pop()  #P2.D1
    player_hand.append(card)
    card = trump.pop()  #P2,D2
    dealer_hand.append(card)
    #player_sum = int(player_hand[0][0])+int(player_hand[1][0])
    for i in player_time:
        player_sum = sum(player_hand[i][0])
    dealer_sum = int(dealer_hand[0][0])+int(dealer_hand[1][0])
    #print(player_hand)
    print("あなたは"+str(player_hand[0][1])+"の"+str(player_hand[0][0])+"と"+str(player_hand[1][1])+"の"+str(player_hand[1][0])+"の合計"+str(player_sum)+"")
    #print(dealer_hand[0])
    print("ディーラーは"+str(dealer_hand[0][1])+"の"+str(dealer_hand[0][0])+"です")
    #と"+str(dealer_hand[1][1])+"の"+str(dealer_hand[1][0])+"の合計"+str(dealer_sum)+"")
#    input = input("カードを引きますか yes/no:")
#    if input == "yes":
#        card = trump.pop() #P2+
#        player_hand.append(card)
#        player_sum = int(player_hand[0][0])+int(player_hand[1][0])

if __name__ == '__main__':
    main()
