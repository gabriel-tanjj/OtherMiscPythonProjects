import random

EASY_TURNS = 10
HARD_TURNS = 5

#Function to check user's guess
def check_answer(guess, answer, turns):
    """Checks answer against guess, returns number of turns remaining"""
    if guess > answer:
        print("Too high")
        return turns - 1
    elif guess < answer:
        print("Too low")
        return turns - 1
    else:
        print(f"Correct answer! The answer is {answer}")

def set_difficulty():
    """Returns a variable tied to an integer as predefined above based on the user specified difficulty"""
    level = input("Choose a difficulty. Type easy or 'hard: ")
    if level == "easy":
        return EASY_TURNS
    else:
        return HARD_TURNS

def start_game():
    """Function for the while loop to keep user guessing, to call check_answer() function here to decide on outcome of guess"""
    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(1, 100)

    turns = set_difficulty()
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts to guess the right answer.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You're out of attempts")
        elif guess != answer:
            print("Guess again")

start_game()


