#EDDIE CARPIO
#10/23/2019
#Craps project
import random
def gamble():
   print("How much would you want to add as your initial bankroll.")
   return int(input())
bank = gamble()
print(f"How much from your total of {bank} on this round?")
bet = int(input())
while bet <= 0:
    print("Invalid try again")
    bet = int(input())
while bank > 0 and bet > 0:
    roll = random.randint(2,12)

    print(f"You have rollled {roll}")

    if roll == 7 or roll == 11:
        print("you win!")
        bank = bank + bet
        print(f"you now have${bank}")
    elif roll == 2 or roll == 3 or roll == 12:
        print("You lose")
        bank = bank - bet

