import time
import random

def coin_flip(players_choice, amount):
    """
    This function flips a coin and returns if a player won.
    INPUT: players choice, bet amount
    """
    # Assigns a random value (0 or 1) to flip_result
    flip_result = random.randint(0,1)
    
    # Animating the loading / coin flip with a pause at 0.2s for each print
    coin_animation = ["––","\\","|","/","––","\\","|","/","––"]
    for i in range(0,9):
        print("\n"*30)
        print("Flipping coin... ", coin_animation[i])
        time.sleep(0.2)
        
    # Checks if you won
    if  choice == flip_result:
        return f"Congratulations, you won! {amount*2} has been added to your account!"
    else:
        return f"Sorry, you lost {amount}"

# Assigns values to the input, and checks for correct input
check = False

while check == False:
    choice = input("Please write HEADS or FALSE: ")
    if choice == "heads" or choice == "tails":
        check = True

while True:
    try:
        bet = int(input("Please choose the amount to bet: "))
        break
    except:
        continue

# Checks for what input and assigns a number based on input
if choice == "heads":
    choice = 0
elif choice == "tails":
    choice = 1
    
print(coin_flip(choice, bet))