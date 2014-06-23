def compare(choice1, choice2):
    """rock, paper, scissors match evaluator"""
    if choice1 == choice2:
        print("It is a tie!")
    elif choice1 == 'rock':
        if choice2 == 'scissors':
            print('Rock wins!')
        elif choice2 == 'paper':
            print('Paper wins!')
    elif choice1 == 'paper':
        if choice2 == 'scissors':
            print('Scissors wins!')
        elif choice2 == 'rock':
            print('paper wins!')
    elif choice1 == 'scissors':
        if choice2 == 'paper':
            print ('Scissors wins!')
        elif choice2 == 'rock':
             print('Rock wins!')


             
rounds = int(raw_input("enter number of rounds:")
for x in range (3):
    choice1 = choice()
    choice2 = choice()
    compare(choice1, choice2)
