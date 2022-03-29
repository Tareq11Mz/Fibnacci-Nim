#Fibonacci Nim #8
#Name: Tareq Mahfouz ID: 20211058
import random
print("\n Rules: Please Read Carefully ")
print(" -the first player will enter number of coins he wants to remove \n -the next move must be less than or equal the double of the previous one till the game ends, \n -the player takes last coin wins, \n -each game starts with a random number of coins.  ")
Ncoins = random.randint(20,50) # giving a random number for coins, Maximum 50 so that the game doesn't take long
coins = int(Ncoins)
#these two variables will be used later to distinguish between each player turn
turns = 0
previous_turns = 0

def fibonacci_nim(coins, turns):
    while coins != 0:
        print("the number of coins is", coins)
        if turns % 2 == 0:
            print("Player1 turn")
            player1 = (input())
            while not player1.isdigit():
                print("play again, enter a number")
                player1 = (input())
            firstmove = int(player1) #assiging the move as an integer to be able to compare its value in the next while loop
            while (firstmove == coins and turns == 0) or (firstmove > coins) or (firstmove <= 0) or (turns>0 and firstmove > (previous_turns*2)):
                print("play again, enter a valid number")
                player1 = (input())
                while not player1.isdigit(): #checking if digit again just incase the user decides to enter another character
                    print("play again, enter a number")
                    player1 = (input())
                firstmove = int(player1) #reassigning the value as an integer incase we go through the previous loop

            #assigning the value of player one to previous_turns so to be compared to player two turn
            previous_turns = firstmove
            coins = coins - firstmove
            EndGame = True

        else:
            print("Player2 turn")
            player2 = (input())
            while not player2.isdigit():
                print("play again, enter a number")
                player2 = (input())
            secondmove = int(player2) #assiging the move as an integer to be able to compare its value in the next while loop
            while (secondmove <=0) or (secondmove > coins) or (secondmove > (previous_turns*2)):
                print("play again, enter a valid number")
                player2 = input()
                while not player2.isdigit(): #checking if digit again just incase the user decides to enter another character
                    print("play again, enter a number")
                    player2 = (input())
                secondmove = int(player2) #reassigning the value as an integer incase we go through the previous loop

            previous_turns = secondmove
            EndGame = False
            coins = coins - secondmove

        turns+=1

    if EndGame == True:
        print("Congratulations Player1, You WON!")
    else:
        print("Congratulations Player2, You WON!")

fibonacci_nim(coins, turns)