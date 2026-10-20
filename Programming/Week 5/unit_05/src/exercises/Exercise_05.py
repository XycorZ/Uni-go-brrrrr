import random


def get_user_guess():
    """ gets the user input"""
    # remove the following line and write the function here
    guess = (input("Enter number for guess:\n"))
    return guess
    


def print_feedback(no_guesses, max_guesses, secret_num):
    """ prints the end feedback """
    # remove the following line and write the function here
    if no_guesses>max_guesses:
        print ("Sorry, better luck next time.")
    else:
        print(f"Well done, you used {no_guesses}/{max_guesses} guesses to guess the secret number {secret_num}.")

    


def main():
    secret_num = random.randint(1, 10)
    keep_going = True
    max_guesses = 3
    no_guesses = 0

    while keep_going:
        if no_guesses < max_guesses:
            guess = get_user_guess()
            if guess == "q":
                keep_going = False
            else:
                try:
                    if int(guess) == secret_num:
                        keep_going = False
                    elif int(guess) >10:
                        print("Invalid input")
                    else:
                        print("Incorrect, please try again\n")
                except ValueError:
                    print("Invalid input\n")

        else:
            keep_going = False

        no_guesses += 1

    if guess == "q":
        print("User exited the program.")
    else:
        print_feedback(no_guesses, max_guesses, secret_num)


if __name__ == "__main__":
    # call the main() function to run the whole program
    main()

    # Uncomment any of these lines to test the functions on their own. You will probably want to comment out the call to main() as well.

    # get_user_guess()
    # print_feedback(2, 3, 5) # should print Well done, you used 2/3 guesses to guess the secret number 5.
    # print_feedback(4, 3, 6) # should print Sorry, better luck next time.