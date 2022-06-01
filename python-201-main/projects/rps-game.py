# ROCK PAPER SCISSORS GAME
# take in a number 0-2 from the user that represents their hand
# generate a random number 0-2 to use for the computer's hand
# call the function get_hand to get the string representation of the user's hand
# call the function get_hand to get the string representation of the computer's hand
# call the function determine_winner to figure out who won
# print out the player hand and computer hand
# print out the winner

import random

def get_hand(hand):
    hands = ["rock", "paper", "scissors"]
    if hand == 0:
        return hands[0]
    if hand == 1:
        return hands[1]
    if hand == 2: 
        return hands[2]
    else:
        print("Please enter 0, 1, or 2.")

def determine_winner(p_hand, c_hand):
    win = "You win!"
    lose = "You lose :-("
    draw = "You tied..."
    if p_hand == c_hand:
        return draw
    if p_hand == "rock" and c_hand == "scissors":
        return win
    if p_hand == "paper" and c_hand == "rock":
        return win
    if p_hand == "scissors" and c_hand == "paper":
        return win
    else:
        return lose


play_again = 'yes'
wins = 0
losses = 0
draws = 0

print("Welcome to Rock, Paper, Scissors!")

while play_again.lower() == 'yes':

    computer_input = random.randint(0, 2)
    computer_hand = get_hand(computer_input)

    player_input = int(input("0 for Rock - 1 for Paper - 2 for Scissors\nEnter your choice: "))
    player_hand = get_hand(player_input)

    print(f"\nYou chose: {player_hand}")
    print(f"Computer chose: {computer_hand}")

    result = (determine_winner(player_hand, computer_hand))
    print(result)
    
    if result == "You win!":
        wins += 1
    if result == "You lose :-(":
        losses += 1
    if result == "You tied...":
        draws += 1
    score_board = f"Wins: {wins} | Losses: {losses} | Draws {draws}"

    print(f"\n{score_board}\n")

    play_again = input("Play again? Enter 'yes' or 'no': ")
