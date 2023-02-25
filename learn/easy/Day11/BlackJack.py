# Black Jack game!!
import random
import sys

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards_score):
    result = sum(cards_score)
    if result > 21:
        print("OH no Black Jack!!")
        sys.exit("GO back to your home!")

def compare(user, dealer):
    if sum(dealer) > 21:
        sys.exit("You win Good!")
    elif sum(dealer) == sum(user):
        sys.exit("Same!")
    elif sum(dealer) < sum(user):
        sys.exit("You win Good!")

def Bye():
    print("GOOD BYE! DO not Bet again!")
    sys.exit("GG")

user_answer = input("Do you want to play a game of Blackjack?? Type 'y' or 'n : \n")

if user_answer == 'y':
    # 카드 생성
    user_card = []
    user_card.append(deal_card())
    user_card.append(deal_card())
    dealer_card = []
    dealer_card.append(deal_card())
    print(f"Your cards are [{user_card[0]}, {user_card[1]}]")
    print(f"Your score is now : {sum(user_card)}")
    print(f"And dealer card is [{dealer_card[0]}]")
    print(f"Dealer score is now : {sum(dealer_card)}")

    user_hit = input('Do you want to "hit" or "no"??\n')
    if user_hit == "hit":
        user_card.append(deal_card())
        print(f"Your new card is {user_card[-1]}")
        calculate_score(user_card)
        dealer_card.append(deal_card())
        print(f"Your score is now : {sum(user_card)}")
        calculate_score(dealer_card)
        # 시작
        money = True
        while money is True:
            user_hit = input('Do you want to "hit" or "no"??\n')
            if user_hit != "hit":
                print(f"Dealer card is {dealer_card[-1]}")
                print(f"Dealer score is now : {sum(dealer_card)}")
                compare(user_card, dealer_card)
                user_card.append(deal_card())
                print(f"Your new card is {user_card[-1]}")
                calculate_score(user_card)
                dealer_card.append(deal_card())
                print(f"Your score is now : {sum(user_card)}")
                calculate_score(dealer_card)

    else:
        Bye()

else:
    Bye()
