# Tell the human you're thinking of a number between 1 and 100
# Tell the human they must guess that number in 7 turns, or else they lose

# If guessed number > thought number, say "number is too high." + number of guesses left
# If guessed number < thought number, say "number is too low." + number of guesses left
# If guessed number = thought number, say "That's the number I'm thinking of!"

# If user can't guess number in 7 or less tries, say "You weren't able to guess the number in 7 tries or less - you lose."
# If user guesses number in 7 or less tries, say "You guessed the number in [INSERT NUMBER OF TURNS TAKEN TO GUESS NUMBER] tries! - you win!"

import random
print("Hey buddy! I'm thinking of a number between 1 and 100. You gotta guess it in 7 turns, or else you lose.")
randomNumber = random.randint(1, 100)
tries = 0

keepGoing = True
while (keepGoing):
    tries += 1
    guess = int(input("What's the number I'm thinking of?: "))
    
    if guess > randomNumber:
        print("Too high - guess again")
    
    if guess < randomNumber:
        print("Too low - guess again")
    
    if guess == randomNumber:
        print(f"Good Job! You guessed the number in {tries} tries! You won!")
        keepGoing = False
    else:
        print("You were't able to guess the number in 7 tries or less. You lose, you fool...")
        keepGoing = False
