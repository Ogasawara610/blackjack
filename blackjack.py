import random
import sys

rank = 0
def get_point(hand):
    result = 0
    for card in hand:
        if card[rank] > 10:
            num = 10
        else:
            num = card[rank]
        result = result + num
    return result

def all_card():
    marks = ["♠","♧","♡","♦"]
    num = range(1,14)
    trump = [(x,y) for x in num for y in marks]
    random.shuffle(trump)
    print(trump)
    return trump

def main():
    player_hand = []
    dealer_hand = []
    trump = all_card()
    card = trump.pop()  #P1,D0
    player_hand.append(card)
    card = trump.pop()  #P1,D1
    dealer_hand.append(card)
    card = trump.pop()  #P2.D1
    player_hand.append(card)
    card = trump.pop()  #P2,D2
    dealer_hand.append(card)
    player_time = 2
    dealer_time = 2
    player_sum = get_point(player_hand)
    dealer_sum = get_point(dealer_hand)

    print("プレイヤーは"+str(player_hand[0][1])+"の"+str(player_hand[0][0])+"と"+str(player_hand[1][1])+"の"+str(player_hand[1][0])+"の合計"+str(player_sum)+"")
    print("ディーラーは"+str(dealer_hand[0][1])+"の"+str(dealer_hand[0][0])+"")

    while player_sum <21:
        choice = input("カードを引きますか yes/no:")
        if choice in ("yes","Yes","y"):
            print("プレイヤーがもう一枚引く")
            card = trump.pop() #P2+
            player_time = player_time + 1
            player_hand.append(card)
            player_sum = get_point(player_hand)
            print("プレイヤーの持ちカードは")
            for y in range(0,player_time):
                print(""+str(player_hand[y][1])+"の"+str(player_hand[y][0])+"と")
            print("合計"+str(player_sum)+"")
            if player_sum > 21:
                print("burst")
                print("プレイヤーの負け")
                sys.exit()
        if choice in ("no","No","n"):
            break
    print("ディーラーの2枚目は"+str(dealer_hand[1][1])+"の"+str(dealer_hand[1][0])+"の合計"+str(dealer_sum)+"")

    while dealer_sum < 17:
        print("ディーラーが一枚引く")
        card = trump.pop() #D2+
        dealer_hand.append(card)
        dealer_time = dealer_time + 1
        dealer_sum = get_point(dealer_hand)
        print("ディーラーは")
        for yy in range(0,dealer_time):
            print(""+str(dealer_hand[yy][1])+"の"+str(dealer_hand[yy][0])+"と")
        print("の合計"+str(dealer_sum)+"")
        if dealer_sum >21:
            print("burst")
            print("プレイヤーの勝ち")
            sys.exit()
    else:
        print("ディーラーは")
        for yy in range(0,dealer_time):
            print(""+str(dealer_hand[yy][1])+"の"+str(dealer_hand[yy][0])+"と")
        print("の合計"+str(dealer_sum)+"")

    if player_sum > dealer_sum:
        print("プレイヤーの勝ち")
    if player_sum == dealer_sum:
        print("引き分け")
    if player_sum < dealer_sum:
        print("プレイヤーの負け")

if __name__ == '__main__':
    main()
