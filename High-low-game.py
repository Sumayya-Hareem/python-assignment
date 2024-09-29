import random

NUM_ROUNDS = 5
score = 0

for round_number in range(1, NUM_ROUNDS + 1):
    print(f"\nRound {round_number}:")
    
    player_number = random.randint(1, 100)
    computer_number = random.randint(1, 100)
    
    print(f"Your number is {player_number}")

    while True:
        user_guess = input("Do you think your number is higher or lower than the computer's ? (type 'higher' or 'lower'): ").strip().lower()
        if user_guess in ["higher", "lower"]:
            break
        else:
            print("Invalid input! Please type 'higher' or 'lower'.")

    if (user_guess == "higher" and player_number > computer_number) or (user_guess == "lower" and player_number < computer_number):
        print(f"You were right! The computer's number was {computer_number}")
        score += 1
    else:
        print(f"Aww, that's incorrect. The computer's number was {computer_number}")
        
    print(f"Your score is now {score}/{round_number}")

if score == NUM_ROUNDS:
    print("Perfect score! You're a genius!")
elif score > NUM_ROUNDS / 2:
    print("Good job, you played really well!")
else:
    print("Better luck next time!")