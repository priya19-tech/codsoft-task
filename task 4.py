import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    if user == computer:
        return 'tie'
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'scissors' and computer == 'paper') or \
         (user == 'paper' and computer == 'rock'):
        return 'user'
    else:
        return 'computer'

def print_scores(user_score, comp_score):
    print(f"\n Scores: You: {user_score} | Computer: {comp_score}\n")

def play_game():
    user_score = 0
    comp_score = 0

    print("Welcome to Rock, Paper, Scissors!")
    print("Instructions: Type 'rock', 'paper', or 'scissors' to play. Type 'exit' to quit.\n")

    while True:
        user_choice = input(" Your move (rock/paper/scissors): ").lower()

        if user_choice == 'exit':
            print(" Thanks for playing! Final scores:")
            print_scores(user_score, comp_score)
            break

        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice! Please try again.")
            continue

        computer_choice = get_computer_choice()
        print(f" Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)

        if result == 'tie':
            print(" It's a tie!")
        elif result == 'user':
            print("You win this round!")
            user_score += 1
        else:
            print(" Computer wins this round!")
            comp_score += 1

        print_scores(user_score, comp_score)

# Start the game
play_game()
