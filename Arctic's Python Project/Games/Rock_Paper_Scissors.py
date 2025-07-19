#Program to play Rock Paper Scissors (RPS) with computer
import random

user_score = 0 # 👊 📃 ✂️
computer_score = 0 # 👊 📃 ✂️

#The win_map decides who wins or loses! computer or user. Based on the dictionary, key:value pair!
win_map = {
    "rock": "scissors",
    "scissors": "paper",
    "paper": "rock"
}

choices: list[str] = ["rock", "paper", "scissors"]
def rps() :
    global user_score
    global computer_score
    user_choice = input("Enter your choice (rock 👊 , paper 📃 , or scissors ✂️): ").lower().strip()
    computer_choice = random.choice(choices) #computer picks up a random choice from the choices (list)

    #To validate choice of user, whether it's a valid choice!
    if user_choice not in choices:
        print("Invalid choice. Try again!")
        return

    #Comparison!
    if user_choice == computer_choice: # user choice and computer choice are same --> Tie!
        print("Tie!")
    elif win_map[user_choice] == computer_choice: # user choice is the key and computer got the value! User wins!
        print("You win!")
        user_score += 1
    else :                   # user choice is the value from the win_map and computer got the key! Computer wins!
        print("You lose! | Computer wins!")
        computer_score += 1



#To allow replay!       
while True :
    rps()
    play_again = input("Play again? (y/n): ").lower() # y = yes and n = no
    if play_again != 'y': # Anything apart from 'y' means No!
        print("Thanks for playing! Bye!")
        print("See you soon :) ")
        break

# Gets the scores of user and computer displayed
print(f"Your score is {user_score}")
print(f"Computer score is {computer_score}")
# Will soon do some more tweaks!        
