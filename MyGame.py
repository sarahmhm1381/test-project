import random

print("------- WELCOME TO OUR SIMPLE GAME! -------")
print("-------   ROCK ; PAPER ; SCISSORS   -------")

print('\n r is Rock')
print(' p is Paper')
print(' s is Scissors\n')
print('-------------------------------')
randomNumber = random.randint(0,2)

if randomNumber ==0:
    computerMove = 'r'
elif randomNumber ==1:
    computerMove = 's'
elif randomNumber ==2:
    computerMove = 'p'

#print(computerMove)


player1 = input("player1 make your move: ").lower()
player2 = computerMove
print(f'player 2 motivation is {player2}')

if (player1=="r" and player2=="s") or (player1=="p" and player2=="r") or (player1=="s" and player2=="p"):
    print("Player 1 is win!!!")
elif (player2=='r' and player1=='s') or (player2=='p' and player1=='r') or (player2=='s' and player1=='p'):
    print("Player 2 is win!!!")    
elif player1 == player2:
    print("player1 and player2 are equal")  
else:
    print('something happend wrong')
