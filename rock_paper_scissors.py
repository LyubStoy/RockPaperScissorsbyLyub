import random
computer_move=""
rock='Rock'
paper='Paper'
scissors='Scissors'
<<<<<<< HEAD
play_continue=True

while play_continue:

    player_move=input("Choose [r]ock,[p]aper or [s]cissors:")

    if player_move=='r':
        player_move=rock
    elif player_move=='p':
        player_move=paper
    elif player_move=='s':
        player_move=scissors
    else :
        raise SystemExit("Invalid Input. Try again...")

    computer_random_number=random.randint(1,3)

    if computer_random_number==1:
        computer_move=rock
    elif computer_random_number==2:
        computer_move=paper
    else :
        computer_move=scissors

    if (player_move==rock and computer_move==scissors) or \
        (player_move==paper and computer_move==rock) or \
        (player_move==scissors and computer_move==paper) :
        print("You win!")
    elif player_move==computer_move:
        print("Draw")
    else :
        print("You lose!")

    continue_or_not=input("Type [yes] to Play Again or [no] to quit:")
    if continue_or_not=='yes':
        continue
    else :
        print("Thank you for playing!")
        #play_continue=false
        break
=======
player_move=input("Choose [r]ock, [p]aper or [s]cissors:")
if player_move=='r':
    player_move=rock
elif player_move=='p':
    player_move=paper
elif player_move=='s':
    player_move=scissors
else :
    raise SystemExit("Invalid Input. Try again...")
computer_random_number=random.randint(1,3)

if computer_random_number==1:
    computer_move=rock
elif computer_random_number==2:
    computer_move=paper
else :
    computer_move=scissors

print(f"The computer chose {computer_move}.")


if (player_move==rock and computer_move==scissors) or \
        (player_move==paper and computer_move==rock) or \
        (player_move==scissors and computer_move==paper) :
    print("You win!")
elif player_move==computer_move:
    print("Draw")
else :
    print("You lose!")

>>>>>>> 2b86da205b09d15d728d73f66984afa1e089a9de
