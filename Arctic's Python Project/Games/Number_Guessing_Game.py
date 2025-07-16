#Program to guess a number from 1 to 100
import random

def guessing_game():
    c = 0
    n = int(input("Guess a number ( 1 to 100 ) :"))
    num = random.randint(1,100)
    c += 1
    while n != num :
        if n < num :
            print("Too low")
            n = int(input("Guess a number ( 1 to 100 ) :"))
        elif n > num :
            print("Too high")
            n = int(input("Guess a number ( 1 to 100 ) :"))
        else :
            print("You guessed right!")
            n = num

        c += 1
    if n == num :
        print("Super-b!")
        print("You guessed it correctly!")
        print(f"You got in {c} tries!")

while True :
    guessing_game()
    play_again = input("Play again? (y/n): ").lower()
    if play_again != 'y':
        print("Thanks for playing! Bye!")
        print("See you soon :) ")
        break