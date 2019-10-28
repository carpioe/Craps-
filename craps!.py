#EDDIE CARPIO
#10/23/2019
#Craps project
import random
def gamble():
   print("How much would you want to add as your initial bankroll plese enter...")
   return int(input())
def bet_money():
    print("How much would you want to bet?")
    return int(input())
def diceroll():
    roll = random.randint(2,12)
    print(f"you have rolled{roll}")
    return roll
def playgame():
    bank = gamble()
    bet = bet_money()
    dice = diceroll()
    if dice == 7 or dice == 11:
        print("you won!")
        bank = bank - bet
        print(f"You have {bank}")
    elif dice == 2 or dice == 3 or dice == 12:
        print("you lost,sorry")
        bank = bank - bet
        print(f"You have {bank}")
    else:
        print(f"You have made point with {dice}, now you need to roll that number to win")
        point = dice
        dice = random.randint(1,12)
        if(dice == point):
            bank= bank + bet
            print(f"You won, you rolled {dice}, Now you have {bank}.")
        else:
            bank =bank - bet
            print(f"You have rolled {dice}. You have {bank}")
    print(f"Would you like to play again? yes or no?")
    choice = input()

    if choice == "yes":
        print(f"How much you want to bet from your {bank}?")
        bet = int(input())
        dice = diceroll()
    if dice == 7 or dice == 11:
        print("you win!")
        bank = bank + bet
        print(f"you now have${bank}")
    elif dice == 2 or dice == 3 or dice == 12:
        print("You lose")
        bank = bank - bet
        print(f"You know have ${bank}")
    else:
        print(f"You have made point with {dice}, now you need to roll that number to win")
        point = dice
        dice = random.randint(1,12)
        if(dice == point):
            bank= bank + bet
            print(f"You won, you rolled {dice}, Now you have {bank}.")
        else:
            bank= bank - bet
            print(f"you have lost, you rolled {dice}. You have {bank}")
    print("Would you like to play again yes or no?")
    choice = input()

    if (bet >bank):
        print("You do not have the money available the game will end.")
    else:
        print("Goodbye")
        bet = 0

playgame()
