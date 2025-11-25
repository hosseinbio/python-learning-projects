import random

choices = ["rock", "paper", "scissors"]
computer_score = 0
player_score = 0


def computers_choice():
    return random.choice(choices)


def players_choice():
    while True:
        player_choice = input(
            f"Insert your choice {choices} or press 'q' to quit: "
        ).lower()
        if player_choice == "q":
            return "q"
        elif player_choice not in choices:
            print("Wrong input!")
        else:
            return player_choice


def winner(computer_choice, player_choice):
    win_decide = [("rock", "scissors"), ("scissors", "paper"), ("paper", "rock")]
    if computer_choice == player_choice:
        return "Tie"
    elif (computer_choice, player_choice) in win_decide:
        return "Computer wins"
    else:
        return "You win"


def score(result, computer_score, player_score):
    if result == "Computer wins":
        computer_score += 1
    elif result == "You win":
        player_score += 1
    print(f"Computer's score: {computer_score} - Your score: {player_score}")
    return computer_score, player_score


def play():
    global computer_score, player_score
    computer = computers_choice()
    player = players_choice()
    if player == "q":
        print("Game exited.")
        exit()
    result = winner(computer, player)
    print(f"{result}! Your choice: {player}, computer's choice: {computer}")
    computer_score, player_score = score(result, computer_score, player_score)


if __name__ == "__main__":
    while True:
        play()
