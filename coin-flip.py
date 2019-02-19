import time
import random

class Player:
    
    def __init__(self, balance, bet):
        self.balance = balance
        self.bet = bet
        
    def checkBalance(self):
        print(f"\nCurrent balance: {self.balance}\n")
        
    def playerWon(self, bet):
        self.balance += self.bet
        
    def playerLost(self, bet):
        self.balance -= self.bet
        
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
        print("\n"*80)
        print("Flipping coin... ", coin_animation[i])
        time.sleep(0.2)
    
    if flip_result == 0:
        flip_print_result = "heads"
    else:
        flip_print_result = "tails"
    
    # Checks if you won
    if  choice == flip_result:
        account.playerWon(amount)
        return f"\nIT CAME UP {flip_print_result.upper()}!\nCongratulations, you won! {amount} has been added to your account!\n"
    else:
        account.playerLost(amount)
        return f"\nIt came up {flip_print_result}.\nSorry, you lost {amount}\n"
    
# Initializes the class
account = Player(1000, 0)

print("\nWelcome to this coin-flip game! \nYou can type in the following: \nHEADS or TAILS = Bet that it will come up heads or tails. \nQUIT or EXIT = Exits the game, you can replay the game until you quit. \n")

print(f"You start with 1000 coins, you can check this by typing in BALANCE or AMOUNT\n")
    
game_off = False
while game_off == False:
    # Assigns values to the input, and checks for correct input
    check = False
    while check == False:
        choice = input("Please write HEADS or TAILS: ")
        if (choice.lower() == "heads") or (choice.lower() == "tails"):
            check = True
        elif choice.lower() == "quit" or choice.lower() == "exit":
            game_off = True
            break
        elif choice.lower() == "balance" or choice.lower() == "amount":
            account.checkBalance()
        
    if game_off == True:
        print("\nThank you for playing!\n")
        break

    while True:
        try:
            bet = int(input("Please choose the amount to bet: "))
            account.bet = bet
            break
        except:
            continue

    # Checks for what input and assigns a number based on input
    if choice.lower() == "heads":
        choice = 0
    elif choice.lower() == "tails":
        choice = 1

    print(coin_flip(choice, bet))