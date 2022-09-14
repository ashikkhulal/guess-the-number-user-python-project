import random

x = int(input(f"Please enter a whole number above 1: "))

while x < 2:
    print("Error! you did not enter a whole number above 1.")
    x = int(input(f"Let us try again! Please reenter a whole number above 1: "))

def guess(x):
    random_number = random.randint(1, x)
    guess = 0 
    while guess != random_number:
        guess = int(input(f"Awesome! Now guess a number between 1 and {x}: "))
        if guess < random_number:
            print ("Sorry, guess again. Too low.")
        elif guess > random_number:
            print ("Sorry, guess again. Too high.")

    print(f"Yay, congrats. You have correctly guessed the random number ({random_number}) that was between 1 and {x}!!!")

guess(x)