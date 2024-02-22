from replit import clear
from art import logo
import random

def get_cards():
    #code for random card picking
    def deal_card():
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        return random.choice(cards)
    user_cards = []
    computer_cards = []

    for i in range(0 , 2):
        #user random element generation
        user_card = deal_card()
        user_cards.append(user_card)

        #computer random element genration
        computer_card = deal_card()
        computer_cards.append(computer_card)
    def calculate_score():
        #calculated user score and computer score
        user_sum = sum(user_cards)
        computer_sum = sum(computer_cards)
        if user_sum == 21 or computer_sum == 21:
            return 0
        elif 11 in user_cards and user_sum > 21:  # ace as 1
            user_cards.remove(11)
            user_cards.append(1)
            user_sum = sum(user_cards)
        while computer_sum != 0 and computer_sum < 17:
            computer_cards.append(deal_card())
            computer_sum = sum(computer_cards)

    calculate_score()

    def compare():
        user_sum = sum(user_cards)
        computer_sum = sum(computer_cards)
        if user_sum == computer_sum:
            print("It's a draw.")
        elif computer_sum == 21:
            print("You Lose.")
        elif user_sum == 21:
            print("You Win.")
        elif user_sum > 21:
            print("You Lose.")
        elif computer_sum > 21:
            print("You Win.")
        elif user_sum > computer_sum :
            print("You Win.")
        else:
            print("You Lose.")

    #this is the final logic of the equation
    print(logo)
    
    print(f"Your cards: {user_cards} and current score: {sum(user_cards)}")
    
    print(f"Computer's first card: {computer_cards[0]}")
    
    if input("Type 'y' to get another card, type 'n' to pass: ") == 'y':
         user_cards.append(deal_card())
        
    calculate_score()
    
    print(f"Your final hand: {user_cards}")
    
    print(f"Computer's final hand: {computer_cards}")
    
    compare()


isplay = True

while isplay:
    if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
        
        clear()
        
        get_cards()
        
    else:
        isplay = False
