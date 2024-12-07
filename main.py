import random

def deal_card():
    '''returns a random card from the deck'''
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    '''take a list of cards and return score calculated from the cards '''
    if 11 in cards and 10 in cards and len(cards) == 2:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(user_score, computer_socre):
    if user_score == computer_socre:
        return "Draw"
    elif user_score > 21 and computer_socre > 21:
        return "Draw"
    elif computer_socre == 0:
        return "Lose, opponent has blackjack"
    elif user_score == 0:
        return "Win with a blackjack"
    elif user_score > 21:
        return "Lose you went over"
    elif computer_socre > 21:
        return "Win opponent went over"
    elif user_score > computer_socre:
        return "You win"
    else:
        return "You lose"

def play_game():

    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    is_game_over = False


    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())


    while not is_game_over:

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {calculate_score(user_cards)}")
        print(f"Computer's first card: {computer_cards[0]}")
        print("\n")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get anther card, type 'n' to pass: ").lower()
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score,computer_score))

while input("Do you want to play a game of blackjack? Type 'y' or 'n': ").lower() == "y":
    print("\n" * 20)
    play_game()