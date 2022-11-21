import random, sys
################################################################################################
print("Hello, let's start the game...- Rock, Paper, Scissors!")

#Variables for gameplay results
wins = 0
losses = 0
draw = 0

#Main game code
while True:
    print(f'Your score is - {wins} wins, {losses} losses, {draw} draw')
    while True:
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit: ')
        playerChoice = input() #Player choice
        if playerChoice == 'q' or playerChoice == 'Q': #Exit the game
            print("Exit game")
            sys.exit()
        if playerChoice == 'r' or playerChoice == 'p' or playerChoice == 's': #Validation of the selection
            break
        print('Type one of r, p, s, or q.: ')
    #User movement display
    if playerChoice == 'r':
        print('Rock vs.. ')
    elif playerChoice == 'p':
        print('Paper vs.. ')
    elif playerChoice == 's':
        print('Scissors vs.. ' )
    #Draw computer movement
    randomNumer = random.randint(1, 3)
    if randomNumer == 1:
        pcChoice = 'r'
        print('Rock')
    elif randomNumer == 2:
        pcChoice = 'p'
        print('Paper')
    elif randomNumer == 3:
        pcChoice = 's'
        print('Scissors')
    #Counting variable game results
    if playerChoice == pcChoice:
        print('We have a tie!')
        draw += 1
    elif playerChoice == 'r' and pcChoice == 's':
        print('You win this round!')
        wins += 1
    elif playerChoice == 'p' and pcChoice == 'r':
        print('You win this round!')
        wins += 1
    elif playerChoice == 's' and pcChoice == 'p':
        print('You win this round!')
        wins += 1
    elif playerChoice == 'r' and pcChoice == 'p':
        print('You lose this round!')
        losses += 1
    elif playerChoice == 'p' and pcChoice == 's':
        print('You lose this round!')
        losses += 1
    elif playerChoice == 's' and pcChoice == 'r':
        print('You lose this round!')
        losses += 1