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


             
rounds = int(raw_input("enter number of rounds:"))
player1_name = raw_input("Enter player1 name: ")
player2_name = raw_input("Enter player2 name: ")
counter = 0
while counter != rounds:            
    choice1 = choice()
    choice2 = choice()
    compare(choice1, choice2)
    counter += 1
    print("{} and {} thanks for playing!".format(player1_name, player2_name))
