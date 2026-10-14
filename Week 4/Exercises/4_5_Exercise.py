# The Number Guessing Game 
import random

# randomly generate a number between 1 and 10
#secret_guess = random.randint(1,10)
secret_guess = 3
guess_count = 0

print("Welcome to the Number Guessing Game!")
print("You need to try and guess the number between 1 and 10...")
print("If you wish to exit the game enter 0...")

guess = int(input("Please enter a guess:\n"))
if guess == secret_guess:
    print(f"Well done you got the correct answer was {secret_guess}")
else:
    while guess != secret_guess:
        if guess == 0:
            print(f"Program exited. The correct answer is {secret_guess}")
            break
        else:
            if guess<secret_guess:
                print("Your guess is too low. ")
            elif guess>secret_guess:
                print("Your guess is too high. ")
            guess = int(input("Please enter a guess:\n"))
            guess_count +=1
            print(f"Well done the correct answer was {secret_guess}")
            print(f"Count = {guess_count+1}")