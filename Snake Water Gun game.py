import random
print('***** Snake - Water - Gun *****')
options = ['s', 'w', 'g']
while True:
    computer = random.choice(options)    
    player = input("Enter your choice : 's' for snake , 'g' for gun and 'w' for water --> ")
    print("Computer's choice was", computer)
    if computer == 's':
        if player == 'w':
            print('Computer won')
        elif player == 'g':
            print('You Won!')
        else:
            print('Draw!')
    elif computer == 'w':
        if player == 's':
            print('You Won!')
        elif player == 'g':
            print('Computer won')
        else:
            print('Draw!')
    elif computer == 'g':
        if player == 's':
            print('Computer won')
        elif player == 'w':
            print('You Won!')
        else:
            print('Draw!')
    print('Thanks for playing')



