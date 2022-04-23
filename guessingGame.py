import random

guess = 0
number = random.randint(0, 10)

while( guess < 3 ):
    u_guess = int(input("Have a guess: "))

    if u_guess == number:
        print("Well done, you win!")
        break
    elif u_guess > number:
        print("Your guess was too high.")
        guess = guess + 1
    elif u_guess < number:
        print("Your guess was too low.")
        guess = guess + 1
    else:
        print("There was an error.")

if guess == 3:
    print("You lose!")
    print("The number was: " + str(number))